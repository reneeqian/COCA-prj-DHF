# Verification Evidence Index — <!-- DHF_VAR:PROJECT_NAME -->COCA-prj<!-- /DHF_VAR:PROJECT_NAME -->

Evidence reports are stored as JSON artifacts in `artifacts/evidence_runs/` in each code
repository. CI uploads them as workflow artifacts.

## Evidence Summary

| Repository | Latest CI Run | Grade |
|------------|--------------|-------|
| <!-- DHF_VAR:CODE_REPO -->Coronary_prj, medical_image_ai_toolkit, regulatory_tools<!-- /DHF_VAR:CODE_REPO --> | {{CI_RUN}} | — |

## Evidence Artifacts

<!-- DHF_EVIDENCE_INDEX_START -->
*Latest run: `20260609_151723`*

| Test ID | Subject | Result | Requirements | Timestamp |
|---------|---------|--------|--------------|-----------|
| DAT001_base_ingestor_abstract_methods_20260609_151723_954288 | BaseIngestor abstract method bodies raise NotImplementedError | PASS | DAT-001 | 2026-06-09T22:17:23.954271 |
| DAT001_dataset_structure_validation_20260609_151723_997504 | DAT-001: missing patient/ directory raises DatasetStructureError | PASS | DAT-001 | 2026-06-09T22:17:23.997444 |
| DAT001_list_patient_ids_os_error_20260609_151723_970253 | list_patient_ids wraps OSError into DatasetStructureError | PASS | DAT-001 | 2026-06-09T22:17:23.970045 |
| DAT001_missing_patient_root_20260609_151723_955803 | Missing patient root raises DatasetStructureError | PASS | DAT-001 | 2026-06-09T22:17:23.955767 |
| DAT001_no_patient_directories_20260609_151723_992266 | Empty patient root raises DatasetStructureError | PASS | DAT-001 | 2026-06-09T22:17:23.992069 |
| DAT002_load_unexpected_exception_20260609_151723_971921 | load_patient_sample wraps unexpected exceptions into DatasetStructureError | PASS | DAT-002 | 2026-06-09T22:17:23.971514 |
| DAT002_slice_determinism_20260609_151723_994853 | Repeated slice retrieval produces identical arrays | PASS | DAT-002 | 2026-06-09T22:17:23.993734 |
| DAT003_invalid_patient_id_20260609_151724_008792 | DAT-003: patient directory with no DICOM series raises DatasetStructureError | PASS | DAT-003 | 2026-06-09T22:17:24.008457 |
| DAT004_get_slice_success_20260609_151723_986414 | Slice retrieved with correct HU conversion | PASS | DAT-004 | 2026-06-09T22:17:23.984918 |
| DAT004_missing_image_position_20260609_151723_983311 | DICOM missing ImagePositionPatient raises DatasetStructureError | PASS | DAT-004 | 2026-06-09T22:17:23.982390 |
| DAT004_nongated_z_sort_20260609_151724_166197 | COCANongatedIngestor Z-sort | PASS | DAT-004 | 2026-06-09T22:17:24.155066 |
| DAT004_skip_dicom_without_position_20260609_151724_263339 | DAT-004: DICOMs missing ImagePositionPatient are skipped with a warning | PASS | DAT-004 | 2026-06-09T22:17:24.260358 |
| DAT005_annotation_xml_parse_failure_20260609_151723_965806 | Malformed annotation XML raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T22:17:23.964638 |
| DAT005_invalid_dicom_file_20260609_151723_968616 | Invalid DICOM file raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T22:17:23.967622 |
| DAT005_missing_image_position_patient_20260609_151723_962063 | DICOM missing ImagePositionPatient raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T22:17:23.960957 |
| DAT005_no_dicom_files_20260609_151723_990230 | Series with no DICOM files raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T22:17:23.989849 |
| DAT005_no_series_directories_20260609_151723_988096 | Patient with no series directories raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T22:17:23.987864 |
| DAT005_patient_without_series_20260609_151723_957404 | Patient directory without series raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T22:17:23.957179 |
| DAT005_series_without_dicoms_20260609_151723_959549 | Series directory with no DICOM files raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T22:17:23.959124 |
| DAT006_get_patient_api_20260609_151724_022556 | DAT-006: load_patient_sample returns PatientSample with correct patient_id | PASS | DAT-006 | 2026-06-09T22:17:24.021111 |
| DAT007_annotation_slice_out_of_bounds_20260609_151723_974897 | Annotation slice index outside volume is ignored | PASS | DAT-007 | 2026-06-09T22:17:23.973555 |
| DAT008_nongated_deterministic_loading_20260609_151724_257586 | DAT-008: loading the same nongated patient twice returns identical volumes | PASS | DAT-008 | 2026-06-09T22:17:24.244921 |
| DAT009_invalid_polygon_skipped_20260609_151723_930875 | ROI with <3 points is skipped | PASS | DAT-009 | 2026-06-09T22:17:23.929351 |
| DAT009_roi_insufficient_points_ignored_20260609_151723_978341 | ROI with fewer than 3 points is ignored | PASS | DAT-009 | 2026-06-09T22:17:23.976861 |
| DAT009_valid_annotation_geometry_20260609_151723_927263 | Valid annotation geometry: polygon shape and dtype | PASS | DAT-009 | 2026-06-09T22:17:23.925182 |
| DAT010_dataset_without_annotations_20260609_151723_980847 | Dataset with no annotation files returns empty annotations | PASS | DAT-010 | 2026-06-09T22:17:23.979971 |
| DAT010_missing_annotation_file_empty_20260609_151723_933627 | Missing annotation file returns empty annotations | PASS | DAT-010 | 2026-06-09T22:17:23.932718 |
| DAT011_datasource_partition_assignment_20260609_151724_316287 | Datasource partition generation | PASS | DAT-011 | 2026-06-09T22:17:24.316215 |
| DAT012_ct_volume_sorted_by_z_20260609_151724_037301 | DAT-012: CT volume slices are sorted by Z position | PASS | DAT-012 | 2026-06-09T22:17:24.036155 |
| DAT013_contour_rasterization_20260609_151723_937757 | Annotation rasterization — polygon to mask | PASS | DAT-013 | 2026-06-09T22:17:23.937638 |
| DAT013_mask_dimension_alignment_20260609_151723_938827 | Annotation rasterization — mask shape matches source | PASS | DAT-013 | 2026-06-09T22:17:23.938631 |
| DAT013_task_rasterizes_contour_to_nonzero_mask_20260609_151724_270771 | DAT-013: CoronaryCalciumTask rasterizes contour annotations to non-zero binary mask | PASS | DAT-013 | 2026-06-09T22:17:24.270501 |
| DAT014_domain_safe_ingestion_errors_20260609_151723_941165 | Domain-safe ingestion errors — DatasetStructureError | PASS | DAT-014 | 2026-06-09T22:17:23.940268 |
| DAT014_missing_patient_directory_20260609_151723_942882 | Domain-safe ingestion errors — missing patient directory | PASS | DAT-014 | 2026-06-09T22:17:23.942834 |
| DAT015_scores_file_not_found_20260609_151724_055338 | DAT-015: missing scores.xlsx raises DatasetStructureError | PASS | DAT-015 | 2026-06-09T22:17:24.055004 |
| DAT016_scores_attached_20260609_151724_116400 | COCANongatedIngestor score loading | PASS | DAT-016 | 2026-06-09T22:17:24.105384 |
| DOC001_readme_exists_with_heading_20260609_151727_355166 | DOC-001: README.md exists and contains at least one Markdown heading | PASS | DOC-001 | 2026-06-09T22:17:27.355067 |
| DOC002_requirements_yaml_valid_structure_20260609_151727_353326 | DOC-002: requirements.yaml exists and has required structure | PASS | DOC-002 | 2026-06-09T22:17:27.299961 |
| DOC003_traceability_matrix_row_schema_20260609_151727_631549 | Traceability matrix row schema — requirement_id field present in every row | PASS | DOC-003 | 2026-06-09T22:17:27.569127 |
| INF001_inference_capability_20260609_151727_041641 | Inference capability on new data | PASS | INF-001 | 2026-06-09T22:17:27.036728 |
| INF002_inference_determinism_20260609_151727_050560 | Inference determinism — identical inputs produce identical outputs | PASS | INF-002 | 2026-06-09T22:17:27.043068 |
| MOD001_small_cnn_output_shape_20260609_151727_052755 | SmallSegmentationCNN output shape | PASS | MOD-001 | 2026-06-09T22:17:27.051971 |
| MOD001_unet2d_configurable_channels_20260609_151727_088516 | UNet2D base_channels configuration | PASS | MOD-001 | 2026-06-09T22:17:27.062919 |
| MOD001_unet2d_finite_outputs_20260609_151727_099726 | UNet2D outputs are finite on random input | PASS | MOD-001 | 2026-06-09T22:17:27.090947 |
| MOD001_unet2d_gradient_flow_20260609_151727_117639 | UNet2D gradient flow verification | PASS | MOD-001 | 2026-06-09T22:17:27.101168 |
| MOD001_unet2d_output_shape_20260609_151727_060982 | UNet2D output shape preserves spatial dimensions | PASS | MOD-001 | 2026-06-09T22:17:27.053776 |
| MOD002_model_persistence_20260609_151726_013412 | Model artifact persistence — save and reload | PASS | MOD-002 | 2026-06-09T22:17:25.960356 |
| MOD003_model_evaluation_20260609_151727_034834 | Model evaluation capability on test partition | PASS | MOD-003 | 2026-06-09T22:17:26.017550 |
| MOD004_regressor_finite_output_20260609_151727_244298 | CalciumScoreRegressor finite outputs | PASS | MOD-004 | 2026-06-09T22:17:27.236092 |
| MOD004_regressor_gradient_flow_20260609_151727_255793 | CalciumScoreRegressor gradient flow | PASS | MOD-004 | 2026-06-09T22:17:27.246252 |
| MOD004_regressor_output_shape_20260609_151727_124301 | CalciumScoreRegressor output shape | PASS | MOD-004 | 2026-06-09T22:17:27.119121 |
| MOD004_regressor_spatial_flexibility_20260609_151727_233828 | CalciumScoreRegressor spatial size flexibility | PASS | MOD-004 | 2026-06-09T22:17:27.125689 |
| MOD005_segmentation_min_dice_20260609_151727_278970 | MOD-005: SEGMENTATION_MIN_DICE equals approved floor 0.50 | PASS | MOD-005 | 2026-06-09T22:17:27.278942 |
| MOD006_regression_max_mae_20260609_151727_280068 | MOD-006: REGRESSION_MAX_MAE_AU equals approved ceiling 100.0 AU | PASS | MOD-006 | 2026-06-09T22:17:27.280056 |
| REP001_training_report_generation_20260609_151727_361379 | Training report generation | PASS | REP-001 | 2026-06-09T22:17:27.358759 |
| REP002_visualization_support_20260609_151727_497033 | Visualization support — training curve figure | PASS | REP-002 | 2026-06-09T22:17:27.363087 |
| REP003_status_report_section_headers_20260609_151727_645191 | REP-003: status_report produces TRAINING, TUNING, and MODEL TESTING section headers | PASS | REP-003 | 2026-06-09T22:17:27.643646 |
| REP004_status_report_model_testing_section_20260609_151727_652594 | REP-004: status_report prints model testing metrics (dice, iou, precision, recall) | PASS | REP-004 | 2026-06-09T22:17:27.652054 |
| REP004_status_report_no_runs_20260609_151727_642017 | status_report handles missing artifact directories | PASS | REP-004 | 2026-06-09T22:17:27.641867 |
| REP004_status_report_training_section_20260609_151727_647944 | REP-004: status_report prints training metrics (final_loss, learning_rate) | PASS | REP-004 | 2026-06-09T22:17:27.647106 |
| REP004_status_report_tuning_section_20260609_151727_650472 | REP-004: status_report prints tuning metrics (num_trials, best_val_loss) | PASS | REP-004 | 2026-06-09T22:17:27.649834 |
| RSK001_segmentation_threshold_20260609_151727_632874 | RSK-001: SEGMENTATION_MIN_DICE equals the approved clinical floor value 0.50 | PASS | RSK-001 | 2026-06-09T22:17:27.632865 |
| RSK002_negative_score_clamped_20260609_151727_633981 | RSK-002: negative calcium scores are clamped before log1p transform | PASS | RSK-002 | 2026-06-09T22:17:27.633745 |
| RSK002_regression_threshold_20260609_151727_635205 | RSK-002: REGRESSION_MAX_MAE_AU equals the approved clinical ceiling 100.0 AU | PASS | RSK-002 | 2026-06-09T22:17:27.635194 |
| RSK003_missing_xlsx_error_20260609_151727_637025 | RSK-003: ingestor raises DatasetStructureError on missing scores.xlsx | PASS | RSK-003 | 2026-06-09T22:17:27.636921 |
| RSK003_ood_hu_warning_20260609_151727_298678 | NongatedCalciumScoreTask emits OOD HU warning when mean HU is extreme | PASS | RSK-003 | 2026-06-09T22:17:27.298499 |
| RSK004_log1p_finite_20260609_151727_639518 | RSK-004: log1p target is finite for zero, large, and negative inputs | PASS | RSK-004 | 2026-06-09T22:17:27.639022 |
| SYS001_volume_sorted_by_z_20260609_151723_936534 | Volume slices are sorted by Z position | PASS | SYS-001 | 2026-06-09T22:17:23.935155 |
| SYS002_DAT011_split_generates_partitions_20260609_151724_313052 | Deterministic holdout split — three-partition generation | PASS | DAT-011, SYS-002 | 2026-06-09T22:17:24.312960 |
| SYS002_split_reproducibility_20260609_151724_314219 | Deterministic holdout split — seed reproducibility | PASS | SYS-002 | 2026-06-09T22:17:24.314128 |
| SYS003_traceability_matrix_generation_20260609_151727_567935 | Traceable verification — traceability matrix generation | PASS | SYS-003 | 2026-06-09T22:17:27.503744 |
| SYS004_coronary_calcium_task_is_instantiable_20260609_151727_657477 | SYS-004: CoronaryCalciumTask can be instantiated without error | PASS | SYS-004 | 2026-06-09T22:17:27.657468 |
| SYS005_coca_gated_ingestor_subclasses_base_ingestor_20260609_151727_658600 | SYS-005: COCAGatedIngestor subclasses BaseIngestor | PASS | SYS-005 | 2026-06-09T22:17:27.658591 |
| SYS006_task_encapsulation_20260609_151727_653556 | Dataset task encapsulation — project-level ownership | PASS | SYS-006 | 2026-06-09T22:17:27.653550 |
| SYS007_intended_use_20260609_151727_659687 | Intended use — advisory, radiologist-facing | PASS | SYS-007 | 2026-06-09T22:17:27.659668 |
| TRN001_initialization_determinism_20260609_151724_369156 | Controlled model initialization — seed determinism | PASS | TRN-001 | 2026-06-09T22:17:24.354828 |
| TRN002_training_artifact_generation_20260609_151725_691426 | Training artifact generation | PASS | TRN-002 | 2026-06-09T22:17:24.371391 |
| TRN003_compute_loss_finite_scalar_20260609_151724_281978 | CoronaryCalciumTask compute_loss returns finite scalar | PASS | TRN-003 | 2026-06-09T22:17:24.275345 |
| TRN003_loss_penalises_wrong_predictions_20260609_151724_303403 | CoronaryCalciumTask loss ordering: wrong > correct | PASS | TRN-003 | 2026-06-09T22:17:24.302516 |
| TRN003_loss_perfect_prediction_20260609_151724_299352 | CoronaryCalciumTask combined loss near zero on perfect prediction | PASS | TRN-003 | 2026-06-09T22:17:24.298088 |
| TRN003_nongated_gradient_flow_20260609_151727_296656 | NongatedCalciumScoreTask gradient flow | PASS | TRN-003 | 2026-06-09T22:17:27.296255 |
| TRN004_model_retraining_20260609_151725_957008 | Coronary model retraining capability | PASS | TRN-004 | 2026-06-09T22:17:25.694329 |
| TRN005_dataset_training_interface_20260609_151724_352878 | Coronary dataset training interface | PASS | TRN-005 | 2026-06-09T22:17:24.320506 |
| TSK001_task_definition_interface_20260609_151727_654410 | Task definition interface — toolkit contract | PASS | TSK-001 | 2026-06-09T22:17:27.654389 |
| TSK001_task_yields_one_sample_per_slice_20260609_151724_266985 | TSK-001: CoronaryCalciumTask yields one sample per CT slice | PASS | TSK-001 | 2026-06-09T22:17:24.266215 |
| TSK002_ignore_short_contours_20260609_151724_273237 | CoronaryCalciumTask ignores contours with fewer than 3 points | PASS | TSK-002 | 2026-06-09T22:17:24.272796 |
| TSK002_task_input_hu_normalised_20260609_151724_286222 | TSK-002: CoronaryCalciumTask normalises input HU values to [-1, +1] range | PASS | TSK-002 | 2026-06-09T22:17:24.284600 |
| TSK002_task_yields_masks_for_annotated_slices_20260609_151724_269107 | TSK-002: CoronaryCalciumTask input/target shapes are (1,1,H,W); unannotated slices get zero target | PASS | TSK-002 | 2026-06-09T22:17:24.268686 |
| TSK003_task_determinism_20260609_151727_656108 | Task determinism — identical inputs produce identical outputs | PASS | TSK-003 | 2026-06-09T22:17:27.655556 |
| TSK004_task_applies_cardiac_hu_window_20260609_151724_295815 | TSK-004: CoronaryCalciumTask applies the cardiac HU window [-160, 240] | PASS | TSK-004 | 2026-06-09T22:17:24.295101 |
| TSK005_hu_above_window_20260609_151727_291254 | NongatedCalciumScoreTask HU window — above | PASS | TSK-004, TSK-005 | 2026-06-09T22:17:27.291177 |
| TSK005_hu_below_window_20260609_151727_290177 | NongatedCalciumScoreTask HU window — below | PASS | TSK-004, TSK-005 | 2026-06-09T22:17:27.290080 |
| TSK005_input_tensor_shape_20260609_151727_283468 | NongatedCalciumScoreTask input tensor shape is (1,1,H,W) | PASS | TSK-005 | 2026-06-09T22:17:27.283343 |
| TSK005_log1p_target_20260609_151727_285598 | NongatedCalciumScoreTask target log1p transform | PASS | TSK-005 | 2026-06-09T22:17:27.285445 |
| TSK005_loss_finite_scalar_20260609_151727_293332 | NongatedCalciumScoreTask MSE loss is finite | PASS | TRN-003, TSK-005 | 2026-06-09T22:17:27.293154 |
| TSK005_loss_higher_for_wrong_20260609_151727_295379 | NongatedCalciumScoreTask MSE loss is monotone in error magnitude | PASS | TSK-005 | 2026-06-09T22:17:27.295297 |
| TSK005_loss_zero_on_perfect_20260609_151727_294349 | NongatedCalciumScoreTask MSE loss near zero on perfect prediction | PASS | TSK-005 | 2026-06-09T22:17:27.294280 |
| TSK005_missing_metadata_zero_score_20260609_151727_288958 | NongatedCalciumScoreTask missing metadata defaults to zero score | PASS | TSK-005 | 2026-06-09T22:17:27.288798 |
| TSK005_target_tensor_shape_20260609_151727_284490 | NongatedCalciumScoreTask target tensor shape is (4,) | PASS | TSK-005 | 2026-06-09T22:17:27.284404 |
| TSK005_wl40_maps_to_zero_20260609_151727_292310 | NongatedCalciumScoreTask WL=40 HU normalises to 0.0 | PASS | TSK-005 | 2026-06-09T22:17:27.292225 |
| TSK005_yields_one_per_slice_20260609_151727_282180 | NongatedCalciumScoreTask yields one sample per slice | PASS | TSK-005 | 2026-06-09T22:17:27.281874 |
| TSK005_zero_score_target_20260609_151727_287638 | NongatedCalciumScoreTask zero-calcium patient yields zero target | PASS | TSK-005 | 2026-06-09T22:17:27.287532 |
| TSK006_gated_broadcast_20260609_151724_307993 | CoronaryCalciumTask broadcast design — every slice receives a target mask | PASS | TSK-006 | 2026-06-09T22:17:24.307139 |
| TSK006_nongated_broadcast_20260609_151727_286600 | NongatedCalciumScoreTask — patient label broadcast to every slice | PASS | TSK-005, TSK-006 | 2026-06-09T22:17:27.286479 |
| VER001_test_suite_existence_20260609_151727_498877 | Automated verification execution — test suite existence | PASS | VER-001 | 2026-06-09T22:17:27.498550 |
| VER002_evidence_capture_20260609_151727_501154 | Evidence capture — auto_save produces loadable JSON | PASS | VER-002 | 2026-06-09T22:17:27.500497 |
| VER003_model_performance_verification_20260609_151727_502659 | Model performance verification — segmentation metrics | PASS | VER-003 | 2026-06-09T22:17:27.502394 |
| tests/test_coca_ingestor_contract.py::test_graceful_failure_on_missing_data | COCA Ingestor → Missing Dataset Failure Mode | PASS | DAT-005 | 2026-06-09T22:17:23.951322 |
| dat002_list_patient_ids_sorted_numerically_20260609_151724_230635 | DAT-002: list_patient_ids returns patient ids in numeric sort order | PASS | DAT-002 | 2026-06-09T22:17:24.220335 |
| dat004_get_sample_generates_image_and_mask_20260609_151724_040793 | DAT-004: get_sample returns (image, mask) arrays with non-zero mask for annotated patient | PASS | DAT-004 | 2026-06-09T22:17:24.038867 |
| dat004_get_sample_multiple_rois_same_slice_20260609_151724_050010 | DAT-004: multiple ROIs on the same slice are merged into one mask | PASS | DAT-004 | 2026-06-09T22:17:24.048358 |
| dat004_get_sample_no_annotations_returns_empty_20260609_151724_046738 | DAT-004: get_sample returns empty arrays when patient has no annotations | PASS | DAT-004 | 2026-06-09T22:17:24.045718 |
| dat004_ingest_dataset_multiple_patients_20260609_151724_028383 | DAT-004: ingest_dataset loads all patients from the dataset | PASS | DAT-004 | 2026-06-09T22:17:24.026776 |
| dat004_nongated_annotations_always_none_20260609_151724_192104 | DAT-004: nongated ingestor always returns None for vector_rois (score-only dataset) | PASS | DAT-004 | 2026-06-09T22:17:24.181612 |
| dat004_nongated_hounsfield_rescale_applied_20260609_151724_179043 | DAT-004: RescaleSlope and RescaleIntercept are applied to nongated CT pixel values | PASS | DAT-004 | 2026-06-09T22:17:24.169508 |
| dat005_missing_dicom_files_20260609_151724_019425 | DAT-005: patient series dir with no DICOM files raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T22:17:24.018932 |
| dat006_get_sample_returns_single_slice_20260609_151724_044008 | DAT-006: get_sample returns exactly one image/mask pair for a single-slice annotated patient | PASS | DAT-006 | 2026-06-09T22:17:24.042487 |
| dat006_get_volume_api_20260609_151724_025237 | DAT-006: load_patient_sample returns a volume with expected shape | PASS | DAT-006 | 2026-06-09T22:17:24.024224 |
| dat006_lazy_patient_loading_20260609_151724_011727 | DAT-006: COCAGatedIngestor loads each patient volume exactly once | PASS | DAT-006 | 2026-06-09T22:17:24.010345 |
| dat007_get_sample_skips_invalid_slice_annotations_20260609_151724_053160 | DAT-007: annotation with out-of-bounds ImageIndex is skipped; get_sample returns empty arrays | PASS | DAT-007 | 2026-06-09T22:17:24.051704 |
| dat007_slice_index_out_of_bounds_20260609_151724_014133 | DAT-007: annotation referencing out-of-bounds slice is silently ignored | PASS | DAT-007 | 2026-06-09T22:17:24.013222 |
| dat008_deterministic_slice_retrieval_20260609_151724_017095 | DAT-008: loading the same patient twice returns identical slice data | PASS | DAT-008 | 2026-06-09T22:17:24.015981 |
| dat009_annotation_missing_image_index_20260609_151724_034378 | DAT-009: annotation entry missing ImageIndex is treated as no annotation | PASS | DAT-009 | 2026-06-09T22:17:24.032989 |
| dat011_ingest_dataset_enumerates_patient_ids_20260609_151724_031073 | DAT-011: ingest_dataset enumerates all patient IDs without loading volumes | PASS | DAT-011 | 2026-06-09T22:17:24.029844 |
| dat015_empty_dataset_root_raises_20260609_151724_068834 | DAT-015: list_patient_ids raises when root has no patient directories | PASS | DAT-015 | 2026-06-09T22:17:24.056831 |
| dat015_missing_image_position_skipped_20260609_151724_204905 | DAT-015: DICOMs missing ImagePositionPatient are skipped; remaining slices still loaded | PASS | DAT-015 | 2026-06-09T22:17:24.193989 |
| dat015_missing_patient_directory_raises_20260609_151724_079790 | DAT-015: load_patient_sample raises for non-existent patient directory | PASS | DAT-015 | 2026-06-09T22:17:24.070687 |
| dat015_no_dicom_files_raises_20260609_151724_093752 | DAT-015: load_patient_sample raises when patient dir has no .dcm files | PASS | DAT-015 | 2026-06-09T22:17:24.081865 |
| dat015_spacing_fallback_on_missing_metadata_20260609_151724_218239 | DAT-015: missing PixelSpacing metadata falls back to (1,1,1) without raising | PASS | DAT-015 | 2026-06-09T22:17:24.207905 |
| dat016_blank_score_cell_treated_as_zero_20260609_151724_152854 | DAT-016: blank/None score cells in xlsx are coerced to 0.0 | PASS | DAT-016 | 2026-06-09T22:17:24.142355 |
| dat016_get_sample_volume_and_score_array_20260609_151724_242796 | DAT-016: get_sample returns numpy volume and score array with shape (4,) | PASS | DAT-016 | 2026-06-09T22:17:24.232837 |
| dat016_missing_score_entry_zero_fill_20260609_151724_127881 | DAT-016: patient absent from scores.xlsx gets zero-filled scores | PASS | DAT-016 | 2026-06-09T22:17:24.118411 |
| dat016_missing_score_warns_20260609_151724_140258 | DAT-016: missing score entry produces a warning on the ingestor report | PASS | DAT-016 | 2026-06-09T22:17:24.130133 |
| rsk003_ood_guard_20260609_151727_638104 | OOD guard test | PASS | RSK-003 | 2026-06-09T22:17:27.637904 |
| tests/test_project_structure.py::test_soup_inventory_complete | SOUP Inventory → All Dependencies Declared | PASS | DOC-001 | 2026-06-09T22:17:27.356490 |
| tests/test_coca_ingestor_synthetic.py::test_annotation_out_of_bounds_raises | COCA Gated Ingestor → Annotation Bounds Validation | PASS | DAT-004 | 2026-06-09T22:17:24.005530 |
| tests/test_coca_ingestor_synthetic.py::test_hounsfield_rescale_applied | COCA Gated Ingestor → HU Rescale | PASS | DAT-004 | 2026-06-09T22:17:24.002759 |
| tests/test_coca_ingestor_synthetic.py::test_slices_sorted_by_z | COCA Gated Ingestor → Slice Sorting | PASS | DAT-004 | 2026-06-09T22:17:23.999393 |
<!-- DHF_EVIDENCE_INDEX_END -->

## Artifact Locations

| Repository | Path |
|------------|------|
| <!-- DHF_VAR:CODE_REPO -->Coronary_prj, medical_image_ai_toolkit, regulatory_tools<!-- /DHF_VAR:CODE_REPO --> | `artifacts/evidence_runs/{YYYYMMDD_HHMMSS}/` |

*For real-time evidence, check CI workflow artifacts.*
