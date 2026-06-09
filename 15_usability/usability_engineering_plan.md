# Usability Engineering Plan — <!-- DHF_VAR:PROJECT_NAME -->COCA-prj<!-- /DHF_VAR:PROJECT_NAME -->

Per IEC 62366-1:2015. Defines the human factors and usability engineering activities
for <!-- DHF_VAR:PROJECT_NAME -->COCA-prj<!-- /DHF_VAR:PROJECT_NAME -->.

## 1. Intended Use Context Summary

| Element | Description |
|---|---|
| Intended users | Trained radiologists with experience in cardiac CT interpretation |
| Use environment | Clinical radiology workstation; local inference only (no network service in current form) |
| User interface | Command-line tool + JSON/PDF output reports; PACS integration is out of scope for current release |
| Frequency of use | Per-case; invoked as part of the standard CT reading workflow |
| Time pressure | Elective — standard cardiac CT reporting timeframe; not intended for emergency use |

## 2. User Tasks

Tasks were identified through developer workflow review and literature review of coronary
calcium scoring workflows (MESA / ACC guidelines; Agatston 1990).

| Task ID | Task Description | Safety-Critical? | Failure Consequence |
|---|---|---|---|
| T-001 | Load patient CT volume and run inference via CLI or script | No | Technical failure — re-run required; no patient harm |
| T-002 | Review AI output (segmentation mask or Agatston score) and decide on clinical action | Yes | Over-reliance on incorrect output → missed CAD risk → delayed or inadequate treatment (H-001, H-002) |
| T-003 | Override or dismiss AI recommendation based on independent clinical judgment | Yes | Dismissal of correct output → missed calcium detection; or uncritical acceptance of incorrect output |
| T-004 | Verify that ingestion succeeded (no DatasetStructureError) before reviewing output | No | Silent failure — if not checked, wrong output may be reviewed (H-003) |

Safety-critical tasks are those where a use error could directly cause or contribute to
patient harm. All safety-critical tasks require formative evaluation.

## 3. Known Use Errors and Hazard-Related Use Scenarios

| ID | Use Error | Probability | Harm | Mitigation |
|---|---|---|---|---|
| UE-001 | Over-reliance on AI output without independent clinical assessment | Low–Moderate | Missed CAD diagnosis or over-treatment (H-001, H-002) | Output labeled "advisory only" in all reports (SYS-007); radiologist final decision documented in intended use (IFU) |
| UE-002 | Misinterpretation of segmentation mask as a quantitative Agatston score | Low | Incorrect cardiovascular risk estimate | Output type is explicit in report format: gated output = mask, nongated output = per-vessel score |
| UE-003 | Failure to check for ingestion error before reviewing output | Moderate | Incorrect patient data processed silently (H-003) | RSK-003: `DatasetStructureError` raised on failure; CLI exits non-zero; operator must confirm clean run |
| UE-004 | Applying the tool to a contraindicated patient (prior stent, pediatric, contrast CT) | Low | Inaccurate calcium estimate in untested population | Contraindications listed in intended use; advisory-only output further mitigates harm |

## 4. Formative Evaluation

Formative studies are conducted iteratively during development to identify and address
use errors before summative testing. Current status reflects pre-market development phase.

| Study | Method | Participants | Status |
|---|---|---|---|
| Intended use review | Expert review of IFU and intended use statement by device developer | 1 (Renee Qian) | Complete (2026-05-05) |
| Output format review | Heuristic evaluation of JSON/PDF report format for clarity of advisory label | 1 (Renee Qian) | Complete (2026-05-05) |
| Simulated use session | Think-aloud with representative radiologist user | 0 | Planned — required before clinical deployment |

Findings from formative evaluation are documented as anomalies in
`11_anomaly_log/anomaly_log.md` with category "Usability."

## 5. Summative Evaluation

Summative testing is conducted on the final design to demonstrate that the intended
users can use the device safely and effectively for its intended use.

| Element | Description |
|---|---|
| Participants | ≥ 5 representative users: radiologists with cardiac CT reading experience |
| Test environment | Simulated clinical setting (research workstation with de-identified cases) |
| Scenarios tested | All safety-critical tasks in §2 (T-002, T-003, T-004); all use errors in §3 (UE-001 through UE-004) |
| Acceptance criteria | Zero critical use errors (UE-001, UE-002); ≤ 20% rate of non-critical use errors per session |
| Planned date | Before first clinical deployment — date TBD |

## 6. Training and Labeling

| Control | Description |
|---|---|
| Labeling | IFU includes: intended use statement, indications, contraindications, advisory-only statement, output interpretation guidance |
| Advisory label | All output reports include the statement: "This output is advisory only. Clinical decisions must be made by a qualified radiologist." |
| User training | Intended users are trained radiologists; no additional device-specific training is required beyond reading the IFU |
| Training verification | Users must attest to having read the IFU before first use (attestation procedure TBD for clinical deployment) |
