# novelsavage Codex Skills

novelsavage が作成・検証している Codex 用スキル集です。

現在は、日本の大学ポータルやブラウザ操作のように「APIがなく、人間向けUIをAIエージェントが慎重に扱う必要がある領域」を中心に整備しています。

## Skills

| Skill | 説明 | 状態 |
|---|---|---|
| [`unipa`](skills/unipa) | 麗澤大学のUNIPA / Universal Passport RXをChrome経由で安全に扱うためのスキル | experimental |

## インストール

使いたいスキルフォルダを、Codex のスキルディレクトリへコピーしてください。

Windows例：

```powershell
Copy-Item -Recurse .\skills\unipa $env:USERPROFILE\.codex\skills\unipa
```

その後、Codexで次のように呼び出せます。

```text
$unipa 今日の課題を確認して
```

## 注意

- このリポジトリは非公式です。
- 各サービス・大学・組織の利用規約に従ってください。
- ログイン情報、個人情報、課題本文、授業資料などをIssueやPull Requestに貼らないでください。
- スキルはブラウザ上の認証済みセッションを操作する可能性があります。最終送信・提出・保存などの操作は、必ずユーザー確認を挟む設計にしています。

## 検証

スキル形式の検証には、Codex付属の `quick_validate.py` 相当の検証スクリプトを使います。

例：

```powershell
$env:PYTHONUTF8='1'
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" ".\skills\unipa"
```

## License

MIT License
