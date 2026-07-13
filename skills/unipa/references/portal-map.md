# UNIPA portal map

Use the footer `サイトマップ` as the safest read-only inventory of currently available features. The observed student portal exposes:

- `おしらせ`
  - `掲示板`
- `時間割`
  - `学生時間割表`
  - `授業時間割表`
  - `試験時間割表`
  - `集中講義時間割表`
  - `教員時間割表`
  - `教員スケジュール`
- `シラバス`
  - `シラバス照会`
- `履修登録&抽選申請`
  - `履修登録`
  - `抽選希望登録`
- `学生カルテ`
  - `学籍情報照会`
  - `健康診断情報照会`
  - `学籍情報変更申請`
  - `成績照会`
  - `学生出欠状況確認`
- `アンケート`
  - `アンケート回答`
  - `授業評価回答`
  - `安否確認回答`
- `申請&予約`
  - `Web申請`
  - `Web申請状況確認`
  - `教室予約`

The site map does not list `クラスプロファイル`. From the portal top, use the `クラスプロファイル` information tile. It may expose the accessible name `クラスプロファイルトップ画面を表示します。`; if that name is absent after loading, identify the visible tile from a fresh screenshot instead of guessing a selector.

## Audit classification

- Generally safe to inventory: site map, bulletin list, timetable layout, syllabus search form, class-profile top, assignment list, and material list.
- Scope before reading: assignment rows can expose submission timestamps, submitter names, scores, and feedback; the student timetable page can also preload GPA and credit-status tables below the timetable.
- Possibly read-tracked: bulletin details and material rows with `未確認` state.
- State-changing or sensitive: mark-read controls, progress forecast, PDF/Excel output, registration, lottery requests, student-record changes, surveys, class evaluations, safety confirmations, applications, reservations, downloads, uploads, deletes, saves, copies, and submissions.

Inventory the existence of sensitive areas from the site map. Open them only when the user's request requires their contents.
