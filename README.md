# COCA-prj Design History File

Design History File (DHF) for the Coronary Artery Calcium (COCA) SaMD project.

IEC 62304 Class: **B** — serious injury possible (calcium miss), mitigated by advisory-only
output (SYS-007).

## Code Repositories

| Repository | Description |
|------------|-------------|
| [forge](https://github.com/reneeqian/forge) | forge-utils v0.1.0 — dev health grading toolkit |
| [regulatory_tools](https://github.com/reneeqian/regulatory_tools) | v1.0.0 — traceability and evidence infrastructure |
| [medical_image_ai_toolkit](https://github.com/reneeqian/medical_image_ai_toolkit) | Reusable ML building blocks |
| [Coronary_prj](https://github.com/reneeqian/Coronary_prj) | COCA-specific ingestion, tasks, and models |

## DHF Structure

```
01_device_description/    — intended use (SYS-007), software classification
02_requirements/          — requirements index and traceability links
03_architecture/          — component architecture and interfaces
04_risk_management/       — hazard analysis (RSK-001–007), risk controls
05_soup/                  — SOUP register (8 direct + transitive)
06_verification/          — verification plan and evidence index
07_configuration_management/ — baseline register with repo SHAs
08_security/              — threat model and security assessment
09_change_control/        — change control and log
```

## Regulatory References

- IEC 62304:2006+AMD1:2015
- ISO 14971:2019
- FDA AI/ML SaMD Action Plan (2021)
