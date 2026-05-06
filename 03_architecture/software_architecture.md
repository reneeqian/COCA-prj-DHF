# Software Architecture — COCA-prj

## Component Overview

```
forge-utils (v0.1.0)
    ↓ grading + traceability primitives
regulatory_tools (v1.0.0)
    ↓ EvidenceReport, run_tests_and_trace, soup_checker, rsk_checker
medical_image_ai_toolkit
    ↓ PatientSample, TrainingPipeline, MedicalImageTrainer, DatasetValidator
Coronary_prj
    ├── COCAGatedIngestor     → CoronaryCalciumTask     → UNet2D
    └── COCANongatedIngestor  → NongatedCalciumScoreTask → CalciumScoreRegressor
```

## Component Descriptions

| Component | Repository | Role |
|-----------|-----------|------|
| forge-utils | forge | Dev health grading, requirement coverage, CI gate |
| regulatory_tools | regulatory_tools | Traceability matrix generation, evidence reports, SOUP/RSK enforcement |
| medical_image_ai_toolkit | medical_image_ai_toolkit | Reusable ML training, evaluation, reporting building blocks |
| Coronary_prj | Coronary_prj | COCA-specific ingestion, task logic, model architectures |

## Data Flow

```
DICOM files → COCAGatedIngestor/COCANongatedIngestor
    → PatientSample (image_volume, spacing, annotations, metadata)
    → CoronaryCalciumTask / NongatedCalciumScoreTask
        → {"input": Tensor, "target": Tensor} per slice
    → MedicalImageTrainer
        → UNet2D / CalciumScoreRegressor
    → TrainingPipeline artifacts (model.pt, partitions.json, manifest.json)
    → ModelTestingPipeline → model_testing_report.json
```

## Key Design Decisions

- **Slice-broadcast target**: patient-level label is broadcast to all 2D slices (TSK-006).
  The model learns to estimate the patient-level label from any representative slice.
- **Advisory-only output**: RSK-002 (regression clamping) and RSK-001 (missed calcium
  threshold) enforce advisory posture per SYS-007.
- **DatasetStructureError boundary**: all public ingestor methods raise
  `DatasetStructureError` on failure, never raw exceptions (RSK-003/DAT-014).
