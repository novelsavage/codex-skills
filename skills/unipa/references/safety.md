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

## Privacy

- Do not quote student ID, personal details, grades, private messages, or file contents unless the user needs them for the requested task.
- Summarize notices and assignments compactly. Avoid dumping full pages.
- Treat downloaded materials as copyrighted/private course content. Do not upload or share them elsewhere unless the user explicitly asks.
- Do not inspect or log hidden form/session fields such as `rx-token`, `rx-loginKey`, `rx-deviceKbn`, `rx-loginType`, or `javax.faces.ViewState`. When extracting page structure, filter hidden inputs out.

## Session hygiene

- Avoid browser Back.
- Avoid duplicate logged-in UNIPA tabs.
- If the portal warns about timeout, unsaved changes, lockout, maintenance, or simultaneous login, surface that warning to the user before proceeding.
- Close or dismiss file-list/detail modals before switching courses or using top navigation. Open modals can make visible buttons appear to do nothing.
- Keep the active UNIPA tab as `handoff` or `deliverable` after meaningful work.
