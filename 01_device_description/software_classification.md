# Software Classification — COCA-prj

## IEC 62304 Classification: Class B

### Decision Rationale

| Criterion | Assessment |
|-----------|-----------|
| Serious injury possible if software fails? | Yes — missed calcium detection (false negative) could delay treatment |
| Injury mitigated by operator or other means? | Yes — output is advisory only; radiologist makes final clinical decision (SYS-007) |
| Death possible if software fails? | Not directly — clinical decision remains with radiologist |

**Resulting class: B** — serious injury possible but mitigated by advisory-only design.

Class C does not apply because death is not directly caused by software failure alone
given the advisory-only architecture mandated by SYS-007.

### Implications for COCA-prj

Per IEC 62304 Class B:
- Software development plan required ✓ (CLAUDE.md, branch policy)
- Risk management required ✓ (04_risk_management/)
- System testing required ✓ (`python runtests.py`, smoke tests)
- Regression testing required ✓ (CI forge-health + pytest on every push)

## FDA Risk Classification

AI/ML-enabled SaMD — moderate risk (Class II analog). Advisory output,
not standalone diagnostic.

## Regulatory Pathway

Intended for 510(k) or De Novo pathway pending performance validation.
