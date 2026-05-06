# Hazard Analysis — COCA-prj

## Hazard Table

| ID | Hazard | Potential Harm | Severity | Probability | Risk Level | RSK Requirement |
|----|--------|---------------|----------|-------------|-----------|-----------------|
| H-001 | Missed calcium detection (false negative segmentation) | Delayed/missed cardiovascular risk assessment | Serious | Remote | Moderate | Coronary_prj RSK-001 |
| H-002 | Over-estimation of calcium score (false positive regression) | Unnecessary further workup or treatment | Minor | Remote | Low | Coronary_prj RSK-002 |
| H-003 | Silent ingestion failure — corrupt DICOM processed as valid | Wrong model input, incorrect output | Serious | Remote | Moderate | Coronary_prj RSK-003 |
| H-004 | Numerical instability — NaN in log-transformed targets | Training failure or corrupted model weights | Minor | Remote | Low | Coronary_prj RSK-004 |
| H-005 | NaN loss propagation corrupting model weights | Corrupted model produces unreliable outputs | Serious | Remote | Moderate | toolkit RSK-001 |
| H-006 | Artifact-model mismatch — wrong model loaded at inference | Incorrect predictions, undetected error | Serious | Remote | Moderate | toolkit RSK-002 |
| H-007 | Training data leaking into test evaluation | Falsely optimistic performance metrics | Minor | Remote | Low | toolkit RSK-003 |

## Severity Scale

| Level | Definition |
|-------|-----------|
| Negligible | No injury or minor, reversible |
| Minor | Reversible injury, no medical intervention needed |
| Serious | Reversible injury requiring medical intervention |
| Critical | Irreversible injury |
| Catastrophic | Death |

## Probability Scale

| Level | Definition |
|-------|-----------|
| Remote | 1 in 100,000 to 1 in 1,000,000 |
| Occasional | 1 in 1,000 to 1 in 100,000 |
