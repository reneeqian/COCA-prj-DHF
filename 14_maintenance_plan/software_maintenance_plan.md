# Software Maintenance Plan — <!-- DHF_VAR:PROJECT_NAME -->COCA-prj<!-- /DHF_VAR:PROJECT_NAME -->

Per IEC 62304 §6.1. Defines the processes for maintaining the software after release,
including monitoring, bug response, end-of-life, and maintenance change control.

## 1. Scope

This plan applies to all released versions of <!-- DHF_VAR:PROJECT_NAME -->COCA-prj<!-- /DHF_VAR:PROJECT_NAME --> from initial release
through end-of-life. It covers corrective, adaptive, and perfective maintenance.

| Maintenance Type | Definition | Examples |
|---|---|---|
| Corrective | Fix defects discovered post-release | Bug fixes, anomaly resolution |
| Adaptive | Accommodate changes in the operating environment | Dependency upgrades, OS compatibility |
| Perfective | Improve performance without changing functionality | Optimization, refactoring |
| Emergency | Immediate fix for safety-critical or Critical-severity anomaly | Hotfix release |

## 2. Monitoring Activities

| Activity | Frequency | Responsible | Tool / Source |
|---|---|---|---|
| CVE scan | Every push + weekly schedule | CI | pip-audit |
| Anomaly log review | Weekly | Renee Qian | `11_anomaly_log/anomaly_log.md` |
| SOUP version drift check | Every CI run | CI | `soup_checker` (regulatory_tools) |
| Model performance review | See monitoring plan | Renee Qian | `13_ai_ml/model_performance_monitoring_plan.md` |
| User feedback review | Monthly | Renee Qian | Direct feedback from clinical collaborators / test users |

## 3. Maintenance Change Process

All maintenance changes follow the change control process in
`09_change_control/change_control_procedure.md`. Additionally:

1. Log the anomaly in `11_anomaly_log/anomaly_log.md` (if corrective).
2. Assess safety impact: does the change affect any RSK-* requirement?
3. If safety impact: update `04_risk_management/` records before deployment.
4. Run `python runtests.py` — must pass at Grade ≥ B with 100% requirements coverage.
5. Record the change in `09_change_control/change_log.md`.
6. Update `07_configuration_management/baseline_register.md` at release.

## 4. Supported Versions

| Version | Support Status | Support End Date |
|---|---|---|
| 0.1.0 | Active — full support | TBD (pre-market; no end date set) |
| Older versions | End of life — no support | — |

Users on end-of-life versions are responsible for assessing continued fitness for purpose.

## 5. Emergency Maintenance

For Critical-severity anomalies with confirmed patient safety impact:

1. Immediately notify <!-- DHF_VAR:RESPONSIBLE_PERSON -->Renee Qian<!-- /DHF_VAR:RESPONSIBLE_PERSON -->.
2. Assess whether deployment must be suspended pending fix.
3. Implement hotfix on a dedicated branch; expedited review by two approvers.
4. Deploy as a patch release (X.Y.Z+1).
5. Notify affected users via direct contact (current deployment is pre-market / research; no automated notification infrastructure in place).
6. File an anomaly report and complete root-cause analysis within 30 days.

## 6. End-of-Life Policy

<!-- DHF_VAR:PROJECT_NAME -->COCA-prj<!-- /DHF_VAR:PROJECT_NAME --> end-of-life date is not yet established (device is pre-market).

Prior to end-of-life:
- Notify users at least 90 days in advance.
- Confirm all unresolved anomalies are either fixed or formally risk-accepted.
- Archive the final release artifacts and all DHF records.
- Retain records for 7 years (or the period required by applicable national regulations, whichever is longer) per IEC 62304 §4.4 and FDA 21 CFR Part 820.
