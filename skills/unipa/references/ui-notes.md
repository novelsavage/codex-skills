# UNIPA UI notes

UNIPA / Universal Passport RX is fragile and often hostile to automation. Prefer visible page state over assumptions.

## Locator strategy

- Prefer stable visible Japanese labels and form/button IDs copied from the current DOM snapshot.
- Many pages use tables, old JSF/PrimeFaces-style IDs, and repeated labels. Confirm locator uniqueness before clicking.
- Treat generated `j_idt...` IDs as volatile. They can change between class-profile subpages; copy them from the current page only.
- Page title may stay generic, so combine title, URL, selected menu, and visible text.
- Treat the visible page heading plus bracketed screen code as the strongest page identity. URL paths can lag by one or more feature transitions.
- Menus can hide subitems until hover/click. Use screenshots when DOM text is confusing.
- Filter hidden inputs out of diagnostic extracts; hidden session fields are not task context.
- Use the current snapshot as locator ground truth. Confirm a target is unique before interaction, and refresh the snapshot after any navigation, AJAX replacement, timeout, or ambiguity.
- Prefer one scoped DOM extraction over repeated per-element reads when inventorying a small, already identified table or panel.
- If a snapshot contains only select options, or exposes unrelated off-screen personal panels, use a viewport screenshot and then inspect only the identified panel.

## Navigation cautions

- Do not use browser Back as a default recovery strategy.
- Avoid opening the same portal in multiple tabs after login.
- Expect daily maintenance windows and timeout warnings.
- Some buttons have generic text (`登録`, `OK`, `戻る`, `閉じる`); scope to the current class/task panel before clicking.
- URL paths are only hints. Observed pages kept stale paths across site map, student timetable, assignment, material, and syllabus screens. Never label a route solely from its path.
- When `ファイル一覧` or another modal is open, course switching and top navigation can silently fail. Close the modal before continuing.
- A previous Codex task can leave a claimed Chrome tab unavailable if it ends without tab finalization. Do not work around this by opening another logged-in UNIPA tab.
- The header logo returns to portal top but may have no accessible name and may be absent from the interactable DOM snapshot. Use a fresh screenshot and visual click fallback rather than guessing a CSS chain.

## Japanese labels to recognize

- Login: `LOGIN`, `学生・教職員はこちらからログイン`
- Notices: `おしらせ`, `掲示`, `重要`, `期限あり`, `もっと見る`
- Schedule: `時間割`, `日表示`, `月表示`, `前週`, `前日`, `今日`, `翌日`, `翌週`
- Course pages: `クラスプロファイル`, `シラバス照会`, `履修授業`
- Class profile: `TOP`, `課題提出`, `テスト`, `クリッカー`, `授業Ｑ＆Ａ登録`, `ＷｅｂＮｏｔｅ`, `プロジェクト`, `コース学習`, `学習状況`, `授業資料`
- Assignments: `課題`, `レポート`, `提出`, `登録`, `期限`, `未提出`, `提出済`, `添付`, `添付資料を確認`, `ファイル一覧`
- Materials: `授業資料一覧`, `授業資料`, `資料内容`, `授業資料公開期間`, `WebNoteへコピー`
- Final actions: `提出`, `登録`, `確定`, `送信`, `完了`

## Submission buttons

Treat `提出`, `登録`, `確定`, `送信`, and final `OK` dialogs as potentially state-changing. If they complete a submission or update, confirm with the user immediately before pressing them.
