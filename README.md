# novelsavage Codex Skills

novelsavage が作成・検証している、Codex 用のスキル集です。

日本固有の就職活動、対話型の技術学習、大学ポータル操作など、汎用モデルだけでは扱いにくいワークフローを中心に整備しています。

## スキル

| スキル | 説明 |
|---|---|
| [`es-writer`](skills/es-writer) | 日本の新卒採用向けESを、企業調査と応募者本人の確認可能な事実に基づいて作成・診断・推敲するスキル |
| [`kindergarten`](skills/kindergarten) | AIが作業を代行せず、技術を一歩ずつ手を動かして学ぶための対話スキル |
| [`luna`](skills/luna) | Luna Max に作業の振り分けや独立した調査・実装を委任するスキル |
| [`mori-ui`](skills/mori-ui) | 題材と操作目的から視覚言語を作り、紫グラデや汎用カードなどAI既定のUIを避けるスキル |
| [`unipa`](skills/unipa) | 麗澤大学の UNIPA / Universal Passport RX を Chrome 経由で安全に扱うためのスキル |
| [`wiki`](skills/wiki) | 個人LLM Wikiを長期記憶として参照し、恒久的な知見を安全に維持するスキル |

## インストール

Node.js 22.20 以降で [Skills CLI](https://github.com/vercel-labs/skills#install-a-skill) を使い、必要なスキルを Codex に追加します。リポジトリのクローンは不要です。

```bash
npx skills add novelsavage/codex-skills --agent codex --global --skill es-writer
```

別のスキルを入れるには `--skill` の後ろをスキル名に替えます。特定のプロジェクトだけで使う場合は、そのプロジェクトのルートで `--global` を外して実行します。

その後、Codex で次のように呼び出せます。

```text
$es-writer 志望動機を添削して
$luna 関連する3つのモジュールを並列に調べて、変更が必要な箇所をまとめて
$mori-ui この管理画面をAIっぽくないUIに作り直して
$wiki Wikiを整理して
```

### `luna` の設定

`--skill luna` でスキルを追加します。名前付きの `luna_worker` を使う場合は、スキルに含まれる [luna-worker.toml](skills/luna/agents/luna-worker.toml) を Codex のエージェントディレクトリにもコピーします。

Linux・macOS でスキルをグローバルに追加した場合の例です。

```bash
mkdir -p ~/.codex/agents
cp -i ~/.agents/skills/luna/agents/luna-worker.toml ~/.codex/agents/
```

Windows では `%USERPROFILE%\.agents\skills\luna\agents\luna-worker.toml` を `%USERPROFILE%\.codex\agents\` にコピーします。

使うモデルは `luna-worker.toml` の `model` と `model_reasoning_effort` で指定します。後継モデルへ切り替えるときは、サブエージェントとして利用できるモデルIDと対応する推論レベルを確認し、インストール先のこのファイルを更新します。呼び出し方は引き続き `$luna` です。名前付きの役割を使えない環境では、スキルが同じ設定を起動ツールに渡します。設定ファイルを入れていない場合は、実行環境で Luna Max を選べるか確認してから起動します。

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
