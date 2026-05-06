# Risk Control Measures — COCA-prj

## Control Measure Table

| RSK ID | Hazard ID | Hazard | Control Measure | Implementation | Verification Test |
|--------|-----------|--------|-----------------|----------------|-------------------|
| Coronary_prj RSK-001 | H-001 | Missed calcium detection | Min Dice threshold gates deployment | `thresholds.SEGMENTATION_MIN_DICE`, evaluated in ModelTestingPipeline | `test_risk_controls.py` |
| Coronary_prj RSK-002 | H-002 | Over-estimation of calcium score | Back-transform with expm1; clamp negatives to 0 | Inference post-processing code | `test_risk_controls.py` |
| Coronary_prj RSK-003 | H-003 | Silent ingestion failure | Public ingestor APIs raise `DatasetStructureError` | `BaseIngestor.get_sample()` | `test_risk_controls.py` |
| Coronary_prj RSK-004 | H-004 | NaN in log-transformed targets | Clamp negative scores to 0 before log1p | `NongatedCalciumScoreTask.generate_training_samples()` | `test_risk_controls.py` |
| toolkit RSK-001 | H-005 | NaN loss propagation | Detect non-finite loss, raise RuntimeError | `MedicalImageTrainer` | `test_risk_controls.py::test_nan_loss_halts_training_with_runtime_error` |
| toolkit RSK-002 | H-006 | Artifact-model mismatch | Write manifest with model_class, param_count, training_config | `training_pipeline._write_model_manifest()` | `test_risk_controls.py::test_model_manifest_contains_required_fields` |
| toolkit RSK-003 | H-007 | Training data in test evaluation | Partition non-overlap detectable via VER-003 | `DeterministicHoldoutSplit` | `test_risk_controls.py::test_train_test_partition_no_overlap` |

## Control Measure Priority

All controls are **protective measures** (IEC 62304 priority 2). Advisory-only output (SYS-007)
serves as a system-level inherently safe design (priority 1) for H-001 and H-002.
