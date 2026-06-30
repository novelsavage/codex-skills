"""Count Japanese ES text with several common web-form conventions."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


MODES = (
    "codepoints",
    "utf16",
    "no-newlines",
    "no-whitespace",
)


def count_utf16_units(text: str) -> int:
    return len(text.encode("utf-16-le")) // 2


def count_text(text: str) -> dict[str, int]:
    without_newlines = text.replace("\r", "").replace("\n", "")
    return {
        "codepoints": len(text),
        "utf16": count_utf16_units(text),
        "no-newlines": len(without_newlines),
        "no-whitespace": sum(not char.isspace() for char in text),
    }


def read_text(args: argparse.Namespace) -> str:
    if args.text is not None:
        return args.text
    if args.file is not None:
        return args.file.read_text(encoding="utf-8")
    return sys.stdin.read()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Count characters in Japanese entry-sheet text."
    )
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--text", help="Text to count. Reads stdin when omitted.")
    source.add_argument("--file", type=Path, help="UTF-8 text file to count.")
    parser.add_argument("--mode", choices=MODES, default="codepoints")
    parser.add_argument("--limit", type=int, help="Optional character limit.")
    parser.add_argument("--json", action="store_true", help="Emit JSON output.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.limit is not None and args.limit < 0:
        raise SystemExit("--limit must be zero or greater")

    counts = count_text(read_text(args))
    selected = counts[args.mode]
    result: dict[str, object] = {
        "counts": counts,
        "selected_mode": args.mode,
        "selected_count": selected,
    }

    if args.limit is not None:
        result.update(
            {
                "limit": args.limit,
                "remaining": args.limit - selected,
                "within_limit": selected <= args.limit,
            }
        )

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        for mode in MODES:
            print(f"{mode}: {counts[mode]}")
        if args.limit is not None:
            print(f"limit: {args.limit}")
            print(f"remaining: {args.limit - selected}")
            print(f"within-limit: {str(selected <= args.limit).lower()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
