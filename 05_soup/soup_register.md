# SOUP Register — COCA-prj

## Direct SOUP

Packages directly declared in medical device code repositories.

| Package | Version | Repo(s) | Role | License | CVE Check | Last Audited |
|---------|---------|---------|------|---------|-----------|--------------|
| numpy | 2.2.6 | medical_image_ai_toolkit, Coronary_prj | Runtime — array ops for image volumes | BSD-3-Clause | pip-audit | 2026-05-05 |
| torch | 2.9.1 | medical_image_ai_toolkit, Coronary_prj | Runtime — ML training and inference | BSD-3-Clause | pip-audit | 2026-05-20 |
| matplotlib | 3.10.8 | medical_image_ai_toolkit, Coronary_prj | Runtime — visualization and PDF reports | PSF | pip-audit | 2026-05-05 |
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

## Residual Risk — torch 2.9.1 CVEs

pip-audit reports 11 CVEs against torch 2.9.1. No fix versions are available from PyTorch as of
2026-05-20. Risk has been reviewed and accepted per the rationale below.

**Risk acceptance rationale:** This software runs as a clinical workstation tool with no exposed
network service or public API. Exploitation of all 11 CVEs requires local host access — an
attacker who already has a local session can cause greater harm via other means. The three CVEs
with any remote-attack language (CVE-2025-2148) additionally require "high attack complexity" and
are rated by the reporter as "exploitation appears to be difficult." None of the CVEs affect the
inference or DICOM-processing code paths that influence clinical output; they are confined to
profiler, JIT compiler, CUDA allocator, and RNN helper functions that are not used at inference
time in this system. The system is deployed in a controlled clinical network environment with
restricted local access. Residual risk is accepted; no upgrade path exists.

| CVE | PYSEC | Affected component | Attack vector | Severity | Fix available |
|-----|-------|--------------------|---------------|----------|---------------|
| CVE-2025-63396 | PYSEC-2025-210 | torch.profiler (PythonTracer) | Local | Medium | None |
| CVE-2025-3121 | PYSEC-2025-196 | torch.jit.jit_module_from_flatbuffer | Local | Medium | None |
| CVE-2025-3000 | PYSEC-2025-194 | torch.jit.script | Local | Critical | None |
| CVE-2025-3001 | PYSEC-2025-195 | torch.lstm_cell | Local | Critical | None |
| CVE-2025-2999 | PYSEC-2025-193 | torch.nn.utils.rnn.unpack_sequence | Local | Critical | None |
| CVE-2025-2998 | PYSEC-2025-192 | torch.nn.utils.rnn.pad_packed_sequence | Local | Critical | None |
| CVE-2026-4538 | PYSEC-2026-139 | pt2 Loading Handler (deserialization) | Local | Medium | None |
| CVE-2025-2953 | PYSEC-2025-191 | torch.mkldnn_max_pool2d | Local | Low | None |
| CVE-2025-3136 | PYSEC-2025-197 | CUDACachingAllocator | Local | Medium | None |
| CVE-2025-2148 | PYSEC-2025-189 | Tuple Handler (jit_fut callbacks) | Network (high complexity) | Critical | None |
| CVE-2025-2149 | PYSEC-2025-190 | nnq_Sigmoid (quantized module) | Local | Low | None |

**Review date:** 2026-05-20 | **Reviewed by:** Renee Qian | **Next review:** 2026-11-20 or on next PyTorch release

## Notes

- All versions are pinned in both `pyproject.toml` and `docs/soup.yaml` in each code repo.
- CVE scanning runs on every push and weekly via pip-audit in CI.
- CycloneDX SBOM artifacts are generated per CI run (see `.github/workflows/pip-audit.yml`).
- Dependabot is configured for weekly vulnerability alerts in all code repos.
- Internal package `forge-utils` is reviewed manually at each release; no public CVE database.
