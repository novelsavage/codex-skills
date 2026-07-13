# UNIPA workflows

## Open and orient

1. Claim an existing UNIPA tab when available; otherwise open the user's UNIPA bookmark or known portal URL.
2. If on the login page, use saved autofill when present and submit only if the user asked for login.
3. Confirm login by checking that password fields disappear and portal menus appear.
4. Identify the current context from visible menu labels, selected tabs, page title, and URL. UNIPA pages can remain titled "麗澤ポータル" even after navigation, so do not rely on title alone.
5. If the URL and body disagree, trust visible body context over URL. Example: a page can show portal-top content while the URL remains under a class-profile path.
6. Prefer the visible heading and bracketed screen code over URL paths. Observed examples include `学生時間割表[Kmd008]`, `課題提出[Jga005]`, `授業資料[Jga023]`, and `シラバス照会[Kmh006]`.
7. Use the footer `サイトマップ` for a safe feature inventory. Use the header logo to return to portal top; the logo may lack an accessible name, so use a current screenshot/vision fallback when it is absent from the interactable DOM.

Common top-level areas include:

- おしらせ
- 時間割
- シラバス
- 履修登録&抽選申請
- 学生カルテ
- アンケート
- 申請&予約
- クラスプロファイル

## Download class materials

1. Start from today's schedule, a named class, or the requested class profile.
2. Open the relevant `クラスプロファイル` or class page from the schedule/list.
3. For class-profile pages, read [class-profile.md](class-profile.md) and prefer the central `授業資料 Class material` card or the list link over brittle top buttons.
4. On `授業資料一覧`, rows usually have titles like `第9回 授業資料`; open the row title to reach the detail page.
5. On the detail page, click `添付資料を確認` to reveal `ファイル一覧`; this reveals filenames without necessarily downloading them.
6. Use the browser download event when clicking the actual file button/link if the user asked to download.
7. After download, report file name, source class/page, and download location.
8. If multiple similarly named materials exist, ask the user which one before downloading all.

## Check assignments

1. Navigate through the class schedule, `クラスプロファイル`, or assignment/task area.
2. Look for Japanese labels such as `課題`, `レポート`, `提出`, `期限`, `登録`, `未提出`, `提出済`.
3. Capture only task-relevant facts:
   - class name;
   - assignment title;
   - due date/time;
   - submission state;
   - required file format or instructions;
   - visible attachments.
4. If instructions are long, summarize and offer to extract exact requirements.
5. On assignment detail pages, `添付資料を確認` can reveal `ファイル一覧`; use it to identify required templates without pressing `確定` or `一時保存`.

## Submit an assignment

1. Read `safety.md` before starting.
2. Verify the class name and assignment title from the visible page.
3. Verify the file path exists locally if uploading a file.
4. Attach the file using the visible upload control.
5. Stop before the final `提出`, `登録`, `確定`, `送信`, or equivalent button.
6. Ask the user to confirm the exact final action, class/task, and file name.
7. After confirmation, submit and verify the success state from a confirmation message, status text, or `提出済` indicator.

## Notices and schedules

- For notices, inspect the list first. It supports category grouping and filters such as `既読`, `未読`, `新着`, `重要`, `申込`, and `フラグつき`, plus explicit mark-read controls. Open a detail only when the requested notice requires it.
- For schedules, use the date controls inside UNIPA instead of the browser Back button. Report day, period, class name, instructor, room, and visible links such as class profile or syllabus.
- `学生時間割表` also contains PDF/Excel output, progress-forecast, GPA, and credit-status areas. Treat only the timetable panel as schedule context unless the user asks for the other data.

## Broad portal audit

1. Read [browser-operations.md](browser-operations.md) and [safety.md](safety.md).
2. Open the footer `サイトマップ`; inventory top-level menus and current counts before opening details.
3. Traverse only the safely readable areas requested or needed to understand the site map.
4. For course-related areas, sample one active course end to end, then compare list-level structure across other courses without opening every repeated record.
5. Record the route and authoritative state signal for each area; do not rely on URL alone.
6. Report coverage in four groups: inspected, skipped because reading may have side effects, blocked, and uncertain.

Do not interpret "徹底的" as permission to mark notices read, reveal grades, download every file, answer forms, or mutate portal state.

## Failure recovery

- If the page turns blank after login or navigation, wait briefly and check for visible menu text before retrying.
- If a click appears to do nothing, take a fresh DOM snapshot/screenshot and verify whether a modal, hidden frame, or scroll position changed.
- If top class-profile buttons do nothing, close visible modals and use the central card links or left course list instead.
- If a server communication error dialog appears but the requested content is visible, record the warning and continue read-only; do not repeatedly click the same control.
- If the session expires and the user has already asked for a UNIPA task, clicking the visible `ログイン` button and then `学生・教職員はこちらからログイン` may restore the SSO session without inspecting credentials. Stop if an ID/password, MFA, or approval prompt requires user input.
- If UNIPA warns about multiple sessions, stop and ask the user which tab/session to keep.
- If Chrome reports that the only UNIPA tab belongs to another browser session, do not create a duplicate. Ask the user to release or reopen one clean tab, then continue from a fresh snapshot.
- If the DOM snapshot is dominated by select options or unexpectedly includes unrelated personal data, stop broad extraction and switch to a viewport screenshot plus a scoped locator/evaluate read.
