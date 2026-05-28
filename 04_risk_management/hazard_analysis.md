# Hazard Analysis — COCA-prj

## Hazard Table

<!-- DHF_HAZARD_ANALYSIS_START -->
| ID | Hazard | Cause | Effect | Severity | Probability | Mitigation |
|----|--------|-------|--------|----------|-------------|------------|
| HAZ-001 | Missed coronary calcium (false negative) | Model underperforms on low-density or small-volume calcification | Radiologist underestimates cardiovascular risk; delayed clinical follow-up | serious | remote | RSK-001 |
| HAZ-002 | Over-estimated calcium score (false positive) | Regression model over-predicts Agatston score on ambiguous anatomy | Unnecessary further workup or treatment escalation | minor | remote | RSK-002 |
| HAZ-003 | Silent ingestion failure — corrupt or missing DICOM processed as valid | Ingestor fails to raise an error on malformed input and produces partial output | Wrong model input leads to incorrect output without operator awareness | serious | remote | RSK-003 |
| HAZ-004 | NaN propagation from log-transformed regression targets | Zero or negative Agatston score not handled before log1p transformation | NaN loss corrupts training or produces undefined regression output | minor | remote | RSK-004 |
<!-- DHF_HAZARD_ANALYSIS_END -->

## Toolkit Hazards (medical_image_ai_toolkit)

These hazards apply to the shared ML infrastructure used by this project.
They are maintained manually here and mitigated by toolkit-level risk controls.

| ID | Hazard | Cause | Effect | Severity | Probability | Mitigation |
|----|--------|-------|--------|----------|-------------|------------|
| H-005 | NaN loss propagation corrupting model weights | Loss function receives NaN from task output | Corrupted model produces unreliable outputs | Serious | Remote | toolkit RSK-001 |
| H-006 | Artifact-model mismatch — wrong model loaded at inference | No schema binding between saved weights and model class | Incorrect predictions, undetected error | Serious | Remote | toolkit RSK-002 |
| H-007 | Training data leaking into test evaluation | Incorrect partitioning or shared patient IDs across splits | Falsely optimistic performance metrics | Minor | Remote | toolkit RSK-003 |

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
