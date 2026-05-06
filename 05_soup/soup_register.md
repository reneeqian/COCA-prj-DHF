# SOUP Register — COCA-prj

## Direct SOUP

Packages directly declared in medical device code repositories.

| Package | Version | Repo(s) | Role | License | CVE Check | Last Audited |
|---------|---------|---------|------|---------|-----------|--------------|
| numpy | 2.2.6 | medical_image_ai_toolkit, Coronary_prj | Runtime — array ops for image volumes | BSD-3-Clause | pip-audit | 2026-05-05 |
| torch | 2.9.1 | medical_image_ai_toolkit, Coronary_prj | Runtime — ML training and inference | BSD-3-Clause | pip-audit | 2026-05-05 |
| matplotlib | 3.10.8 | medical_image_ai_toolkit, Coronary_prj | Runtime — visualization and PDF reports | PSF | pip-audit | 2026-05-05 |
| openpyxl | 3.1.5 | Coronary_prj | Runtime — Agatston score spreadsheet (scores.xlsx) | MIT | pip-audit | 2026-05-05 |
| pydicom | 3.0.2 | Coronary_prj | Runtime — DICOM file reading for CT volumes | MIT | pip-audit | 2026-05-05 |
| scikit-image | 0.25.2 | Coronary_prj | Runtime — polygon rasterization for segmentation masks | BSD-3-Clause | pip-audit | 2026-05-05 |
| pyyaml | 6.0.3 | regulatory_tools | Runtime — YAML parsing for requirements and config | MIT | pip-audit | 2026-05-05 |
| forge-utils | 0.1.0 | regulatory_tools, medical_image_ai_toolkit, Coronary_prj | Runtime — health grading and traceability infrastructure | Internal | manual review | 2026-05-05 |

## Transitive SOUP

Packages introduced indirectly via forge-utils. These are forge's runtime dependencies
and are audited automatically by pip-audit in each consumer repo's CI.

| Package | Version | Via | Role | License |
|---------|---------|-----|------|---------|
| pydantic | 2.12.5 | forge-utils | Data validation for forge config objects | MIT |
| typer | 0.25.1 | forge-utils | CLI argument parsing for forge | MIT |
| rich | 15.0.0 | forge-utils | Terminal output formatting | MIT |
| toml | 0.10.2 | forge-utils | Parsing forge.toml configuration files | MIT |

## Notes

- All versions are pinned in both `pyproject.toml` and `docs/soup.yaml` in each code repo.
- CVE scanning runs on every push and weekly via pip-audit in CI.
- CycloneDX SBOM artifacts are generated per CI run (see `.github/workflows/pip-audit.yml`).
- Dependabot is configured for weekly vulnerability alerts in all code repos.
- Internal package `forge-utils` is reviewed manually at each release; no public CVE database.
