# Threat Model — <!-- DHF_VAR:PROJECT_NAME -->COCA-prj<!-- /DHF_VAR:PROJECT_NAME -->

## Data Flows

```
[PACS / Local Storage]
        │  DICOM files (untrusted input boundary)
        ▼
[COCAGatedIngestor / COCANongatedIngestor]
        │  PatientSample (image_volume, spacing, annotations, metadata)
        │  Validate: required tags, pixel dimensions, slice order
        ▼
[CoronaryCalciumTask / NongatedCalciumScoreTask]
        │  Tensor slices {"input": Tensor, "target": Tensor}
        ▼
[UNet2D / CalciumScoreRegressor]  ← model.pt artifact (trust boundary)
        │  Raw logits / log1p score tensors
        ▼
[Post-processing: sigmoid + threshold / expm1 + clamp ≥ 0]
        │  Segmentation mask (H,W) or Agatston score vector (4,)
        ▼
[ModelTestingPipeline / Reporting]
        │  model_testing_report.json, PDF report, console summary
        ▼
[Radiologist workstation / PACS viewer]  ← advisory display only
```

## Trust Boundaries

| Boundary | Description |
|----------|-------------|
| DICOM ingest | DICOM files arrive from PACS or local storage; pixel data and metadata are untrusted until validated by the ingestor |
| Model artifact load | `model.pt` is loaded from disk; SHA-256 manifest check (RSK-002) must pass before use |
| Regression post-processing | Raw model output is clamped to ≥ 0 before being reported (RSK-002); no negative Agatston scores reach the output |
| Report output | JSON/PDF reports are written to local disk; no network egress in current deployment |

## Threat Table (STRIDE)

| ID | Threat Category | Asset | Threat | Mitigation |
|----|----------------|-------|--------|-----------|
| T-001 | Tampering | Model artifact | Corrupted or substituted `model.pt` used for inference | Manifest integrity check at load time: model_class, param_count, training_config stored in `manifest.json` alongside model (RSK-002) |
| T-002 | Information Disclosure | Patient DICOM data | Unauthorized access to DICOM files processed by the system | Access control is the responsibility of the deploying institution's PACS administrator; this software does not transmit patient data externally |
| T-003 | Spoofing | Patient identity | DICOM with mismatched patient metadata processed as a different patient | Ingestor reads PatientID from DICOM tags; responsibility for correct patient routing lies with the upstream PACS workflow |
| T-004 | Tampering | Input DICOM | Adversarially crafted DICOM file bypasses validation and causes incorrect output | RSK-003: ingestor raises `DatasetStructureError` on malformed DICOM; pydicom pinned to ≥ 3.0.2 (CVE-2026-32711 patched) |
| T-005 | Elevation of Privilege | Local process | Model outputs negative scores that are displayed without clamping | RSK-002: expm1 back-transform followed by `max(0, score)` clamp; enforced in post-processing code and verified in CI |
| T-006 | Denial of Service | Inference pipeline | NaN propagation from corrupt input causes model to silently return undefined output | RSK-001 (NaN detection in trainer); RSK-004 (log1p clamp before transform); toolkit RSK-001 (RuntimeError halts training) |
| T-007 | Information Disclosure | Audit logs | Inference logs inadvertently include patient-identifiable pixel data | Inference logs record input hash (not raw pixels), output value, timestamp, and software version only |

## Out of Scope

The following are explicitly out of scope for this threat model:

- **Network-layer threats** — this software does not expose a network service, API, or web endpoint in its current form. Any network integration (e.g., PACS connectivity, cloud inference endpoint) requires a separate threat model.
- **Physical access threats** — physical security of the workstation is the responsibility of the deploying institution.
- **PACS system security** — authentication, access control, and audit logging within the PACS system are outside the scope of this software.
- **Operating system vulnerabilities** — host OS hardening is outside the scope of this software's DHF; it is expected that the deploying institution applies OS-level security patches.
