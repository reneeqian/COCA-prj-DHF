# Residual Risk Evaluation — COCA-prj

## Summary

| Hazard ID | Residual Risk Level | Acceptable? | Notes |
|-----------|--------------------|-|-------|
| H-001 | Low | Yes | Advisory output + min Dice threshold gate |
| H-002 | Negligible | Yes | Clamping + advisory output |
| H-003 | Low | Yes | DatasetStructureError boundary + evidence reporting |
| H-004 | Negligible | Yes | log1p clamping before transform |
| H-005 | Low | Yes | RuntimeError halts training before weights corrupted |
| H-006 | Low | Yes | Manifest + model_class check at load time |
| H-007 | Negligible | Yes | Automated partition overlap test in CI |

## Overall Residual Risk Conclusion

Residual risk is acceptable. The benefits of automated calcium detection assistance
(consistent detection, reduced radiologist workload, opportunistic screening) outweigh
the residual risks because:

1. All high-severity hazards are mitigated by advisory-only architecture (SYS-007)
2. Automated risk controls are continuously verified in CI
3. Model performance is gated by acceptance thresholds before deployment

Reviewed by: Renee Qian — 2026-05-05
