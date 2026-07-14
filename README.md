# novelsavage Codex Skills

novelsavage が作成・検証している、Codex 用のスキル集です。

日本固有の就職活動、対話型の技術学習、大学ポータル操作など、汎用モデルだけでは扱いにくいワークフローを中心に整備しています。

## スキル

| スキル | 説明 | 状態 |
|---|---|---|
| [`es-writer`](skills/es-writer) | 日本の新卒採用向けESを、企業調査と応募者本人の確認可能な事実に基づいて作成・診断・推敲するスキル | experimental |
| [`kindergarten`](skills/kindergarten) | AIが作業を代行せず、技術を一歩ずつ手を動かして学ぶための対話スキル | experimental |
| [`unipa`](skills/unipa) | 麗澤大学の UNIPA / Universal Passport RX を Chrome 経由で安全に扱うためのスキル | experimental |
| [`wiki`](skills/wiki) | 個人LLM Wikiを長期記憶として参照し、恒久的な知見を安全に維持するスキル | experimental |

## インストール

使いたいスキルフォルダを、Codex のスキルディレクトリへコピーします。

Windows の例：

```powershell
Copy-Item -Recurse .\skills\es-writer $env:USERPROFILE\.codex\skills\es-writer
```

Ubuntu の例：

```bash
cp -a skills/wiki ~/.codex/skills/
```

その後、Codex で次のように呼び出せます。

```text
$es-writer 志望動機を添削して
$wiki Wikiを整理して
```

### `wiki`の前提

`wiki`は、次のファイルを含む個人LLM Wikiが`~/Projects/llm-wiki`に用意されている環境向けです。

- `~/Projects/llm-wiki/AGENTS.md`
- `~/Projects/llm-wiki/wiki/index.md`

Wiki本体と個人情報はこのリポジトリに含まれません。スキルはWikiを読み取り、条件を満たす恒久的な知見を自動更新することがあります。運用規約と保存対象を確認してから使用してください。

## 注意

- このリポジトリは非公式です。
- 各サービス・大学・組織の利用規約に従ってください。
- ログイン情報、個人情報、課題本文、授業資料などを Issue や Pull Request に貼らないでください。
- スキルは、ブラウザ上の認証済みセッションを操作する可能性があります。
- 外部サービスでの最終送信、提出、確定保存などの操作は、必ずユーザー確認を挟む設計にしています。

## 検証

スキル形式の検証には、Codex 付属の `quick_validate.py` 相当の検証スクリプトを使います。

例：

```powershell
$env:PYTHONUTF8='1'
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" ".\skills\unipa"
```

## ライセンス

MIT License
