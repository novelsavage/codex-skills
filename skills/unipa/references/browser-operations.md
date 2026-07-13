# UNIPA browser operations

Use this reference for broad audits, unfamiliar pages, and browser recovery.

## Interaction loop

For every click, fill, selection, or key press:

1. Observe the current page with one fresh DOM snapshot. Use a screenshot instead only when visual layering, icons, or a modal cannot be understood from the DOM.
2. Record the state tuple: visible page heading and screen code, active course, selected section/tab, open modal, and URL hint.
3. Build a locator only from the current snapshot. Prefer a stable attribute, then a scoped role and accessible name, then scoped visible text.
4. Confirm the locator resolves to one visible element. Do not use positional shortcuts for repeated labels.
5. Perform one action.
6. Verify the cheapest authoritative signal: changed heading, selected tab, visible modal title, status badge, file name, confirmation message, or URL change.
7. Refresh the snapshot before the next locator if the DOM changed or the action failed.

Do not retry a timed-out or ambiguous locator unchanged. Re-observe, close overlays, narrow the container, or switch to a stable attribute copied from the new snapshot.

## Read-only audit

When the user requests a broad scan:

1. Start with the footer `サイトマップ` and inventory visible top-level areas without opening every item. Read [portal-map.md](portal-map.md).
2. Classify each candidate action:
   - safe read: schedule views, class lists, material and assignment lists, syllabus details;
   - possibly tracked: notice details, messages, questionnaires, attendance or grade details;
   - state-changing: downloads when permission-gated, copy-to-WebNote, favorites, uploads, saves, submissions, registrations, reservations, answers, and logout.
3. Traverse safe-read areas in a stable order: portal top, notices summary, schedule, class profile, assignments, materials, syllabus, then other requested areas.
4. Before entering a possibly tracked area, inspect the visible label and surrounding UI for `未読`, `既読`, acknowledgment, or confirmation behavior. Skip it unless the request authorizes that effect.
5. For each inspected area, capture only its heading, screen code, relevant counts/statuses, dates, and the navigation path that reached it.
6. Stop expanding when a section repeats the same structure across many courses. Sample enough to learn the pattern, then report the remaining scope instead of opening every record.
7. End with a coverage summary: inspected, skipped for safety, blocked by authentication/session/UI, and still uncertain.

This is an audit of visible user-facing behavior, not a crawl of hidden endpoints. Do not guess URLs, enumerate generated IDs, inspect storage, or collect hidden form/session values.

## UNIPA-specific locator strategy

- Scope repeated labels to the active course panel, table row, card, dialog, or selected tab.
- Treat `j_idt...` and similar JSF IDs as snapshot-local. Reuse them only until the next navigation or partial-page update.
- Prefer visible Japanese labels and stable `href` values copied from the current snapshot. Do not derive neighboring URLs from an observed path.
- Treat URL paths as hints only; AJAX navigation can leave the URL and visible body out of sync.
- Prefer the visible heading plus bracketed screen code, such as `学生時間割表[Kmd008]`, `課題提出[Jga005]`, or `授業資料[Jga023]`, over the address bar. A URL can remain from the previous screen even after a full feature change.
- When a dialog is open, scope `閉じる` to that dialog. Some close controls have no accessible text and require a current-snapshot class or node ID.

## Observation boundaries

- On `学生時間割表`, do not take a full-page DOM snapshot unless the user requested academic-progress data. The page can include off-screen GPA and credit-status tables below the timetable.
- On assignment lists, scope extraction to the requested row and required columns. The grid may include submitter names, submission timestamps, scores, feedback, and other-submitters fields.
- On syllabus search, avoid dumping every `<option>` from the organization and curriculum selectors. Use a viewport screenshot or inspect only selected values and visible field labels.
- When a DOM snapshot returns only repeated `<option>` nodes or otherwise loses page structure, switch to a viewport screenshot, then use a targeted DOM read for the identified panel.

## Recovery and tab lifecycle

- If a click does nothing, check for `ファイル一覧`, a warning dialog, a disabled control, a stale snapshot, or a partial AJAX update before retrying.
- If DOM inspection times out once, use the browser troubleshooting guidance, verify whether the page is visually responsive, and retry once with a targeted observation. Do not loop.
- If the existing UNIPA tab is owned by another Codex browser session, do not open a duplicate logged-in tab. Ask the user to finish/release the previous task or reopen one clean UNIPA tab.
- At the end, call Chrome tab finalization exactly once as the last browser action. Keep an unfinished/login/confirmation page as `handoff`; otherwise release the claimed tab.
