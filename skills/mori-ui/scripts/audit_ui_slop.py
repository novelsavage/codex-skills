#!/usr/bin/env python3
"""Flag common AI-generated UI defaults for human review."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


SOURCE_EXTENSIONS = {
    ".astro",
    ".css",
    ".html",
    ".js",
    ".jsx",
    ".less",
    ".sass",
    ".scss",
    ".svelte",
    ".ts",
    ".tsx",
    ".vue",
}

EXCLUDED_DIRECTORIES = {
    ".git",
    ".next",
    ".nuxt",
    ".output",
    ".svelte-kit",
    ".vercel",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "out",
    "vendor",
}

SEVERITY_ORDER = {"low": 1, "medium": 2, "high": 3}


@dataclass(frozen=True)
class Finding:
    rule: str
    severity: str
    path: str
    line: int
    message: str
    excerpt: str


@dataclass(frozen=True)
class LineRule:
    rule: str
    severity: str
    pattern: re.Pattern[str]
    message: str


LINE_RULES = (
    LineRule(
        "rounded-shadow-surface",
        "medium",
        re.compile(
            r"(?=.*(?:rounded-(?:xl|2xl|3xl)|border-radius\s*:\s*(?:1[6-9]|[2-9]\d)px))"
            r"(?=.*(?:shadow-(?:lg|xl|2xl)|box-shadow\s*:[^;]*(?:1[2-9]|[2-9]\d)px))",
            re.IGNORECASE,
        ),
        "大きな角丸と影の組合せ。独立した浮遊対象でなければ別の境界表現を検討してください。",
    ),
    LineRule(
        "glass-surface",
        "medium",
        re.compile(r"(?:backdrop-blur|backdrop-filter\s*:\s*blur)", re.IGNORECASE),
        "ガラス表現を検出。背景文脈を残す必要があるか確認してください。",
    ),
    LineRule(
        "decorative-sparkles",
        "low",
        re.compile(r"(?:✨|🪄|Sparkles(?:Icon)?)"),
        "装飾的なキラキラ表現を検出。機能上の意味があるか確認してください。",
    ),
    LineRule(
        "generic-copy",
        "high",
        re.compile(
            r"(?:可能性を解き放|体験を再定義|次世代の|未来を創|"
            r"unlock (?:the |your )?potential|redefine (?:the |your )?experience|"
            r"revolutioni[sz]e|supercharge your|seamlessly connect)",
            re.IGNORECASE,
        ),
        "製品固有の情報が薄い定型コピーを検出。対象・操作・結果を直接書いてください。",
    ),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="UIソースからAIテンプレ的な表現の候補を抽出します。",
    )
    parser.add_argument("path", type=Path, help="監査するファイルまたはディレクトリ")
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="出力形式（既定: text）",
    )
    parser.add_argument(
        "--fail-on",
        choices=("never", "low", "medium", "high"),
        default="never",
        help="指定以上の重大度があれば終了コード1（既定: never）",
    )
    return parser.parse_args()


def iter_source_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target] if target.suffix.lower() in SOURCE_EXTENSIONS else []

    files: list[Path] = []
    for root, directory_names, file_names in os.walk(target):
        directory_names[:] = sorted(
            name for name in directory_names if name not in EXCLUDED_DIRECTORIES
        )
        root_path = Path(root)
        for file_name in sorted(file_names):
            path = root_path / file_name
            if path.suffix.lower() in SOURCE_EXTENSIONS:
                files.append(path)
    return files


def make_excerpt(line: str, limit: int = 140) -> str:
    excerpt = " ".join(line.strip().split())
    if len(excerpt) <= limit:
        return excerpt
    return excerpt[: limit - 1] + "…"


def line_findings(path: Path, display_path: str, content: str) -> list[Finding]:
    findings: list[Finding] = []
    for line_number, line in enumerate(content.splitlines(), start=1):
        for rule in LINE_RULES:
            if rule.pattern.search(line):
                findings.append(
                    Finding(
                        rule.rule,
                        rule.severity,
                        display_path,
                        line_number,
                        rule.message,
                        make_excerpt(line),
                    )
                )
    return findings


def aggregate_findings(display_path: str, content: str) -> list[Finding]:
    findings: list[Finding] = []
    purple = r"(?:purple|violet|fuchsia|indigo|#(?:7c3aed|8b5cf6|a855f7|c026d3))"
    gradient = r"(?:gradient|from-|via-|to-)"
    purple_gradient = re.search(
        rf"(?:{gradient}.{{0,500}}{purple}|{purple}.{{0,500}}{gradient})",
        content,
        re.IGNORECASE | re.DOTALL,
    )
    if purple_gradient:
        findings.append(
            Finding(
                "purple-gradient",
                "high",
                display_path,
                content.count("\n", 0, purple_gradient.start()) + 1,
                "紫系グラデーションを検出。題材やデータ上の必然性を確認してください。",
                make_excerpt(purple_gradient.group(0)),
            )
        )

    text_clip = r"(?:bg-clip-text|background-clip\s*:\s*text|-webkit-text-fill-color\s*:\s*transparent)"
    gradient_headline = re.search(
        rf"(?:{gradient}.{{0,400}}{text_clip}|{text_clip}.{{0,400}}{gradient})",
        content,
        re.IGNORECASE | re.DOTALL,
    )
    if gradient_headline:
        findings.append(
            Finding(
                "gradient-headline",
                "high",
                display_path,
                content.count("\n", 0, gradient_headline.start()) + 1,
                "グラデーション文字の可能性。見出しの意味をタイポグラフィで作れるか確認してください。",
                make_excerpt(gradient_headline.group(0)),
            )
        )

    aggregate_rules = (
        (
            "repeated-large-radius",
            "medium",
            re.compile(
                r"(?:rounded-(?:xl|2xl|3xl)|border-radius\s*:\s*(?:1[6-9]|[2-9]\d)px)",
                re.IGNORECASE,
            ),
            4,
            "大きな角丸が同一ファイルで反復されています。対象ごとの形状理由を確認してください。",
        ),
        (
            "repeated-strong-shadow",
            "medium",
            re.compile(
                r"(?:shadow-(?:lg|xl|2xl)|box-shadow\s*:[^;]*(?:1[2-9]|[2-9]\d)px)",
                re.IGNORECASE,
            ),
            4,
            "強い影が同一ファイルで反復されています。浮遊階層の意味を確認してください。",
        ),
    )

    for rule, severity, pattern, threshold, message in aggregate_rules:
        matches = list(pattern.finditer(content))
        if len(matches) >= threshold:
            line_number = content.count("\n", 0, matches[0].start()) + 1
            findings.append(
                Finding(
                    rule,
                    severity,
                    display_path,
                    line_number,
                    message,
                    f"{len(matches)} occurrences",
                )
            )

    lines = content.splitlines()
    for index, line in enumerate(lines):
        if not re.search(
            r"(?:grid-cols-3|repeat\s*\(\s*3\s*,\s*(?:minmax|1fr))",
            line,
            re.IGNORECASE,
        ):
            continue
        nearby = "\n".join(lines[index : index + 25])
        card_terms = re.findall(
            r"(?:\bcard\b|rounded-(?:lg|xl|2xl|3xl))",
            nearby,
            re.IGNORECASE,
        )
        if len(card_terms) >= 3:
            findings.append(
                Finding(
                    "three-column-card-grid",
                    "low",
                    display_path,
                    index + 1,
                    "3列カード構成を検出。内容に固有の比較軸や優先順位があるか確認してください。",
                    make_excerpt(line),
                )
            )
            break

    return findings


def scan(target: Path) -> tuple[list[Finding], int]:
    files = iter_source_files(target)
    findings: list[Finding] = []
    base = target if target.is_dir() else target.parent

    for path in files:
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = path.read_text(encoding="utf-8", errors="replace")

        try:
            display_path = path.relative_to(base).as_posix()
        except ValueError:
            display_path = path.as_posix()

        findings.extend(line_findings(path, display_path, content))
        findings.extend(aggregate_findings(display_path, content))

    findings.sort(
        key=lambda item: (
            -SEVERITY_ORDER[item.severity],
            item.path.lower(),
            item.line,
            item.rule,
        )
    )
    return findings, len(files)


def print_text(findings: list[Finding], file_count: int) -> None:
    if not findings:
        print(f"PASS: {file_count} file(s) scanned, no candidates found.")
        return

    for finding in findings:
        print(
            f"{finding.severity.upper():6} "
            f"{finding.path}:{finding.line} [{finding.rule}] {finding.message}"
        )
        if finding.excerpt:
            print(f"       {finding.excerpt}")
    print(f"\n{len(findings)} candidate(s) in {file_count} file(s). Human review required.")


def should_fail(findings: list[Finding], threshold: str) -> bool:
    if threshold == "never":
        return False
    minimum = SEVERITY_ORDER[threshold]
    return any(SEVERITY_ORDER[item.severity] >= minimum for item in findings)


def main() -> int:
    args = parse_args()
    target = args.path.resolve()
    if not target.exists():
        print(f"ERROR: path does not exist: {target}", file=sys.stderr)
        return 2

    findings, file_count = scan(target)
    if args.format == "json":
        print(
            json.dumps(
                {
                    "path": target.as_posix(),
                    "files_scanned": file_count,
                    "findings": [asdict(item) for item in findings],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print_text(findings, file_count)

    return 1 if should_fail(findings, args.fail_on) else 0


if __name__ == "__main__":
    raise SystemExit(main())
