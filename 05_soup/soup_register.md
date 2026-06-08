# SOUP Register — COCA-prj

## soup.yaml Contents

Auto-generated from `docs/soup.yaml` in Coronary_prj. Source of truth for version and license.

<!-- DHF_SOUP_TABLE_START -->
| Name | Version | Purpose | License |
|------|---------|---------|---------|
| numpy | 2.2.6 | Array operations for image volume manipulation and mask generation | BSD-3-Clause |
| torch | 2.12.0 | Deep learning model training and inference (UNet2D, CalciumScoreRegressor) | BSD-3-Clause |
| matplotlib | 3.10.9 | Visualization for training plots and run reports | PSF |
| openpyxl | 3.1.5 | Reading Agatston score spreadsheet (scores.xlsx) for nongated dataset | MIT |
| forge-utils | 0.2.0 | Regulatory health grading and traceability infrastructure | Internal |
| pydicom | 3.0.2 | DICOM file reading for gated and nongated CT volumes | MIT |
| scikit-image | 0.25.2 | Polygon rasterization for segmentation mask generation | BSD-3-Clause |
| idna | 3.15 | Internationalized domain names; pinned >=3.15 to close CVE-2026-45409 | BSD-3-Clause |
<!-- DHF_SOUP_TABLE_END -->

## Direct SOUP

Packages directly declared in medical device code repositories.

| Package | Version | Repo(s) | Role | License | CVE Check | Last Audited |
|---------|---------|---------|------|---------|-----------|--------------|
| numpy | 2.2.6 | medical_image_ai_toolkit, Coronary_prj | Runtime — array ops for image volumes | BSD-3-Clause | pip-audit | 2026-05-05 |
| torch | 2.12.0 | medical_image_ai_toolkit, Coronary_prj | Runtime — ML training and inference | BSD-3-Clause | pip-audit | 2026-06-08 |
| matplotlib | 3.10.9 | medical_image_ai_toolkit, Coronary_prj | Runtime — visualization and PDF reports | PSF | pip-audit | 2026-06-08 |
| openpyxl | 3.1.5 | Coronary_prj | Runtime — Agatston score spreadsheet (scores.xlsx) | MIT | pip-audit | 2026-05-05 |
| pydicom | 3.0.2 | Coronary_prj | Runtime — DICOM file reading for CT volumes | MIT | pip-audit | 2026-05-05 |
| scikit-image | 0.25.2 | Coronary_prj | Runtime — polygon rasterization for segmentation masks | BSD-3-Clause | pip-audit | 2026-05-05 |
| pyyaml | 6.0.3 | regulatory_tools | Runtime — YAML parsing for requirements and config | MIT | pip-audit | 2026-05-05 |
| forge-utils | 0.1.0 | regulatory_tools, medical_image_ai_toolkit, Coronary_prj | Runtime — health grading and traceability infrastructure | Internal | manual review | 2026-05-05 |

## Transitive SOUP

Packages introduced indirectly. Audited automatically by pip-audit in each consumer repo's CI.

| Package | Version | Via | Role | License | CVE Status |
|---------|---------|-----|------|---------|------------|
| pydantic | 2.12.5 | forge-utils | Data validation for forge config objects | MIT | Clean |
| typer | 0.25.1 | forge-utils | CLI argument parsing for forge | MIT | Clean |
| rich | 15.0.0 | forge-utils | Terminal output formatting | MIT | Clean |
| toml | 0.10.2 | forge-utils | Parsing forge.toml configuration files | MIT | Clean |
| idna | ≥3.15 | requests (transitive) | Internationalized domain names — network I/O | BSD-3-Clause | Pinned ≥3.15 (CVE-2026-45409 fixed in 3.15) |

## CVE Resolution — torch 2.9.1 → 2.12.0

The 11 CVEs previously documented against torch 2.9.1 (residual risk accepted 2026-05-20) are
all resolved in torch 2.12.0. pip-audit against `torch==2.12.0` reports no known vulnerabilities
as of 2026-06-08. The residual risk acceptance is closed; no outstanding torch CVEs remain.

| CVE | PYSEC | Resolution |
|-----|-------|------------|
| CVE-2025-63396 | PYSEC-2025-210 | Fixed in torch 2.12.0 |
| CVE-2025-3121 | PYSEC-2025-196 | Fixed in torch 2.12.0 |
| CVE-2025-3000 | PYSEC-2025-194 | Fixed in torch 2.12.0 |
| CVE-2025-3001 | PYSEC-2025-195 | Fixed in torch 2.12.0 |
| CVE-2025-2999 | PYSEC-2025-193 | Fixed in torch 2.12.0 |
| CVE-2025-2998 | PYSEC-2025-192 | Fixed in torch 2.12.0 |
| CVE-2026-4538 | PYSEC-2026-139 | Fixed in torch 2.12.0 |
| CVE-2025-2953 | PYSEC-2025-191 | Fixed in torch 2.12.0 |
| CVE-2025-3136 | PYSEC-2025-197 | Fixed in torch 2.12.0 |
| CVE-2025-2148 | PYSEC-2025-189 | Fixed in torch 2.12.0 |
| CVE-2025-2149 | PYSEC-2025-190 | Fixed in torch 2.12.0 |

**Closed:** 2026-06-08 | **Reviewed by:** Renee Qian | **Trigger:** upgrade to torch 2.12.0 via Dependabot

## Notes

- All versions are pinned in both `pyproject.toml` and `docs/soup.yaml` in each code repo.
- CVE scanning runs on every push and weekly via pip-audit in CI.
- CycloneDX SBOM artifacts are generated per CI run (see `.github/workflows/pip-audit.yml`).
- Dependabot is configured for weekly vulnerability alerts in all code repos.
- Internal package `forge-utils` is reviewed manually at each release; no public CVE database.
