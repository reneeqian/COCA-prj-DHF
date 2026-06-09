# Verification Evidence Index — <!-- DHF_VAR:PROJECT_NAME -->COCA-prj<!-- /DHF_VAR:PROJECT_NAME -->

Evidence reports are stored as JSON artifacts in `artifacts/evidence_runs/` in each code
repository. CI uploads them as workflow artifacts.

## Evidence Summary

| Repository | Latest CI Run | Grade |
|------------|--------------|-------|
| <!-- DHF_VAR:CODE_REPO -->Coronary_prj, medical_image_ai_toolkit, regulatory_tools<!-- /DHF_VAR:CODE_REPO --> | See evidence artifacts below (local run 20260609_073512) | — |

## Evidence Artifacts

<!-- DHF_EVIDENCE_INDEX_START -->
*Latest run: `20260609_073512`*

| Test ID | Subject | Result | Requirements | Timestamp |
|---------|---------|--------|--------------|-----------|
| DAT001_base_ingestor_abstract_methods_20260609_073512_081409 | BaseIngestor abstract method bodies raise NotImplementedError | PASS | DAT-001 | 2026-06-09T14:35:12.081395 |
| DAT001_dataset_structure_validation_20260609_073512_110311 | DAT-001: missing patient/ directory raises DatasetStructureError | PASS | DAT-001 | 2026-06-09T14:35:12.110282 |
| DAT001_list_patient_ids_os_error_20260609_073512_091960 | list_patient_ids wraps OSError into DatasetStructureError | PASS | DAT-001 | 2026-06-09T14:35:12.091827 |
| DAT001_missing_patient_root_20260609_073512_082565 | Missing patient root raises DatasetStructureError | PASS | DAT-001 | 2026-06-09T14:35:12.082536 |
| DAT001_no_patient_directories_20260609_073512_106977 | Empty patient root raises DatasetStructureError | PASS | DAT-001 | 2026-06-09T14:35:12.106874 |
| DAT002_load_unexpected_exception_20260609_073512_093385 | load_patient_sample wraps unexpected exceptions into DatasetStructureError | PASS | DAT-002 | 2026-06-09T14:35:12.093045 |
| DAT002_slice_determinism_20260609_073512_108929 | Repeated slice retrieval produces identical arrays | PASS | DAT-002 | 2026-06-09T14:35:12.108106 |
| DAT003_invalid_patient_id_20260609_073512_118310 | DAT-003: patient directory with no DICOM series raises DatasetStructureError | PASS | DAT-003 | 2026-06-09T14:35:12.118157 |
| DAT004_get_slice_success_20260609_073512_103096 | Slice retrieved with correct HU conversion | PASS | DAT-004 | 2026-06-09T14:35:12.102438 |
| DAT004_missing_image_position_20260609_073512_101310 | DICOM missing ImagePositionPatient raises DatasetStructureError | PASS | DAT-004 | 2026-06-09T14:35:12.100638 |
| DAT004_nongated_z_sort_20260609_073512_240998 | COCANongatedIngestor Z-sort | PASS | DAT-004 | 2026-06-09T14:35:12.232934 |
| DAT004_skip_dicom_without_position_20260609_073512_307617 | DAT-004: DICOMs missing ImagePositionPatient are skipped with a warning | PASS | DAT-004 | 2026-06-09T14:35:12.306436 |
| DAT005_annotation_xml_parse_failure_20260609_073512_088886 | Malformed annotation XML raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T14:35:12.088041 |
| DAT005_invalid_dicom_file_20260609_073512_090711 | Invalid DICOM file raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T14:35:12.090064 |
| DAT005_missing_image_position_patient_20260609_073512_086880 | DICOM missing ImagePositionPatient raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T14:35:12.086256 |
| DAT005_no_dicom_files_20260609_073512_105715 | Series with no DICOM files raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T14:35:12.105472 |
| DAT005_no_series_directories_20260609_073512_104368 | Patient with no series directories raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T14:35:12.104218 |
| DAT005_patient_without_series_20260609_073512_083815 | Patient directory without series raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T14:35:12.083660 |
| DAT005_series_without_dicoms_20260609_073512_085144 | Series directory with no DICOM files raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T14:35:12.084887 |
| DAT006_get_patient_api_20260609_073512_128035 | DAT-006: load_patient_sample returns PatientSample with correct patient_id | PASS | DAT-006 | 2026-06-09T14:35:12.127330 |
| DAT007_annotation_slice_out_of_bounds_20260609_073512_095620 | Annotation slice index outside volume is ignored | PASS | DAT-007 | 2026-06-09T14:35:12.094692 |
| DAT008_nongated_deterministic_loading_20260609_073512_304725 | DAT-008: loading the same nongated patient twice returns identical volumes | PASS | DAT-008 | 2026-06-09T14:35:12.297104 |
| DAT009_invalid_polygon_skipped_20260609_073512_062997 | ROI with <3 points is skipped | PASS | DAT-009 | 2026-06-09T14:35:12.061925 |
| DAT009_roi_insufficient_points_ignored_20260609_073512_097668 | ROI with fewer than 3 points is ignored | PASS | DAT-009 | 2026-06-09T14:35:12.096799 |
| DAT009_valid_annotation_geometry_20260609_073512_060009 | Valid annotation geometry: polygon shape and dtype | PASS | DAT-009 | 2026-06-09T14:35:12.057975 |
| DAT010_dataset_without_annotations_20260609_073512_099454 | Dataset with no annotation files returns empty annotations | PASS | DAT-010 | 2026-06-09T14:35:12.098845 |
| DAT010_missing_annotation_file_empty_20260609_073512_065117 | Missing annotation file returns empty annotations | PASS | DAT-010 | 2026-06-09T14:35:12.064397 |
| DAT011_datasource_partition_assignment_20260609_073512_321353 | Datasource partition generation | PASS | DAT-011 | 2026-06-09T14:35:12.321297 |
| DAT012_ct_volume_sorted_by_z_20260609_073512_140235 | DAT-012: CT volume slices are sorted by Z position | PASS | DAT-012 | 2026-06-09T14:35:12.138786 |
| DAT013_contour_rasterization_20260609_073512_068521 | Annotation rasterization — polygon to mask | PASS | DAT-013 | 2026-06-09T14:35:12.068415 |
| DAT013_mask_dimension_alignment_20260609_073512_069515 | Annotation rasterization — mask shape matches source | PASS | DAT-013 | 2026-06-09T14:35:12.069319 |
| DAT013_task_rasterizes_contour_to_nonzero_mask_20260609_073512_310812 | DAT-013: CoronaryCalciumTask rasterizes contour annotations to non-zero binary mask | PASS | DAT-013 | 2026-06-09T14:35:12.310717 |
| DAT014_domain_safe_ingestion_errors_20260609_073512_071066 | Domain-safe ingestion errors — DatasetStructureError | PASS | DAT-014 | 2026-06-09T14:35:12.070657 |
| DAT014_missing_patient_directory_20260609_073512_072239 | Domain-safe ingestion errors — missing patient directory | PASS | DAT-014 | 2026-06-09T14:35:12.072205 |
| DAT015_scores_file_not_found_20260609_073512_154321 | DAT-015: missing scores.xlsx raises DatasetStructureError | PASS | DAT-015 | 2026-06-09T14:35:12.154132 |
| DAT016_scores_attached_20260609_073512_203355 | COCANongatedIngestor score loading | PASS | DAT-016 | 2026-06-09T14:35:12.194824 |
| DOC001_readme_exists_with_heading_20260609_073514_466606 | DOC-001: README.md exists and contains at least one Markdown heading | PASS | DOC-001 | 2026-06-09T14:35:14.466528 |
| DOC002_requirements_yaml_valid_structure_20260609_073514_465146 | DOC-002: requirements.yaml exists and has required structure | PASS | DOC-002 | 2026-06-09T14:35:14.413693 |
| DOC003_traceability_matrix_row_schema_20260609_073514_720944 | Traceability matrix row schema — requirement_id field present in every row | PASS | DOC-003 | 2026-06-09T14:35:14.663087 |
| INF001_inference_capability_20260609_073514_255059 | Inference capability on new data | PASS | INF-001 | 2026-06-09T14:35:14.250818 |
| INF002_inference_determinism_20260609_073514_261224 | Inference determinism — identical inputs produce identical outputs | PASS | INF-002 | 2026-06-09T14:35:14.256243 |
| MOD001_small_cnn_output_shape_20260609_073514_263423 | SmallSegmentationCNN output shape | PASS | MOD-001 | 2026-06-09T14:35:14.262609 |
| MOD001_unet2d_configurable_channels_20260609_073514_285539 | UNet2D base_channels configuration | PASS | MOD-001 | 2026-06-09T14:35:14.270614 |
| MOD001_unet2d_finite_outputs_20260609_073514_291637 | UNet2D outputs are finite on random input | PASS | MOD-001 | 2026-06-09T14:35:14.286840 |
| MOD001_unet2d_gradient_flow_20260609_073514_304023 | UNet2D gradient flow verification | PASS | MOD-001 | 2026-06-09T14:35:14.293464 |
| MOD001_unet2d_output_shape_20260609_073514_269485 | UNet2D output shape preserves spatial dimensions | PASS | MOD-001 | 2026-06-09T14:35:14.264338 |
| MOD002_model_persistence_20260609_073513_531564 | Model artifact persistence — save and reload | PASS | MOD-002 | 2026-06-09T14:35:13.507777 |
| MOD003_model_evaluation_20260609_073514_249397 | Model evaluation capability on test partition | PASS | MOD-003 | 2026-06-09T14:35:13.533419 |
| MOD004_regressor_finite_output_20260609_073514_376147 | CalciumScoreRegressor finite outputs | PASS | MOD-004 | 2026-06-09T14:35:14.372245 |
| MOD004_regressor_gradient_flow_20260609_073514_381612 | CalciumScoreRegressor gradient flow | PASS | MOD-004 | 2026-06-09T14:35:14.377448 |
| MOD004_regressor_output_shape_20260609_073514_307949 | CalciumScoreRegressor output shape | PASS | MOD-004 | 2026-06-09T14:35:14.305398 |
| MOD004_regressor_spatial_flexibility_20260609_073514_369212 | CalciumScoreRegressor spatial size flexibility | PASS | MOD-004 | 2026-06-09T14:35:14.309016 |
| MOD005_segmentation_min_dice_20260609_073514_398149 | MOD-005: SEGMENTATION_MIN_DICE equals approved floor 0.50 | PASS | MOD-005 | 2026-06-09T14:35:14.398133 |
| MOD006_regression_max_mae_20260609_073514_399099 | MOD-006: REGRESSION_MAX_MAE_AU equals approved ceiling 100.0 AU | PASS | MOD-006 | 2026-06-09T14:35:14.399093 |
| REP001_training_report_generation_20260609_073514_471735 | Training report generation | PASS | REP-001 | 2026-06-09T14:35:14.469268 |
| REP002_visualization_support_20260609_073514_596476 | Visualization support — training curve figure | PASS | REP-002 | 2026-06-09T14:35:14.473238 |
| REP003_status_report_section_headers_20260609_073514_732601 | REP-003: status_report produces TRAINING, TUNING, and MODEL TESTING section headers | PASS | REP-003 | 2026-06-09T14:35:14.731306 |
| REP004_status_report_model_testing_section_20260609_073514_739776 | REP-004: status_report prints model testing metrics (dice, iou, precision, recall) | PASS | REP-004 | 2026-06-09T14:35:14.739149 |
| REP004_status_report_no_runs_20260609_073514_729879 | status_report handles missing artifact directories | PASS | REP-004 | 2026-06-09T14:35:14.729746 |
| REP004_status_report_training_section_20260609_073514_735069 | REP-004: status_report prints training metrics (final_loss, learning_rate) | PASS | REP-004 | 2026-06-09T14:35:14.734265 |
| REP004_status_report_tuning_section_20260609_073514_737471 | REP-004: status_report prints tuning metrics (num_trials, best_val_loss) | PASS | REP-004 | 2026-06-09T14:35:14.736757 |
| RSK001_segmentation_threshold_20260609_073514_722324 | RSK-001: SEGMENTATION_MIN_DICE equals the approved clinical floor value 0.50 | PASS | RSK-001 | 2026-06-09T14:35:14.722315 |
| RSK002_negative_score_clamped_20260609_073514_723390 | RSK-002: negative calcium scores are clamped before log1p transform | PASS | RSK-002 | 2026-06-09T14:35:14.723119 |
| RSK002_regression_threshold_20260609_073514_724204 | RSK-002: REGRESSION_MAX_MAE_AU equals the approved clinical ceiling 100.0 AU | PASS | RSK-002 | 2026-06-09T14:35:14.724199 |
| RSK003_missing_xlsx_error_20260609_073514_725524 | RSK-003: ingestor raises DatasetStructureError on missing scores.xlsx | PASS | RSK-003 | 2026-06-09T14:35:14.725487 |
| RSK003_ood_hu_warning_20260609_073514_412435 | NongatedCalciumScoreTask emits OOD HU warning when mean HU is extreme | PASS | RSK-003 | 2026-06-09T14:35:14.412344 |
| RSK004_log1p_finite_20260609_073514_727747 | RSK-004: log1p target is finite for zero, large, and negative inputs | PASS | RSK-004 | 2026-06-09T14:35:14.727306 |
| SYS001_volume_sorted_by_z_20260609_073512_067401 | Volume slices are sorted by Z position | PASS | SYS-001 | 2026-06-09T14:35:12.066369 |
| SYS002_DAT011_split_generates_partitions_20260609_073512_319207 | Deterministic holdout split — three-partition generation | PASS | DAT-011, SYS-002 | 2026-06-09T14:35:12.319145 |
| SYS002_split_reproducibility_20260609_073512_320048 | Deterministic holdout split — seed reproducibility | PASS | SYS-002 | 2026-06-09T14:35:12.319963 |
| SYS003_traceability_matrix_generation_20260609_073514_661843 | Traceable verification — traceability matrix generation | PASS | SYS-003 | 2026-06-09T14:35:14.601848 |
| SYS004_coronary_calcium_task_is_instantiable_20260609_073514_744368 | SYS-004: CoronaryCalciumTask can be instantiated without error | PASS | SYS-004 | 2026-06-09T14:35:14.744362 |
| SYS005_coca_gated_ingestor_subclasses_base_ingestor_20260609_073514_745161 | SYS-005: COCAGatedIngestor subclasses BaseIngestor | PASS | SYS-005 | 2026-06-09T14:35:14.745155 |
| SYS006_task_encapsulation_20260609_073514_740862 | Dataset task encapsulation — project-level ownership | PASS | SYS-006 | 2026-06-09T14:35:14.740854 |
| SYS007_intended_use_20260609_073514_745949 | Intended use — advisory, radiologist-facing | PASS | SYS-007 | 2026-06-09T14:35:14.745944 |
| TRN001_initialization_determinism_20260609_073512_360097 | Controlled model initialization — seed determinism | PASS | TRN-001 | 2026-06-09T14:35:12.348918 |
| TRN002_training_artifact_generation_20260609_073513_365167 | Training artifact generation | PASS | TRN-002 | 2026-06-09T14:35:12.361828 |
| TRN003_compute_loss_finite_scalar_20260609_073512_313032 | CoronaryCalciumTask compute_loss returns finite scalar | PASS | TRN-003 | 2026-06-09T14:35:12.312493 |
| TRN003_loss_penalises_wrong_predictions_20260609_073512_317200 | CoronaryCalciumTask loss ordering: wrong > correct | PASS | TRN-003 | 2026-06-09T14:35:12.316856 |
| TRN003_loss_perfect_prediction_20260609_073512_316053 | CoronaryCalciumTask combined loss near zero on perfect prediction | PASS | TRN-003 | 2026-06-09T14:35:12.315877 |
| TRN003_nongated_gradient_flow_20260609_073514_411500 | NongatedCalciumScoreTask gradient flow | PASS | TRN-003 | 2026-06-09T14:35:14.411346 |
| TRN004_model_retraining_20260609_073513_506012 | Coronary model retraining capability | PASS | TRN-004 | 2026-06-09T14:35:13.366967 |
| TRN005_dataset_training_interface_20260609_073512_347447 | Coronary dataset training interface | PASS | TRN-005 | 2026-06-09T14:35:12.322973 |
| TSK001_task_definition_interface_20260609_073514_741822 | Task definition interface — toolkit contract | PASS | TSK-001 | 2026-06-09T14:35:14.741810 |
| TSK001_task_yields_one_sample_per_slice_20260609_073512_308906 | TSK-001: CoronaryCalciumTask yields one sample per CT slice | PASS | TSK-001 | 2026-06-09T14:35:12.308514 |
| TSK002_ignore_short_contours_20260609_073512_311662 | CoronaryCalciumTask ignores contours with fewer than 3 points | PASS | TSK-002 | 2026-06-09T14:35:12.311612 |
| TSK002_task_input_hu_normalised_20260609_073512_314200 | TSK-002: CoronaryCalciumTask normalises input HU values to [-1, +1] range | PASS | TSK-002 | 2026-06-09T14:35:12.314063 |
| TSK002_task_yields_masks_for_annotated_slices_20260609_073512_309891 | TSK-002: CoronaryCalciumTask input/target shapes are (1,1,H,W); unannotated slices get zero target | PASS | TSK-002 | 2026-06-09T14:35:12.309729 |
| TSK003_task_determinism_20260609_073514_743303 | Task determinism — identical inputs produce identical outputs | PASS | TSK-003 | 2026-06-09T14:35:14.742780 |
| TSK004_task_applies_cardiac_hu_window_20260609_073512_315085 | TSK-004: CoronaryCalciumTask applies the cardiac HU window [-160, 240] | PASS | TSK-004 | 2026-06-09T14:35:12.315012 |
| TSK005_hu_above_window_20260609_073514_407229 | NongatedCalciumScoreTask HU window — above | PASS | TSK-004, TSK-005 | 2026-06-09T14:35:14.407177 |
| TSK005_hu_below_window_20260609_073514_406377 | NongatedCalciumScoreTask HU window — below | PASS | TSK-004, TSK-005 | 2026-06-09T14:35:14.406320 |
| TSK005_input_tensor_shape_20260609_073514_401081 | NongatedCalciumScoreTask input tensor shape is (1,1,H,W) | PASS | TSK-005 | 2026-06-09T14:35:14.401021 |
| TSK005_log1p_target_20260609_073514_402793 | NongatedCalciumScoreTask target log1p transform | PASS | TSK-005 | 2026-06-09T14:35:14.402692 |
| TSK005_loss_finite_scalar_20260609_073514_408934 | NongatedCalciumScoreTask MSE loss is finite | PASS | TRN-003, TSK-005 | 2026-06-09T14:35:14.408820 |
| TSK005_loss_higher_for_wrong_20260609_073514_410614 | NongatedCalciumScoreTask MSE loss is monotone in error magnitude | PASS | TSK-005 | 2026-06-09T14:35:14.410556 |
| TSK005_loss_zero_on_perfect_20260609_073514_409794 | NongatedCalciumScoreTask MSE loss near zero on perfect prediction | PASS | TSK-005 | 2026-06-09T14:35:14.409746 |
| TSK005_missing_metadata_zero_score_20260609_073514_405498 | NongatedCalciumScoreTask missing metadata defaults to zero score | PASS | TSK-005 | 2026-06-09T14:35:14.405419 |
| TSK005_target_tensor_shape_20260609_073514_401927 | NongatedCalciumScoreTask target tensor shape is (4,) | PASS | TSK-005 | 2026-06-09T14:35:14.401857 |
| TSK005_wl40_maps_to_zero_20260609_073514_408077 | NongatedCalciumScoreTask WL=40 HU normalises to 0.0 | PASS | TSK-005 | 2026-06-09T14:35:14.408023 |
| TSK005_yields_one_per_slice_20260609_073514_400204 | NongatedCalciumScoreTask yields one sample per slice | PASS | TSK-005 | 2026-06-09T14:35:14.400034 |
| TSK005_zero_score_target_20260609_073514_404517 | NongatedCalciumScoreTask zero-calcium patient yields zero target | PASS | TSK-005 | 2026-06-09T14:35:14.404438 |
| TSK006_gated_broadcast_20260609_073512_318195 | CoronaryCalciumTask broadcast design — every slice receives a target mask | PASS | TSK-006 | 2026-06-09T14:35:12.318025 |
| TSK006_nongated_broadcast_20260609_073514_403631 | NongatedCalciumScoreTask — patient label broadcast to every slice | PASS | TSK-005, TSK-006 | 2026-06-09T14:35:14.403539 |
| VER001_test_suite_existence_20260609_073514_598126 | Automated verification execution — test suite existence | PASS | VER-001 | 2026-06-09T14:35:14.597869 |
| VER002_evidence_capture_20260609_073514_599993 | Evidence capture — auto_save produces loadable JSON | PASS | VER-002 | 2026-06-09T14:35:14.599527 |
| VER003_model_performance_verification_20260609_073514_601038 | Model performance verification — segmentation metrics | PASS | VER-003 | 2026-06-09T14:35:14.600816 |
| tests/test_coca_ingestor_contract.py::test_graceful_failure_on_missing_data | COCA Ingestor → Missing Dataset Failure Mode | PASS | DAT-005 | 2026-06-09T14:35:12.078735 |
| dat002_list_patient_ids_sorted_numerically_20260609_073512_286482 | DAT-002: list_patient_ids returns patient ids in numeric sort order | PASS | DAT-002 | 2026-06-09T14:35:12.279175 |
| dat004_get_sample_generates_image_and_mask_20260609_073512_142905 | DAT-004: get_sample returns (image, mask) arrays with non-zero mask for annotated patient | PASS | DAT-004 | 2026-06-09T14:35:12.141590 |
| dat004_get_sample_multiple_rois_same_slice_20260609_073512_150444 | DAT-004: multiple ROIs on the same slice are merged into one mask | PASS | DAT-004 | 2026-06-09T14:35:12.149117 |
| dat004_get_sample_no_annotations_returns_empty_20260609_073512_147673 | DAT-004: get_sample returns empty arrays when patient has no annotations | PASS | DAT-004 | 2026-06-09T14:35:12.146738 |
| dat004_ingest_dataset_multiple_patients_20260609_073512_132858 | DAT-004: ingest_dataset loads all patients from the dataset | PASS | DAT-004 | 2026-06-09T14:35:12.131512 |
| dat004_nongated_annotations_always_none_20260609_073512_259181 | DAT-004: nongated ingestor always returns None for vector_rois (score-only dataset) | PASS | DAT-004 | 2026-06-09T14:35:12.251730 |
| dat004_nongated_hounsfield_rescale_applied_20260609_073512_250095 | DAT-004: RescaleSlope and RescaleIntercept are applied to nongated CT pixel values | PASS | DAT-004 | 2026-06-09T14:35:12.242445 |
| dat005_missing_dicom_files_20260609_073512_126077 | DAT-005: patient series dir with no DICOM files raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T14:35:12.125788 |
| dat006_get_sample_returns_single_slice_20260609_073512_145264 | DAT-006: get_sample returns exactly one image/mask pair for a single-slice annotated patient | PASS | DAT-006 | 2026-06-09T14:35:12.144173 |
| dat006_get_volume_api_20260609_073512_130065 | DAT-006: load_patient_sample returns a volume with expected shape | PASS | DAT-006 | 2026-06-09T14:35:12.129276 |
| dat006_lazy_patient_loading_20260609_073512_120153 | DAT-006: COCAGatedIngestor loads each patient volume exactly once | PASS | DAT-006 | 2026-06-09T14:35:12.119437 |
| dat007_get_sample_skips_invalid_slice_annotations_20260609_073512_152740 | DAT-007: annotation with out-of-bounds ImageIndex is skipped; get_sample returns empty arrays | PASS | DAT-007 | 2026-06-09T14:35:12.151833 |
| dat007_slice_index_out_of_bounds_20260609_073512_122239 | DAT-007: annotation referencing out-of-bounds slice is silently ignored | PASS | DAT-007 | 2026-06-09T14:35:12.121477 |
| dat008_deterministic_slice_retrieval_20260609_073512_124555 | DAT-008: loading the same patient twice returns identical slice data | PASS | DAT-008 | 2026-06-09T14:35:12.123590 |
| dat009_annotation_missing_image_index_20260609_073512_137409 | DAT-009: annotation entry missing ImageIndex is treated as no annotation | PASS | DAT-009 | 2026-06-09T14:35:12.136394 |
| dat011_ingest_dataset_enumerates_patient_ids_20260609_073512_135011 | DAT-011: ingest_dataset enumerates all patient IDs without loading volumes | PASS | DAT-011 | 2026-06-09T14:35:12.134213 |
| dat015_empty_dataset_root_raises_20260609_073512_165992 | DAT-015: list_patient_ids raises when root has no patient directories | PASS | DAT-015 | 2026-06-09T14:35:12.155962 |
| dat015_missing_image_position_skipped_20260609_073512_268640 | DAT-015: DICOMs missing ImagePositionPatient are skipped; remaining slices still loaded | PASS | DAT-015 | 2026-06-09T14:35:12.260720 |
| dat015_missing_patient_directory_raises_20260609_073512_175115 | DAT-015: load_patient_sample raises for non-existent patient directory | PASS | DAT-015 | 2026-06-09T14:35:12.167474 |
| dat015_no_dicom_files_raises_20260609_073512_184768 | DAT-015: load_patient_sample raises when patient dir has no .dcm files | PASS | DAT-015 | 2026-06-09T14:35:12.176911 |
| dat015_spacing_fallback_on_missing_metadata_20260609_073512_277670 | DAT-015: missing PixelSpacing metadata falls back to (1,1,1) without raising | PASS | DAT-015 | 2026-06-09T14:35:12.270199 |
| dat016_blank_score_cell_treated_as_zero_20260609_073512_231519 | DAT-016: blank/None score cells in xlsx are coerced to 0.0 | PASS | DAT-016 | 2026-06-09T14:35:12.224272 |
| dat016_get_sample_volume_and_score_array_20260609_073512_295527 | DAT-016: get_sample returns numpy volume and score array with shape (4,) | PASS | DAT-016 | 2026-06-09T14:35:12.287902 |
| dat016_missing_score_entry_zero_fill_20260609_073512_213486 | DAT-016: patient absent from scores.xlsx gets zero-filled scores | PASS | DAT-016 | 2026-06-09T14:35:12.205221 |
| dat016_missing_score_warns_20260609_073512_222845 | DAT-016: missing score entry produces a warning on the ingestor report | PASS | DAT-016 | 2026-06-09T14:35:12.215149 |
| rsk003_ood_guard_20260609_073514_726499 | OOD guard test | PASS | RSK-003 | 2026-06-09T14:35:14.726313 |
| tests/test_project_structure.py::test_soup_inventory_complete | SOUP Inventory → All Dependencies Declared | PASS | DOC-001 | 2026-06-09T14:35:14.467497 |
| tests/test_coca_ingestor_synthetic.py::test_annotation_out_of_bounds_raises | COCA Gated Ingestor → Annotation Bounds Validation | PASS | DAT-004 | 2026-06-09T14:35:12.116023 |
| tests/test_coca_ingestor_synthetic.py::test_hounsfield_rescale_applied | COCA Gated Ingestor → HU Rescale | PASS | DAT-004 | 2026-06-09T14:35:12.113994 |
| tests/test_coca_ingestor_synthetic.py::test_slices_sorted_by_z | COCA Gated Ingestor → Slice Sorting | PASS | DAT-004 | 2026-06-09T14:35:12.111555 |
<!-- DHF_EVIDENCE_INDEX_END -->

## Artifact Locations

| Repository | Path |
|------------|------|
| <!-- DHF_VAR:CODE_REPO -->Coronary_prj, medical_image_ai_toolkit, regulatory_tools<!-- /DHF_VAR:CODE_REPO --> | `artifacts/evidence_runs/{YYYYMMDD_HHMMSS}/` |

*For real-time evidence, check CI workflow artifacts.*
