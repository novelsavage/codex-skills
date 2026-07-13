# UNIPA class profile

Use this reference inside a `クラスプロファイル` / Web Learning course page.

## Observed structure

- The course page header shows a course code and course name, for example `EEI3000102ソフトウェア開発の実際 -2`.
- The top area has navigation buttons such as `TOP`, `課題提出`, `テスト`, `クリッカー`, `授業Ｑ＆Ａ登録`, `ＷｅｂＮｏｔｅ`, `プロジェクト`, `コース学習`, `学習状況`, `授業資料`, `アンケート回答`, and `授業評価回答`.
- The left pane lists enrolled courses grouped by day/period. Course links update the active class by AJAX and keep the URL mostly unchanged.
- The central `TOP` view has card links such as `課題提出 Task submission 残り1／1件` and `授業資料 Class material`.
- The portal top exposes a direct `クラスプロファイル` tile. It can have accessible name `クラスプロファイルトップ画面を表示します。`, but the name is not present in every rendered state; use a screenshot fallback when needed.
- URLs are not reliable state identifiers. Observed pages include:
  - `bs/bsa001/Bsa00101.xhtml` while either site map or class-profile-adjacent content is visible;
  - `jg/jga001/Jga00101.xhtml` while assignment content is visible;
  - `jg/jga005/Jga00502.xhtml` while material content is visible;
  - `jg/jga023/Jga02302.xhtml` while syllabus search is visible.

These are examples of stale/mismatched URL state, not route mappings. Use the visible heading and screen code instead.

## Robust navigation pattern

1. Determine the active course from the visible header, not URL alone.
2. If starting from the portal schedule, click the course row's `クラスプロファイル` button after scoping to the course block.
3. On class-profile top, prefer central card links for `課題提出` and `授業資料`. They use `syncTransition` and are more reliable than top button pairs.
4. Top button pairs are visible button + adjacent hidden submit. They may not navigate while a modal is open or while the page thinks a form is modified.
5. If switching course from the left pane, first close any open `ファイル一覧`, warning, or detail modal.
6. After every navigation, wait until the visible body contains the target label and course name.

## Assignment flow

1. Open `課題提出 Task submission ...` from the central card or use a direct assignment link from the schedule/top page.
2. On detail pages, capture:
   - `課題名`;
   - `課題公開期間`;
   - `課題提出期間`;
   - `課題内容`;
   - `課題提出方法`;
   - existing `添付ファイル`;
   - upload input status;
   - buttons such as `確定` and `一時保存`.
3. Use `添付資料を確認` to reveal `ファイル一覧` for templates or reference files.
4. Do not click `確定`, `一時保存`, `提出`, or final `OK` without action-time confirmation.
5. A submitted/ended assignment can still show `Choose File`, `削除`, `WebNoteへコピー`, and `確定`. Treat every one as state-changing even when a submission timestamp and file are already present.

## Class material flow

1. Open `授業資料 Class material`.
2. On `授業資料一覧`, rows have titles such as `第9回 授業資料`, dates, author, and `コピー`.
3. Inspect the `未確認` column before opening a row. An unread detail may be tracked.
4. Open the row title, not `コピー`, to read the material detail.
5. On detail pages, capture:
   - title;
   - `授業実施日`;
   - `授業資料公開期間`;
   - `資料内容`.
6. Click `添付資料を確認` to reveal `ファイル一覧`; this can show file names such as PDFs and ZIPs without downloading.
7. Treat `WebNoteへコピー` and row `コピー` buttons as state-changing or at least user-content-copying actions. Confirm before pressing them.

## Known failure modes

- A server communication error dialog may appear while the requested file list is still visible. Report the warning and avoid repeated clicks.
- `ファイル一覧` modals can block left-course switching and top navigation while leaving the page text readable.
- Generated `j_idt...` IDs shift between pages. Do not hard-code them across tasks.
- Repeated labels are common. Scope actions to the active course, current tab/card, or latest detail section before clicking.
- The visible file-list dialog can coexist with many hidden dialog templates. Scope to a visible dialog first, then use its `a.ui-dialog-titlebar-close` control; do not select the first global dialog.
