# SOUP Risk Analysis — COCA-prj

## Analysis per IEC 62304 §8.1.2

| Package | Potential Failure Mode | Severity | Mitigation |
|---------|----------------------|----------|-----------|
| numpy | Incorrect array operations on image volumes (wrong dtype, broadcasting error) | Serious | Pinned version; test suite exercises array ops on known inputs |
| torch | Model inference returns wrong shape or NaN outputs | Serious | RSK-001 (NaN detection), RSK-002 (model manifest), tests cover inference paths |
| matplotlib | Report generation failure (PDF output corrupted or empty) | Minor | Advisory output only; failure does not affect clinical output |
| openpyxl | xlsx parse failure — scores read as wrong vessel or patient ID | Serious | DatasetStructureError boundary in ingestor; CI tests verify score loading |
| pydicom | DICOM read failure — corrupt pixel data, wrong slice order | Serious | RSK-003 (DatasetStructureError boundary); input validation in ingestor |
| scikit-image | Polygon rasterization error — mask region incorrect | Serious | Output is advisory only (SYS-007); test_risk_controls.py covers Dice threshold gate |
| pyyaml | YAML parse failure in requirements.yaml or soup.yaml | Minor | Affects regulatory_tools tooling, not clinical pipeline; CI validates YAML schema |
| forge-utils | Health grade miscalculated — CI gate passes below Grade B | Minor | Manual review at each forge release; not part of clinical inference path |
| pydantic (transitive) | Data validation silently coerces types in forge config objects | Negligible | Affects dev tooling only; not in clinical inference path |
| typer (transitive) | CLI argument parsing error in forge commands | Negligible | Affects dev tooling only; not in clinical inference path |
| rich (transitive) | Terminal output corruption | Negligible | Display only; no effect on inference or regulatory artifacts |
| toml (transitive) | forge.toml parse failure — forge health grade unavailable | Negligible | CI degrades gracefully; not in clinical inference path |

## General Mitigations Applied

- All SOUP dependencies are pinned to exact versions in `pyproject.toml` and `docs/soup.yaml`.
- Automated CVE scanning via `pip-audit` runs on every push and weekly schedule.
- CycloneDX SBOM generated per CI run and stored as build artifact.
- Dependabot configured for automated vulnerability alerts in all consumer repos.
- Advisory-only architecture (SYS-007) ensures clinical impact of SOUP failures is limited to
  incorrect recommendations, not autonomous treatment decisions.
