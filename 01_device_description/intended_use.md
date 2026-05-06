# Intended Use — COCA-prj

## Device Description

COCA-prj is a software-only medical device (SaMD) that uses deep learning to assist
in detecting and quantifying coronary artery calcium from non-contrast CT images.

## Intended Use Statement

COCA-prj is intended to assist trained radiologists in detecting and quantifying
coronary artery calcium from non-contrast CT images (gated and non-gated protocols).

It is **not** intended as a standalone diagnostic device. Output is advisory; clinical
decisions remain with the responsible clinician.

*Source: Coronary_prj/docs/requirements.yaml, SYS-007*

## Intended User

Trained radiologists with experience in cardiac CT interpretation.

## Target Patient Population

Adults undergoing non-contrast CT for cardiovascular risk assessment, including:
- Gated cardiac CT (calcium scoring protocol)
- Non-gated chest CT (opportunistic calcium scoring)

## Indications for Use

Identification and quantification of coronary artery calcium as an adjunct to clinical
cardiovascular risk assessment.

## Contraindications

- Not intended for emergency diagnostic use
- Not validated for pediatric populations
- Not validated for patients with prior coronary intervention (stents, CABG)

## Operating Environment

Local inference on imaging workstation with trained model artifact. Model trained on
COCA dataset (gated and non-gated protocols).
