# UNIPA safety rules

## Login

- Use the user's Chrome profile through `chrome:control-chrome`.
- If ID/password fields are already filled, do not inspect the password value. Submit only when the user asked to log in to that UNIPA site.
- If credentials are not filled, ask the user to log in or provide the next step. Do not search browser storage, cookies, localStorage, profile files, or saved passwords.
- If CAPTCHA, MFA, or an external identity-provider approval appears, ask the user to complete or explicitly authorize that step.

## State-changing actions

Confirm immediately before:

- submitting an assignment/report;
- uploading a file;
- replacing, deleting, or withdrawing a submission;
- answering/submitting a quiz, survey, questionnaire, application, or reservation;
- changing registration, favorites, settings, or profile information;
- logging out if it might interrupt the user's work.

Confirmation must name the site/account context, class/task if visible, file name if any, and the exact button/action.

## Read actions with possible side effects

- Opening a notice, message, questionnaire, attendance item, grade detail, or acknowledgment page can change `未読` to `既読` or record access.
- Before opening such an item during a broad audit, inspect the surrounding UI for unread/read markers and confirmation text.
- If the user's request clearly requires reading that exact item, opening it is within scope. Otherwise inventory its title, date, sender, and state from the list and report that the detail was skipped.
- Do not click `確認`, `了解`, `回答`, `受講`, or similar acknowledgment controls as part of read-only browsing.
- The bulletin list has per-item `既読にする` and group-level `すべて既読にする` controls. Never use them during an audit.
- The class-material list has a `未確認` column. Treat an unread material detail as possibly read-tracked; inspect the list first and open the detail only when requested or already confirmed.

## Privacy

- Do not quote student ID, personal details, grades, private messages, or file contents unless the user needs them for the requested task.
- Summarize notices and assignments compactly. Avoid dumping full pages.
- Treat downloaded materials as copyrighted/private course content. Do not upload or share them elsewhere unless the user explicitly asks.
- Do not inspect or log hidden form/session fields such as `rx-token`, `rx-loginKey`, `rx-deviceKbn`, `rx-loginType`, or `javax.faces.ViewState`. When extracting page structure, filter hidden inputs out.
- Do not broadly extract a timetable, assignment grid, student record, grade page, or application page. These can expose off-screen grades, credits, submitter names, submission timestamps, scores, health data, or application content. Read only the requested panel and fields.

## Session hygiene

- Avoid browser Back.
- Avoid duplicate logged-in UNIPA tabs.
- If the portal warns about timeout, unsaved changes, lockout, maintenance, or simultaneous login, surface that warning to the user before proceeding.
- Close or dismiss file-list/detail modals before switching courses or using top navigation. Open modals can make visible buttons appear to do nothing.
- Keep the active UNIPA tab as `handoff` or `deliverable` after meaningful work.
- Finalize the Chrome tab session as the last browser action. Leaving a claimed tab unfinalized can block a later Codex task from safely reusing it.
