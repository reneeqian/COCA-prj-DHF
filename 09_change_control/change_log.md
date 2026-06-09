# Change Log — <!-- DHF_VAR:PROJECT_NAME -->COCA-prj<!-- /DHF_VAR:PROJECT_NAME -->

## Structured Change Records

| Version | Date | Category | Description | Risk Impact | Author |
|---------|------|----------|-------------|------------|--------|
| 0.1.0 | {{DATE}} | Initial | Initial DHF creation | None | <!-- DHF_VAR:AUTHOR -->Renee Qian<!-- /DHF_VAR:AUTHOR --> |

## Recent Commits (auto-generated)

Auto-generated from `git log --oneline --no-merges` on the Coronary_prj repository.

<!-- DHF_CHANGE_LOG_START -->
| Version | SHA | Description |
|---------|-----|-------------|
| 0.1.0 | e0fe5c2 | feat(dev): add mypy 2.1.0 as qualified verification tool (#73) |
| 0.1.0 | 1f5cc28 | docs(health): update forge health badge — Grade A (score 0.90) |
| 0.1.0 | c1119a4 | feat: restore forge grade A — pip CVE fix, type fixes, ruff cleanup, coverage tests |
| 0.1.0 | 5aac480 | feat(dev): add mypy 2.1.0 as qualified verification tool |
| 0.1.0 | 3e73bcc | chore(deps): bump actions/setup-python from 5 to 6 |
| 0.1.0 | 766a67c | chore(deps): bump actions/dependency-review-action from 4 to 5 |
| 0.1.0 | 2549672 | fix(ci): switch sync-main-to-dev to workflow_run trigger |
| 0.1.0 | 8ef2021 | chore(deps): bump actions/add-to-project from 1.0.2 to 2.0.0 |
| 0.1.0 | e9d897d | fix(ci): skip bot-triggered forge-health runs; fix Dependabot secret access |
| 0.1.0 | bfb2c75 | chore(gitignore): exclude project_summary.md and refresh traceability matrix |
| 0.1.0 | 5584c1b | chore(deps): bump idna from 3.15 to 3.18 |
| 0.1.0 | 236e416 | chore(deps): bump peter-evans/find-comment from 3 to 4 |
| 0.1.0 | 084af66 | ci: add GitHub Actions workflow to auto-add issues/PRs to project board |
| 0.1.0 | 2be547f | fix(audit): replace anomaly_log.md with machine-readable yaml |
| 0.1.0 | ad6a63d | fix(audit): add anomaly log (IEC 62304 §9.1) |
| 0.1.0 | 45c3ca1 | dev → main: forge-utils v0.3.0, conflict resolution, CI hardening (#55) |
| 0.1.0 | 0a4c54b | dev → main: SOUP hygiene, torch/matplotlib bump, CI fixes (#54) |
| 0.1.0 | bc20606 | fix(ci): remove unpinned heavy-dep pre-installs from forge-health |
| 0.1.0 | dea650e | fix(ci): pin dhf-impact.yml to regulatory_tools@v1.1.0 |
| 0.1.0 | c8fcc93 | chore(soup): bump torch/matplotlib, pin idna, add risk+verified_by fields (#53) |
| 0.1.0 | 9570e20 | Bump actions/checkout from 4 to 6 (#50) |
| 0.1.0 | 2911da7 | Bump github/codeql-action from 3 to 4 (#49) |
| 0.1.0 | 48486e2 | Bump peter-evans/create-or-update-comment from 4 to 5 (#48) |
| 0.1.0 | 06b887a | Bump actions/cache from 4 to 5 (#47) |
| 0.1.0 | 7b8b42c | Bump actions/upload-artifact from 4 to 7 (#46) |
| 0.1.0 | cf34527 | dev → main: requirements architecture, DHF integration, RTM with verification fields (#44) |
| 0.1.0 | 3c28b95 | fix(ci): remove unpinned torch/numpy/matplotlib pre-install from pip-audit |
| 0.1.0 | c82fbef | docs: declare IEC 62304 samd_class: C in requirements.yaml metadata (#45) |
| 0.1.0 | 1319cdc | ci: post forge-health status before push to satisfy branch protection |
| 0.1.0 | 0fc87c7 | ci: auto-sync main into dev after every merge |
| 0.1.0 | a19b836 | chore(ci): remove auto-merge workflow (#43) |
| 0.1.0 | bc1e4e0 | feat(dhf): requirements split, derived_from links, hazard analysis, RTM with verification fields (#42) |
| 0.1.0 | eaafe30 | test: Phase 9 — test quality remediation (FIRST+AAA, 1R, ES, BC) (#41) |
| 0.1.0 | be532b4 | fix(deps): pin idna>=3.15 to close CVE-2026-45409 (#37) |
| 0.1.0 | 18bb989 | ci: add pip-audit policy script and update forge-utils to v0.2.0 (#40) |
| 0.1.0 | a0521d0 | feat: add tests for 4 untested requirements (SYS-007, TSK-006, MOD-005, MOD-006) (#38) |
| 0.1.0 | 498ae0b | chore: gitignore CLAUDE.md (local Claude Code instructions, not for version control) (#36) |
| 0.1.0 | 0812646 | chore: gitignore CLAUDE.md (local Claude Code instructions, not for version control) (#35) |
| 0.1.0 | 3404493 | feat: extend kaggle_training.py to support gated and nongated modes (#34) |
| 0.1.0 | e590279 | ci: add pip caching and update forge-utils to v0.2.0 (#33) |
| 0.1.0 | f692188 | Upgrade pydicom 3.0.1 → 3.0.2 to fix CVE-2026-32711 (#32) |
| 0.1.0 | 19142ec | SOUP hardening: pin versions, add pydicom/scikit-image deps, CI security parity (#31) |
| 0.1.0 | 27b6691 | sync: bring main into dev (#30) |
| 0.1.0 | e091b11 | sync: bring dev up to date with main (#28) |
| 0.1.0 | 195f9d8 | chore: remove redundant test CI (forge-health runs pytest internally) (#26) |
| 0.1.0 | aa9dbd5 | sync: bring dev up to date with main (#25) |
| 0.1.0 | 91fc599 | fix: auto-merge workflow must use --squash to match dev branch ruleset (#23) |
| 0.1.0 | 9afbb3b | fix: write forge health to job summary instead of committing README (#22) |
| 0.1.0 | 5cd6860 | fix: sync main history into dev to resolve PR conflicts (#21) |
| 0.1.0 | 2323764 | chore: add CODEOWNERS — auto-request @reneeqian on all PRs (#20) |
| 0.1.0 | 04d8e68 | feat: regulatory hardening — RSK requirements, OOD guard, thresholds, SOUP inventory (#18) |
| 0.1.0 | 75a32e1 | fix: only auto-commit forge health README on main/dev push |
| 0.1.0 | 0366c3b | docs: update forge health report [skip ci] |
| 0.1.0 | 3ad4f1b | fix: use git+https for forge-utils and pin regulatory_tools to @dev |
| 0.1.0 | 7b9fb56 | added nongated ingestor, task definition, and model for calcium score regression. Also added a smoketest script for nongated training and tests for the new ingestor and task definition. Updated README, requirements, traceability matrix, and pyproject.toml to reflect the new additions. |
| 0.1.0 | 431d732 | docs: update forge health report [skip ci] |
| 0.1.0 | 3540301 | feat: add status_report and PDF export support |
| 0.1.0 | cddabf2 | docs: update forge health report [skip ci] |
| 0.1.0 | e504eb2 | feat: add Kaggle training script and update smoketest to use latest sweep params |
| 0.1.0 | 1ae6a0e | docs: update forge health report [skip ci] |
| 0.1.0 | 0f3da61 | test: add EvidenceReport to ingestor and annotation tests; add tuning smoke script |
| 0.1.0 | d850c30 | docs: rewrite README for brevity and accuracy |
| 0.1.0 | a807df9 | docs: update forge health report [skip ci] |
| 0.1.0 | 74641a4 | ci: pin regulatory_tools to main branch |
| 0.1.0 | 94bb077 | fix: install regulatory_tools from dev branch for README health update |
| 0.1.0 | a6de0a8 | docs: update forge health report [skip ci] |
| 0.1.0 | d24daa3 | ci: fix workflows to enable forge health on PRs to dev |
| 0.1.0 | 45f3f3e | fix: make README commit-back non-fatal on protected branches |
| 0.1.0 | bee0356 | feat: README forge health update and auto-merge on dev |
| 0.1.0 | 2f8f601 | Opt into Node.js 24 for GitHub Actions |
| 0.1.0 | 9b61435 | Fix forge-utils pip install syntax for git extras |
| 0.1.0 | ae6fcbb | Split CI into separate test and forge health workflows |
| 0.1.0 | 8689a7d | Add forge health assessment to CI on every branch push |
| 0.1.0 | 090b6e4 | Improve code quality: static analysis, type annotations, requirement coverage |
| 0.1.0 | a83e745 | added forge.toml |
| 0.1.0 | 6bc4907 | naming update, converting validation to modeltesting |
| 0.1.0 | b6ba17e | adding a healthstatus badge |
| 0.1.0 | 2b199b5 | fix: track models source package blocked by gitignore |
| 0.1.0 | 3ba0aca | updated smoketesttraining.py to use UNet2D model and print training outputs. Updated smoketestvalidation.py to use UNet2D model. |
| 0.1.0 | d9fcb39 | update smoketestvalidation.py |
| 0.1.0 | fab19eb | Clean traceability markers and tracked bytecode |
| 0.1.0 | 3dc924c | added requirements |
| 0.1.0 | b9b1117 | doc update |
| 0.1.0 | dc3bee3 | tests passing locally with new task test |
| 0.1.0 | 6d9d1e4 | updating smoke test training for task definition and valdiation changes |
| 0.1.0 | 918d982 | set up for validation smoke test script |
| 0.1.0 | badbf58 | updated gated ingestory to gracefully handle corrupt patient dicoms, slice indexing was also handled |
| 0.1.0 | 760b084 | fixed the slice indexing issue in COCA ingestor |
| 0.1.0 | f8cbc13 | github action should work now |
| 0.1.0 | fa1f2b5 | updates run_tests_and_trace.py to runtests.py to reflect that it now contains more than just testing the traceability report generation, but also includes tests for project structure and documentation requirements. This renaming better reflects the broader scope of the testing functionality provided by this script. Additionally, updated the test_project_structure.py to align with the new requirement tags for documentation-related checks. |
| 0.1.0 | cd63779 | update the requirement_id to requirement_tag changes |
| 0.1.0 | af03c07 | updating how tests and reporting is done |
| 0.1.0 | 5b19fb7 | getting smoketesttraining.py up to date with main |
| 0.1.0 | 4cf4ac2 | update run_tests_and_trace.py to remove source_dir argument and adjust pytest runner accordingly |
| 0.1.0 | ba178b0 | readme update |
| 0.1.0 | 9f13bec | more clean up |
| 0.1.0 | 9beed85 | polishing up the testing pocess |
| 0.1.0 | c919400 | updated traceability matrix generator to include requirement coverage summary and untested requirements list; updated run_tests_and_trace.py to calculate and pass requirement coverage summary to the generator. |
| 0.1.0 | 1b7414c | removed task definition |
| 0.1.0 | ed6fcee | removed task definition and switching to putting task implication in ingestor |
| 0.1.0 | aebf8cb | new reqs |
| 0.1.0 | 9795d9f | new requirements to include task definition |
| 0.1.0 | a60f244 | mnc |
| 0.1.0 | 0142660 | added coca task definition |
| 0.1.0 | eb9c3c7 | removed unnecessary file |
| 0.1.0 | 610c4a0 | added a test for z=ordering |
| 0.1.0 | 10bd5e2 | all tests passing locally |
| 0.1.0 | a6bc644 | base ingestor |
| 0.1.0 | b2e4cd5 | added pytest-cov to run-tests.yml |
| 0.1.0 | f5febd0 | run-tests.yml fix |
| 0.1.0 | fb2c637 | using existing code |
| 0.1.0 | c173fa3 | still debugging run-tests.ymlß |
| 0.1.0 | c2fa9af | fixed a whoopsie mistake |
| 0.1.0 | 2774047 | debugging run-tests.yml |
| 0.1.0 | f75f144 | debugging |
| 0.1.0 | 6742601 | debugging |
| 0.1.0 | 0080f5d | trying to fix run-tests.yml |
| 0.1.0 | cb6d449 | fixing run-tests.yml to include code coverage report generation and fixing a bug in the slice index calculation in coca_gated_ingestor.py |
| 0.1.0 | e6bdfb2 | modifying: .github/workflows/run-tests.yml |
| 0.1.0 | ad46084 | add ci workflow for running tests and generating coverage report |
| 0.1.0 | ba04cbc | updated the ingestor with a get_sample method |
| 0.1.0 | 23ae696 | getting smoke test to work |
| 0.1.0 | d344984 | tests passing |
| 0.1.0 | 6a0b9a8 | updated requirements |
| 0.1.0 | 1ed0aa3 | tests passing and linked in traceability matrix.  next need to have tests generate artifacts |
| 0.1.0 | e096663 | tests passing and reached 89% code coverage. Added a check to ensure that contours with fewer than 3 points are skipped, as they cannot form a valid polygon. Updated the requirements document to include the need for automated tests verifying annotation validity. |
| 0.1.0 | 9e2c407 | updating tests, still trying to gain coverage |
| 0.1.0 | 48b3c5d | added coverage and modifying requirements |
| 0.1.0 | 7a5c714 | added doc requirements and test for project structure |
| 0.1.0 | 59fa49f | updating requirements and tests for traceability tool |
| 0.1.0 | f09c3d0 | moved requiremnts back |
| 0.1.0 | ee809bd | update readme |
| 0.1.0 | b5d7031 | updated requirements to be trimmed and simplified |
| 0.1.0 | 2c02715 | updated documentation to simplify things |
| 0.1.0 | e9cad94 | Consolidate documentation into minimal regulated structure |
| 0.1.0 | 0fafe93 | kjhgf |
| 0.1.0 | 48c675d | some more changes |
| 0.1.0 | 2470cd5 | Remove exploratory development folder from tracked repo |
| 0.1.0 | 9db736e | pause point |
| 0.1.0 | 3cc278f | update readme |
| 0.1.0 | f3fe042 | tests pass now |
| 0.1.0 | 1c81a32 | added marker to pytest.ini for tests that require external datasets |
| 0.1.0 | af09dbb | updated traceability matrix and tests to reflect changes in requirements and codebase. Added a new test to check that setting a random seed results in the same metrics across runs. |
| 0.1.0 | 51ecfdc | got traceaility matrix generation working, added evidence auto-saving in tests, and updated the test for dataset structure to save evidence as well. |
| 0.1.0 | 3cc4dec | set up a run tests and traceability matrix script, and update the evidence report structure to better capture test results and associated requirements. |
| 0.1.0 | 812d6d3 | removed files related to the package metadata, likely as part of a cleanup or restructuring of the project. The tests have been updated to use a fixture for the dataset root and to include requirement IDs in the test reports. |
| 0.1.0 | df346f6 | modified gitignore |
| 0.1.0 | 2ea064e | adding a formal documentation |
| 0.1.0 | 2901f15 | restructured project to be a package, moved files around, updated imports, and added some new files. Also updated tests to reflect new structure. |
| 0.1.0 | 221e455 | update to reflect evidence report move to regulatory tools |
| 0.1.0 | 0f96b3d | updating to accept external libraries |
| 0.1.0 | 234bc23 | update gitignore |
| 0.1.0 | 9b464da | pulling out medical_image_ai_toolkit and regulatory_tools |
| 0.1.0 | 5c7ac12 | adsfa |
| 0.1.0 | e49f70f | got the traceability command to work but not finding rows. |
| 0.1.0 | 1709d08 | trying to get regulatory tools working and also need to set up python project paths to avoid path issues |
| 0.1.0 | dbcbe61 | getting started adding pytest requirement IDs so that it will autogen the traceability matrix |
| 0.1.0 | b3d1aed | added regulatory_tools module and updated tests to reflect changes in requirements and traceability diagram |
| 0.1.0 | ade21b4 | realigning requirements and traceability matrix with the current state of the project, and updating tests to reflect changes in the medical image trainer and related components. |
| 0.1.0 | e65414d | adding unit tests |
| 0.1.0 | d5cb795 | doing an initial separation of medicalimagetoolkit and reorganizing src |
| 0.1.0 | de3e679 | updated traceability matrix |
| 0.1.0 | f3063a0 | added evidence gathering and fixed requirements_id input bug |
| 0.1.0 | 30b4904 | training works, now to pull out medical_image_trainer |
| 0.1.0 | 73c43cc | training now works |
| 0.1.0 | b4b254b | kuyfhgjbn |
| 0.1.0 | 4022bf2 | updated before beginning splitstrategy and taskdefinition |
| 0.1.0 | 67fcbf6 | created a current_state_design_and_conventions.md to keep track of current design conventions and rules |
| 0.1.0 | f47fc67 | rename |
| 0.1.0 | 6a40901 | small fix to test so that in the case of using a dummy dataset, the test still runs correctly |
| 0.1.0 | ff96405 | getting started with medical_image_trainer |
| 0.1.0 | 6b44c35 | moved:   src/medimg_training/dataobjects/patient_sample.py |
| 0.1.0 | 42a4742 | all tests passing |
| 0.1.0 | aef05ec | module reorg appears to work, next get tests to pass |
| 0.1.0 | 03a3d96 | still figuring out medimg_training as a module |
| 0.1.0 | 1d4c62d | trying to get medimg_training to work as a extractable module |
| 0.1.0 | 34ac927 | chnaged requirements to suite separation between coronary_prj and medimg_training. |
| 0.1.0 | 6d29b43 | docing |
| 0.1.0 | 36a490b | separation of documentation between CAC project and medimg_training package |
| 0.1.0 | b1868f3 | updating documentation |
| 0.1.0 | 208fc3c | implemented ingestor, validator, and pytest |
| 0.1.0 | 8bd8a0c | getting started with an ingestor |
| 0.1.0 | 6a54755 | started coca_gated_ingestor.py and updated data contracts to be consistent |
| 0.1.0 | 7f17aff | getting started with skeleton for coca gated ingestor |
| 0.1.0 | ffdda98 | scratch script (explore_coca.py) to visualize COCA patient CAC data and experiment for eventual ingestor |
| 0.1.0 | f5fb83a | getting started with coca_adapter |
| 0.1.0 | f75dff2 | picked a dataset. updated README and docs |
| 0.1.0 | 8fc94cb | updating requirements and assumptions |
| 0.1.0 | ab86a19 | first commit |
<!-- DHF_CHANGE_LOG_END -->
