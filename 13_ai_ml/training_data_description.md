# Training Data Description — <!-- DHF_VAR:PROJECT_NAME -->COCA-prj<!-- /DHF_VAR:PROJECT_NAME -->

Per FDA AI/ML SaMD Guidance (2021) §III. Documents the provenance, composition,
and known limitations of all data used to train and validate the algorithm.

## 1. Dataset Overview

| Dataset | Role | Size | Source | Version / Date Frozen |
|---|---|---|---|---|
| COCA — Gated protocol (train partition) | Training — segmentation | ~80% of gated patients | Stanford Medicine Radiological AI Lab, PhysioNet | Public release; frozen at project baseline 2026-05-05 |
| COCA — Gated protocol (val partition) | Validation (hyperparameter tuning) | ~10% of gated patients | Same | Same |
| COCA — Gated protocol (test partition) | Test (locked) | ~10% of gated patients | Same | Same |
| COCA — Nongated protocol (train partition) | Training — regression | ~80% of nongated patients | Stanford Medicine Radiological AI Lab, PhysioNet | Public release; frozen at project baseline 2026-05-05 |
| COCA — Nongated protocol (val partition) | Validation (hyperparameter tuning) | ~10% of nongated patients | Same | Same |
| COCA — Nongated protocol (test partition) | Test (locked) | ~10% of nongated patients | Same | Same |

Partitioning is deterministic using `DeterministicHoldoutSplit` with a fixed random seed.
The test partition is locked and never used for training or hyperparameter selection.
See `13_ai_ml/predetermined_change_control_plan.md` §5 for test set integrity controls.

## 2. Data Collection Protocol

The COCA dataset is a publicly available, de-identified dataset collected at Stanford Medicine.
It contains non-contrast cardiac CT scans with expert-annotated coronary artery calcium regions.

- **Imaging modality / acquisition protocol:** Non-contrast CT; two protocols:
  - **Gated:** Electrocardiogram (ECG)-gated cardiac CT (standard calcium scoring protocol); pixel annotations provided as XML (Apple plist format) per-patient
  - **Nongated:** Non-ECG-gated chest CT (opportunistic calcium scoring); Agatston scores provided per-vessel (LCA, LAD, LCX, RCA) in `scores.xlsx`
- **Site(s):** Stanford Health Care (single-site dataset)
- **Inclusion criteria:** Adult patients undergoing non-contrast CT for cardiovascular risk assessment
- **Exclusion criteria:** Contrast-enhanced CT; pediatric patients; patients with known prior coronary stents or CABG (not explicitly filtered in public dataset — treat as a known limitation)
- **Labeling procedure (gated):** Expert radiologist contour annotations (polygon ROIs per CT slice); stored as plist XML
- **Label quality assurance:** COCA is a published research dataset with multi-reader annotation consensus; full QA procedure details are in the original COCA publication

## 3. Patient Demographics

Demographics for the COCA dataset are as reported in the original publication (Commandeur et al., 2020). This project does not have access to patient-level demographic metadata beyond what is encoded in the DICOM headers.

| Characteristic | COCA Dataset (overall) | Notes |
|---|---|---|
| Age | Adults; distribution available in COCA publication | Not stratified per partition in this project |
| Sex | Mixed male/female; distribution in COCA publication | Not stratified per partition in this project |
| CAC score distribution | Broad range including CAC = 0 | COCA dataset is specifically collected to include both zero-calcium and high-calcium patients |
| Site | Single-site (Stanford Health Care) | Single-site is a known generalization limitation |

## 4. Known Limitations and Gaps

| Limitation | Description | Mitigating Control |
|---|---|---|
| Single-site data | All CT scans collected at one institution; scanner models, acquisition protocols, and patient population may differ from deployment site | Advisory-only architecture (SYS-007); performance re-evaluation required before deployment at new institution |
| Post-intervention patients not excluded | Patients with prior coronary stents or CABG may be present in the dataset; stent artifacts affect calcium scoring accuracy | Contraindication in intended use: "Not validated for patients with prior coronary intervention" |
| Pediatric patients not present | COCA is an adult dataset; pediatric anatomy and calcium patterns not represented | Contraindication: "Not validated for pediatric populations" |
| Opportunistic nongated scoring | Nongated calcium scores are derived from chest CT not acquired in a calcium-scoring protocol; subject to higher noise and partial-volume effects | Advisory-only output; regression MAE threshold gate (RSK-002, MOD-006) |
| Patient 103 (nongated) | Patient ID 103 has no score entry in `scores.xlsx`; zero-filled per DAT-016 | Score zero-fill is documented and tested; impact is minimal for one patient |
| Demographic metadata availability | Race/ethnicity and comorbidity data are not available in the public COCA release | Cannot perform subgroup bias analysis by race/ethnicity; flagged as limitation |

## 5. Bias Assessment

Formal bias analysis by subgroup is not possible for this dataset because race/ethnicity
and comorbidity data are not available in the public COCA release. The following proxy
assessments are made:

| Subgroup | N (test) | Metric | Assessment |
|---|---|---|---|
| CAC = 0 (zero-calcium patients) | ~10% of test partition | Dice (gated) | Zero-calcium slices contribute zero-mask targets; model must not produce false positives — tested via Dice threshold gate (RSK-001) |
| High CAC (score > 400 AU) | Present in dataset | MAE (nongated) | Higher absolute error expected at extreme scores; MAE threshold gate (MOD-006) applies |
| Sex | Mixed; not stratified | N/A | Cannot be assessed without per-patient sex metadata in test partition |
| Race/ethnicity | Unknown | N/A | Cannot be assessed; flagged as gap for post-market surveillance |

Subgroup performance gaps that exceed clinically relevant thresholds require mitigation via:
- Contraindication in labeling, or
- Targeted data augmentation in retraining, or
- Explicit risk control in `04_risk_management/risk_control_measures.md`

## 6. Data Integrity Controls

- The COCA dataset is used in read-only mode; no modifications are made to the source files.
- Dataset access is controlled by local filesystem permissions and physical access to the storage volume.
- Partitions are generated deterministically (fixed seed) and recorded in `partitions.json` alongside each training artifact.

| Dataset | Freeze Date | Location | Notes |
|---|---|---|---|
| COCA gated | 2026-05-05 | `/Volumes/rqian1TB/coca/cocacoronarycalciumandchestcts-2/Gated_release_final/` | Symlinked via `Coronary_prj/data/raw/coca/` |
| COCA nongated | 2026-05-05 | `/Volumes/rqian1TB/coca/cocacoronarycalciumandchestcts-2/deidentified_nongated/` | Same symlink |

SHA-256 hashes of key annotation files are recorded below (Option A — key files only, per FDA
AI/ML SaMD Guidance §III data integrity requirements). Run `scripts/hash_coca_dataset.sh` when
the external storage volume is mounted to regenerate or verify these values.

| File | SHA-256 | Date Hashed |
|---|---|---|
| `Gated_release_final/calcium_xml/` (manifest) | _pending — run hash_coca_dataset.sh_ | — |
| `deidentified_nongated/scores.xlsx` | _pending — run hash_coca_dataset.sh_ | — |

The COCA dataset is publicly available on PhysioNet (Commandeur et al., 2020; DOI:
10.13026/kcts-ky57). The public PhysioNet versioning provides independent verification of
dataset provenance. Full volume hashing (Option B) is deferred until immediately before
regulatory submission. Individual training partitions are reproducible via the seeded
`DeterministicHoldoutSplit` recorded in `partitions.json` alongside each training artifact.
