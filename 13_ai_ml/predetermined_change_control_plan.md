# Predetermined Change Control Plan — <!-- DHF_VAR:PROJECT_NAME -->COCA-prj<!-- /DHF_VAR:PROJECT_NAME -->

Per FDA Guidance: Artificial Intelligence and Machine Learning in Software as a Medical
Device (2021), adaptive AI/ML devices must describe the types of anticipated modifications
and the controls that ensure continued safety and effectiveness.

## 1. Scope

This plan covers anticipated modifications to the <!-- DHF_VAR:PROJECT_NAME -->COCA-prj<!-- /DHF_VAR:PROJECT_NAME --> algorithm that may
occur post-market without a new 510(k) submission, provided they remain within the
pre-specified bounds defined below.

Two algorithm components are in scope:
1. **Gated segmentation** — UNet2D producing a binary calcium mask; evaluated by Dice score
2. **Nongated regression** — CalciumScoreRegressor producing per-vessel Agatston score estimates; evaluated by MAE in Agatston units

## 2. Types of Anticipated Modifications

| Modification Type | Description | Requires New Submission? |
|---|---|---|
| Performance optimization | Re-training on expanded dataset with same architecture; performance improves within bounds | No — if within §4 bounds |
| Architecture update | Change to model layers, hyperparameters, or preprocessing pipeline | Evaluate per §3 criteria |
| New patient population | Extension to demographics not in original training data | Likely yes |
| New intended use | Application to a different clinical task | Yes — always |
| Input data format change | New imaging modality, resolution, or acquisition protocol | Evaluate per §3 criteria |

## 3. Change Evaluation Criteria

A planned modification does **not** require a new 510(k) if **all** of the following hold:

1. The intended use and indications remain unchanged.
2. The modification does not affect safety-critical risk controls (RSK-* requirements).
3. Post-change performance on the locked test set remains within the bounds in §4.
4. The modification type is listed in §2 as "No — if within bounds."
5. The change is documented in `09_change_control/change_log.md` with the evaluation rationale.

If any criterion fails, engage regulatory counsel before deployment.

## 4. Pre-Specified Performance Bounds

These bounds were established at initial DHF baseline (2026-05-05) and represent the
acceptable performance envelope for algorithm updates without re-submission.

| Metric | Task | Pre-Submission Floor/Ceiling | Acceptable Deviation | Measurement Dataset |
|---|---|---|---|---|
| Dice score (segmentation) | Gated UNet2D | 0.50 (floor; see MOD-005, RSK-001) | Must remain ≥ 0.50 | Locked gated test partition |
| MAE in Agatston units (regression) | Nongated CalciumScoreRegressor | 100.0 AU (ceiling; see MOD-006, RSK-002) | Must remain ≤ 100.0 AU | Locked nongated test partition |

*If post-change performance falls outside these bounds, treat the modification as a new
submission candidate.*

**Note:** `SEGMENTATION_MIN_DICE = 0.50` and `REGRESSION_MAX_MAE_AU = 100.0` are defined
as named constants in `Coronary_prj/src/coronary_prj/thresholds.py` and are verified in CI
(MOD-005, MOD-006, RSK-001, RSK-002 tests). Any change to these constants requires a risk
assessment and update to this PCCP.

## 5. Locked Test Set

Performance evaluation for change control uses a locked, held-out test set that is
never used for training or hyperparameter selection.

| Dataset | Version | Location | Freeze Date |
|---|---|---|---|
| COCA gated — test partition | Public release (PhysioNet) | `/Volumes/rqian1TB/coca/cocacoronarycalciumandchestcts-2/Gated_release_final/` | 2026-05-05 |
| COCA nongated — test partition | Public release (PhysioNet) | `/Volumes/rqian1TB/coca/cocacoronarycalciumandchestcts-2/deidentified_nongated/` | 2026-05-05 |

Partition assignments (patient IDs in each split) are recorded in `partitions.json` in each
training artifact directory. The test partition must not be used for training or
hyperparameter selection. Any change to test set composition requires regulatory counsel
review and update to this PCCP.

## 6. Monitoring Triggers for Unplanned Changes

If post-market monitoring (see `13_ai_ml/model_performance_monitoring_plan.md`) detects:
- Dice score falling below 0.50 on a sample of new production data
- MAE exceeding 100.0 AU on a sample of new production data
- A clinically significant change in output distribution
- New failure modes not present in the original hazard analysis

...then a formal change assessment must be initiated, and a new submission may be required.
