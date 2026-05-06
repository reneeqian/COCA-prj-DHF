# Key Interfaces — COCA-prj

## Data Contracts

| Interface | Location | Description |
|-----------|----------|-------------|
| `PatientSample` | medical_image_ai_toolkit | `image_volume (D,H,W)`, `spacing`, `annotations`, `metadata` |
| `AnnotationBundle` | medical_image_ai_toolkit | Named `VectorROI` objects (polygons per slice) |
| `TrainingConfig` | medical_image_ai_toolkit | `task`, `split_strategy`, `epochs`, `batch_size`, `lr` |
| `EvidenceReport` | regulatory_tools | Structured test evidence with `info/warn/error` entries |
| `DatasetStructureError` | Coronary_prj | Public ingestor error boundary for corrupt/missing data |

## Model Input/Output

| Model | Input | Output |
|-------|-------|--------|
| UNet2D | `(1, 1, H, W)` single-channel CT slice | `(1, 1, H, W)` segmentation logits |
| CalciumScoreRegressor | `(B, 1, H, W)` CT slice | `(B, 4)` log1p Agatston scores [LCA, LAD, LCX, RCA] |

## Score Regression Post-processing

Output `pred` from `CalciumScoreRegressor` must be back-transformed: `torch.expm1(pred)`.
Values < 0 after back-transformation shall be clamped to 0 (RSK-002, Coronary_prj).

## Error Types

| Exception | Source | Meaning |
|-----------|--------|---------|
| `DatasetStructureError` | Coronary_prj | Corrupt/missing DICOM, invalid annotation, missing scores file |
| `RuntimeError("NaN loss detected")` | medical_image_ai_toolkit | Non-finite loss during training (RSK-001, toolkit) |
| `RuntimeError("Datasource partitions not created")` | medical_image_ai_toolkit | Train called before partitioning |
