# Model Performance Monitoring Plan — <!-- DHF_VAR:PROJECT_NAME -->COCA-prj<!-- /DHF_VAR:PROJECT_NAME -->

Per FDA AI/ML SaMD Guidance (2021) §VI. Describes how post-market model performance
is tracked, how drift is detected, and when retraining or re-submission is triggered.

## 1. Monitored Metrics

| Metric | Task | Description | Baseline Value | Alert Threshold | Critical Threshold |
|---|---|---|---|---|---|
| Dice score | Gated segmentation | Overlap between predicted mask and ground truth on a sample of new cases | ≥ 0.50 at deployment (MOD-005) | Dice < 0.55 on rolling 30-case sample | Dice < 0.50 on any 10-case batch |
| MAE (Agatston units) | Nongated regression | Mean absolute error between predicted and ground-truth per-vessel Agatston scores | ≤ 100.0 AU at deployment (MOD-006) | MAE > 80 AU on rolling 30-case sample | MAE > 100.0 AU on any 10-case batch |
| Input distribution drift | Both | Statistical distance between incoming DICOM HU distributions and training distribution | — | p < 0.05 (KS test on windowed HU mean) | p < 0.01 |
| False negative rate (calcium missed) | Gated segmentation | Rate at which the model produces an empty mask when calcium is present | Estimated from test set | > 10% increase from baseline | > 25% increase from baseline |

**Alert threshold:** triggers internal review within 5 business days.
**Critical threshold:** triggers immediate suspension of deployment pending root-cause analysis.

## 2. Data Collection for Monitoring

| Source | Data Collected | Frequency | Retention |
|---|---|---|---|
| Production inference logs | Input file hash, output mask/score value, timestamp, software artifact SHA-256 | Every inference | 7 years (per applicable regulatory records requirements) |
| User feedback / corrections | Radiologist overrides or flags of AI output; cases escalated for review | Continuous | 7 years |
| PACS audit logs | Patient ID (anonymized), study date, inference event | Continuous | Per institutional PACS retention policy |

Inference logs must include: software artifact SHA-256, anonymized input identifier, timestamp, output value.
See `10_software_development_plan/sdp.md` §8 (Problem Resolution) for the audit logging requirement.

## 3. Monitoring Schedule

| Activity | Frequency | Responsible |
|---|---|---|
| Automated metric review (if inference volume sufficient) | Weekly | Renee Qian (Software Developer) |
| Formal performance report | Quarterly | Renee Qian |
| Full distribution drift analysis | Every 6 months | Renee Qian |
| Post-incident review | Within 5 days of any alert threshold breach | Renee Qian |

Note: At current scale (pre-market / research deployment), monitoring is performed manually by the responsible developer. A formal monitoring dashboard will be required before broad clinical deployment.

## 4. Retraining Triggers

Retraining is initiated when **any** of the following occur:

1. A monitored metric crosses the Alert threshold for two consecutive review periods.
2. A monitored metric crosses the Critical threshold at any point.
3. Input distribution drift is confirmed by statistical test.
4. A new patient subgroup or acquisition protocol is added to the intended use.
5. A systematic labeling error is discovered in the original training data.

All retraining events must be documented in `09_change_control/change_log.md` and
evaluated against the Predetermined Change Control Plan before deployment.

## 5. Re-Submission Triggers

A new 510(k) or supplement is required when retraining results in:
- Performance outside the pre-specified bounds in `13_ai_ml/predetermined_change_control_plan.md` §4
- A change to the intended use or patient population
- A change to a locked architectural component beyond the scope of the PCCP

## 6. Responsible Persons

| Activity | Responsible | Escalation |
|---|---|---|
| Day-to-day monitoring | Renee Qian (Software Developer) | N/A (solo development team) |
| Alert response | Renee Qian | Regulatory counsel if safety-impacting |
| Retraining decision | Renee Qian | Regulatory counsel if new submission may be required |
| Re-submission decision | Renee Qian | Regulatory counsel (required) |
