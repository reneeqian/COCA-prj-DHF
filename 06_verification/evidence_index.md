# Verification Evidence Index — <!-- DHF_VAR:PROJECT_NAME -->COCA-prj<!-- /DHF_VAR:PROJECT_NAME -->

Evidence reports are stored as JSON artifacts in `artifacts/evidence_runs/` in each code
repository. CI uploads them as workflow artifacts.

## Evidence Summary

| Repository | Latest CI Run | Grade |
|------------|--------------|-------|
| <!-- DHF_VAR:CODE_REPO -->Coronary_prj, medical_image_ai_toolkit, regulatory_tools<!-- /DHF_VAR:CODE_REPO --> | {{CI_RUN}} | — |

## Evidence Artifacts

<!-- DHF_EVIDENCE_INDEX_START -->
*Latest run: `20260521_120853`*

| Test ID | Subject | Result | Requirements | Timestamp |
|---------|---------|--------|--------------|-----------|
| DAT001_dataset_structure_validation_20260521_120853_321122 | DAT-001: missing patient/ directory raises DatasetStructureError | PASS | DAT-001 | 2026-05-21T19:08:53.321101 |
| DAT001_missing_patient_root_20260521_120853_298934 | Missing patient root raises DatasetStructureError | PASS | DAT-001 | 2026-05-21T19:08:53.298911 |
| DAT001_no_patient_directories_20260521_120853_318318 | Empty patient root raises DatasetStructureError | PASS | DAT-001 | 2026-05-21T19:08:53.318025 |
| DAT002_slice_determinism_20260521_120853_320168 | Repeated slice retrieval produces identical arrays | PASS | DAT-002 | 2026-05-21T19:08:53.319318 |
| DAT003_invalid_patient_id_20260521_120853_328297 | DAT-003: patient directory with no DICOM series raises DatasetStructureError | PASS | DAT-003 | 2026-05-21T19:08:53.328025 |
| DAT004_get_slice_success_20260521_120853_315088 | Slice retrieved with correct HU conversion | PASS | DAT-004 | 2026-05-21T19:08:53.314516 |
| DAT004_missing_image_position_20260521_120853_313679 | DICOM missing ImagePositionPatient raises DatasetStructureError | PASS | DAT-004 | 2026-05-21T19:08:53.313139 |
| DAT004_nongated_z_sort_20260521_120853_428772 | COCANongatedIngestor Z-sort | PASS | DAT-004 | 2026-05-21T19:08:53.422091 |
| DAT004_skip_dicom_without_position_20260521_120853_481609 | DAT-004: DICOMs missing ImagePositionPatient are skipped with a warning | PASS | DAT-004 | 2026-05-21T19:08:53.480649 |
| DAT005_annotation_xml_parse_failure_20260521_120853_305571 | Malformed annotation XML raises DatasetStructureError | PASS | DAT-005 | 2026-05-21T19:08:53.304756 |
| DAT005_invalid_dicom_file_20260521_120853_307214 | Invalid DICOM file raises DatasetStructureError | PASS | DAT-005 | 2026-05-21T19:08:53.306554 |
| DAT005_missing_image_position_patient_20260521_120853_303707 | DICOM missing ImagePositionPatient raises DatasetStructureError | PASS | DAT-005 | 2026-05-21T19:08:53.302917 |
| DAT005_no_dicom_files_20260521_120853_317174 | Series with no DICOM files raises DatasetStructureError | PASS | DAT-005 | 2026-05-21T19:08:53.316914 |
| DAT005_no_series_directories_20260521_120853_316095 | Patient with no series directories raises DatasetStructureError | PASS | DAT-005 | 2026-05-21T19:08:53.315937 |
| DAT005_patient_without_series_20260521_120853_300072 | Patient directory without series raises DatasetStructureError | PASS | DAT-005 | 2026-05-21T19:08:53.299762 |
| DAT005_series_without_dicoms_20260521_120853_301858 | Series directory with no DICOM files raises DatasetStructureError | PASS | DAT-005 | 2026-05-21T19:08:53.301525 |
| DAT006_get_patient_api_20260521_120853_338056 | DAT-006: load_patient_sample returns PatientSample with correct patient_id | PASS | DAT-006 | 2026-05-21T19:08:53.337013 |
| DAT007_annotation_slice_out_of_bounds_20260521_120853_309144 | Annotation slice index outside volume is ignored | PASS | DAT-007 | 2026-05-21T19:08:53.308285 |
| DAT008_nongated_deterministic_loading_20260521_120853_479368 | DAT-008: loading the same nongated patient twice returns identical volumes | PASS | DAT-008 | 2026-05-21T19:08:53.473401 |
| DAT009_invalid_polygon_skipped_20260521_120853_283612 | ROI with <3 points is skipped | PASS | DAT-009 | 2026-05-21T19:08:53.282600 |
| DAT009_roi_insufficient_points_ignored_20260521_120853_310816 | ROI with fewer than 3 points is ignored | PASS | DAT-009 | 2026-05-21T19:08:53.310042 |
| DAT009_valid_annotation_geometry_20260521_120853_280681 | Valid annotation geometry: polygon shape and dtype | PASS | DAT-009 | 2026-05-21T19:08:53.278226 |
| DAT010_dataset_without_annotations_20260521_120853_312274 | Dataset with no annotation files returns empty annotations | PASS | DAT-010 | 2026-05-21T19:08:53.311646 |
| DAT010_missing_annotation_file_empty_20260521_120853_285088 | Missing annotation file returns empty annotations | PASS | DAT-010 | 2026-05-21T19:08:53.284512 |
| DAT011_datasource_partition_assignment_20260521_120853_528227 | Datasource partition generation | PASS | DAT-011 | 2026-05-21T19:08:53.528182 |
| DAT012_ct_volume_sorted_by_z_20260521_120853_348511 | DAT-012: CT volume slices are sorted by Z position | PASS | DAT-012 | 2026-05-21T19:08:53.347494 |
| DAT013_contour_rasterization_20260521_120853_288163 | Annotation rasterization — polygon to mask | PASS | DAT-013 | 2026-05-21T19:08:53.287500 |
| DAT013_mask_dimension_alignment_20260521_120853_289204 | Annotation rasterization — mask shape matches source | PASS | DAT-013 | 2026-05-21T19:08:53.289002 |
| DAT013_task_rasterizes_contour_to_nonzero_mask_20260521_120853_500379 | DAT-013: CoronaryCalciumTask rasterizes contour annotations to non-zero binary mask | PASS | DAT-013 | 2026-05-21T19:08:53.500197 |
| DAT014_domain_safe_ingestion_errors_20260521_120853_290840 | Domain-safe ingestion errors — DatasetStructureError | PASS | DAT-014 | 2026-05-21T19:08:53.290327 |
| DAT014_missing_patient_directory_20260521_120853_291819 | Domain-safe ingestion errors — missing patient directory | PASS | DAT-014 | 2026-05-21T19:08:53.291797 |
| DAT015_scores_file_not_found_20260521_120853_360254 | DAT-015: missing scores.xlsx raises DatasetStructureError | PASS | DAT-015 | 2026-05-21T19:08:53.360055 |
| DAT016_scores_attached_20260521_120853_397461 | COCANongatedIngestor score loading | PASS | DAT-016 | 2026-05-21T19:08:53.391321 |
| DOC001_readme_exists_with_heading_20260521_120855_497720 | DOC-001: README.md exists and contains at least one Markdown heading | PASS | DOC-001 | 2026-05-21T19:08:55.497420 |
| DOC002_requirements_yaml_valid_structure_20260521_120855_496716 | DOC-002: requirements.yaml exists and has required structure | PASS | DOC-002 | 2026-05-21T19:08:55.478449 |
| DOC003_traceability_matrix_row_schema_20260521_120855_651947 | Traceability matrix row schema — requirement_id field present in every row | PASS | DOC-003 | 2026-05-21T19:08:55.627561 |
| INF001_inference_capability_20260521_120855_331048 | Inference capability on new data | PASS | INF-001 | 2026-05-21T19:08:55.327323 |
| INF002_inference_determinism_20260521_120855_336479 | Inference determinism — identical inputs produce identical outputs | PASS | INF-002 | 2026-05-21T19:08:55.332192 |
| MOD001_small_cnn_output_shape_20260521_120855_339025 | SmallSegmentationCNN output shape | PASS | MOD-001 | 2026-05-21T19:08:55.337706 |
| MOD001_unet2d_configurable_channels_20260521_120855_359822 | UNet2D base_channels configuration | PASS | MOD-001 | 2026-05-21T19:08:55.346035 |
| MOD001_unet2d_finite_outputs_20260521_120855_366418 | UNet2D outputs are finite on random input | PASS | MOD-001 | 2026-05-21T19:08:55.360939 |
| MOD001_unet2d_gradient_flow_20260521_120855_378469 | UNet2D gradient flow verification | PASS | MOD-001 | 2026-05-21T19:08:55.367646 |
| MOD001_unet2d_output_shape_20260521_120855_344810 | UNet2D output shape preserves spatial dimensions | PASS | MOD-001 | 2026-05-21T19:08:55.340306 |
| MOD002_model_persistence_20260521_120854_609368 | Model artifact persistence — save and reload | PASS | MOD-002 | 2026-05-21T19:08:54.590241 |
| MOD003_model_evaluation_20260521_120855_325283 | Model evaluation capability on test partition | PASS | MOD-003 | 2026-05-21T19:08:54.610917 |
| MOD004_regressor_finite_output_20260521_120855_443498 | CalciumScoreRegressor finite outputs | PASS | MOD-004 | 2026-05-21T19:08:55.439404 |
| MOD004_regressor_gradient_flow_20260521_120855_449584 | CalciumScoreRegressor gradient flow | PASS | MOD-004 | 2026-05-21T19:08:55.444523 |
| MOD004_regressor_output_shape_20260521_120855_383837 | CalciumScoreRegressor output shape | PASS | MOD-004 | 2026-05-21T19:08:55.379649 |
| MOD004_regressor_spatial_flexibility_20260521_120855_437866 | CalciumScoreRegressor spatial size flexibility | PASS | MOD-004 | 2026-05-21T19:08:55.384792 |
| MOD005_segmentation_min_dice_20260521_120855_465617 | MOD-005: SEGMENTATION_MIN_DICE equals approved floor 0.50 | PASS | MOD-005 | 2026-05-21T19:08:55.465603 |
| MOD006_regression_max_mae_20260521_120855_466335 | MOD-006: REGRESSION_MAX_MAE_AU equals approved ceiling 100.0 AU | PASS | MOD-006 | 2026-05-21T19:08:55.466330 |
| REP001_training_report_generation_20260521_120855_502311 | Training report generation | PASS | REP-001 | 2026-05-21T19:08:55.500351 |
| REP002_visualization_support_20260521_120855_595575 | Visualization support — training curve figure | PASS | REP-002 | 2026-05-21T19:08:55.503906 |
| REP003_status_report_section_headers_20260521_120855_661874 | REP-003: status_report produces TRAINING, TUNING, and MODEL TESTING section headers | PASS | REP-003 | 2026-05-21T19:08:55.660640 |
| REP004_status_report_model_testing_section_20260521_120855_667180 | REP-004: status_report prints model testing metrics (dice, iou, precision, recall) | PASS | REP-004 | 2026-05-21T19:08:55.666742 |
| REP004_status_report_no_runs_20260521_120855_659518 | status_report handles missing artifact directories | PASS | REP-004 | 2026-05-21T19:08:55.659434 |
| REP004_status_report_training_section_20260521_120855_663704 | REP-004: status_report prints training metrics (final_loss, learning_rate) | PASS | REP-004 | 2026-05-21T19:08:55.662931 |
| REP004_status_report_tuning_section_20260521_120855_665707 | REP-004: status_report prints tuning metrics (num_trials, best_val_loss) | PASS | REP-004 | 2026-05-21T19:08:55.665209 |
| RSK001_segmentation_threshold_20260521_120855_652923 | RSK-001: SEGMENTATION_MIN_DICE equals the approved clinical floor value 0.50 | PASS | RSK-001 | 2026-05-21T19:08:55.652915 |
| RSK002_negative_score_clamped_20260521_120855_653752 | RSK-002: negative calcium scores are clamped before log1p transform | PASS | RSK-002 | 2026-05-21T19:08:55.653479 |
| RSK002_regression_threshold_20260521_120855_654336 | RSK-002: REGRESSION_MAX_MAE_AU equals the approved clinical ceiling 100.0 AU | PASS | RSK-002 | 2026-05-21T19:08:55.654333 |
| RSK003_missing_xlsx_error_20260521_120855_655442 | RSK-003: ingestor raises DatasetStructureError on missing scores.xlsx | PASS | RSK-003 | 2026-05-21T19:08:55.655411 |
| RSK004_log1p_finite_20260521_120855_657515 | RSK-004: log1p target is finite for zero, large, and negative inputs | PASS | RSK-004 | 2026-05-21T19:08:55.657026 |
| SYS001_volume_sorted_by_z_20260521_120853_286914 | Volume slices are sorted by Z position | PASS | SYS-001 | 2026-05-21T19:08:53.285942 |
| SYS002_DAT011_split_generates_partitions_20260521_120853_526464 | Deterministic holdout split — three-partition generation | PASS | DAT-011, SYS-002 | 2026-05-21T19:08:53.526416 |
| SYS002_split_reproducibility_20260521_120853_527085 | Deterministic holdout split — seed reproducibility | PASS | SYS-002 | 2026-05-21T19:08:53.527027 |
| SYS003_traceability_matrix_generation_20260521_120855_626612 | Traceable verification — traceability matrix generation | PASS | SYS-003 | 2026-05-21T19:08:55.600917 |
| SYS004_coronary_calcium_task_is_instantiable_20260521_120855_669864 | SYS-004: CoronaryCalciumTask can be instantiated without error | PASS | SYS-004 | 2026-05-21T19:08:55.669860 |
| SYS005_coca_gated_ingestor_subclasses_base_ingestor_20260521_120855_670356 | SYS-005: COCAGatedIngestor subclasses BaseIngestor | PASS | SYS-005 | 2026-05-21T19:08:55.670352 |
| SYS006_task_encapsulation_20260521_120855_667750 | Dataset task encapsulation — project-level ownership | PASS | SYS-006 | 2026-05-21T19:08:55.667744 |
| SYS007_intended_use_20260521_120855_670877 | Intended use — advisory, radiologist-facing | PASS | SYS-007 | 2026-05-21T19:08:55.670872 |
| TRN001_initialization_determinism_20260521_120853_577063 | Controlled model initialization — seed determinism | PASS | TRN-001 | 2026-05-21T19:08:53.566963 |
| TRN002_training_artifact_generation_20260521_120854_446683 | Training artifact generation | PASS | TRN-002 | 2026-05-21T19:08:53.578745 |
| TRN003_compute_loss_finite_scalar_20260521_120853_519146 | CoronaryCalciumTask compute_loss returns finite scalar | PASS | TRN-003 | 2026-05-21T19:08:53.502525 |
| TRN003_loss_penalises_wrong_predictions_20260521_120853_525174 | CoronaryCalciumTask loss ordering: wrong > correct | PASS | TRN-003 | 2026-05-21T19:08:53.524896 |
| TRN003_loss_perfect_prediction_20260521_120853_524361 | CoronaryCalciumTask combined loss near zero on perfect prediction | PASS | TRN-003 | 2026-05-21T19:08:53.522867 |
| TRN003_nongated_gradient_flow_20260521_120855_477536 | NongatedCalciumScoreTask gradient flow | PASS | TRN-003 | 2026-05-21T19:08:55.476443 |
| TRN004_model_retraining_20260521_120854_588588 | Coronary model retraining capability | PASS | TRN-004 | 2026-05-21T19:08:54.448470 |
| TRN005_dataset_training_interface_20260521_120853_565749 | Coronary dataset training interface | PASS | TRN-005 | 2026-05-21T19:08:53.529230 |
| TSK001_task_definition_interface_20260521_120855_668263 | Task definition interface — toolkit contract | PASS | TSK-001 | 2026-05-21T19:08:55.668256 |
| TSK001_task_yields_one_sample_per_slice_20260521_120853_492724 | TSK-001: CoronaryCalciumTask yields one sample per CT slice | PASS | TSK-001 | 2026-05-21T19:08:53.482203 |
| TSK002_ignore_short_contours_20260521_120853_501660 | CoronaryCalciumTask ignores contours with fewer than 3 points | PASS | TSK-002 | 2026-05-21T19:08:53.501550 |
| TSK002_task_input_hu_normalised_20260521_120853_521693 | TSK-002: CoronaryCalciumTask normalises input HU values to [-1, +1] range | PASS | TSK-002 | 2026-05-21T19:08:53.520371 |
| TSK002_task_yields_masks_for_annotated_slices_20260521_120853_499102 | TSK-002: CoronaryCalciumTask input/target shapes are (1,1,H,W); unannotated slices get zero target | PASS | TSK-002 | 2026-05-21T19:08:53.493819 |
| TSK003_task_determinism_20260521_120855_669196 | Task determinism — identical inputs produce identical outputs | PASS | TSK-003 | 2026-05-21T19:08:55.668772 |
| TSK004_task_applies_cardiac_hu_window_20260521_120853_522337 | TSK-004: CoronaryCalciumTask applies the cardiac HU window [-160, 240] | PASS | TSK-004 | 2026-05-21T19:08:53.522266 |
| TSK005_hu_above_window_20260521_120855_472797 | NongatedCalciumScoreTask HU window — above | PASS | TSK-004, TSK-005 | 2026-05-21T19:08:55.472748 |
| TSK005_hu_below_window_20260521_120855_472179 | NongatedCalciumScoreTask HU window — below | PASS | TSK-004, TSK-005 | 2026-05-21T19:08:55.472131 |
| TSK005_input_tensor_shape_20260521_120855_467654 | NongatedCalciumScoreTask input tensor shape is (1,1,H,W) | PASS | TSK-005 | 2026-05-21T19:08:55.467605 |
| TSK005_log1p_target_20260521_120855_468963 | NongatedCalciumScoreTask target log1p transform | PASS | TSK-005 | 2026-05-21T19:08:55.468759 |
| TSK005_loss_finite_scalar_20260521_120855_474708 | NongatedCalciumScoreTask MSE loss is finite | PASS | TRN-003, TSK-005 | 2026-05-21T19:08:55.474089 |
| TSK005_loss_higher_for_wrong_20260521_120855_475946 | NongatedCalciumScoreTask MSE loss is monotone in error magnitude | PASS | TSK-005 | 2026-05-21T19:08:55.475892 |
| TSK005_loss_zero_on_perfect_20260521_120855_475371 | NongatedCalciumScoreTask MSE loss near zero on perfect prediction | PASS | TSK-005 | 2026-05-21T19:08:55.475329 |
| TSK005_missing_metadata_zero_score_20260521_120855_471595 | NongatedCalciumScoreTask missing metadata defaults to zero score | PASS | TSK-005 | 2026-05-21T19:08:55.471531 |
| TSK005_target_tensor_shape_20260521_120855_468236 | NongatedCalciumScoreTask target tensor shape is (4,) | PASS | TSK-005 | 2026-05-21T19:08:55.468177 |
| TSK005_wl40_maps_to_zero_20260521_120855_473403 | NongatedCalciumScoreTask WL=40 HU normalises to 0.0 | PASS | TSK-005 | 2026-05-21T19:08:55.473344 |
| TSK005_yields_one_per_slice_20260521_120855_467071 | NongatedCalciumScoreTask yields one sample per slice | PASS | TSK-005 | 2026-05-21T19:08:55.466901 |
| TSK005_zero_score_target_20260521_120855_470930 | NongatedCalciumScoreTask zero-calcium patient yields zero target | PASS | TSK-005 | 2026-05-21T19:08:55.470787 |
| TSK006_gated_broadcast_20260521_120853_525866 | CoronaryCalciumTask broadcast design — every slice receives a target mask | PASS | TSK-006 | 2026-05-21T19:08:53.525705 |
| TSK006_nongated_broadcast_20260521_120855_469864 | NongatedCalciumScoreTask — patient label broadcast to every slice | PASS | TSK-005, TSK-006 | 2026-05-21T19:08:55.469519 |
| VER001_test_suite_existence_20260521_120855_597006 | Automated verification execution — test suite existence | PASS | VER-001 | 2026-05-21T19:08:55.596768 |
| VER002_evidence_capture_20260521_120855_598996 | Evidence capture — auto_save produces loadable JSON | PASS | VER-002 | 2026-05-21T19:08:55.598531 |
| VER003_model_performance_verification_20260521_120855_600190 | Model performance verification — segmentation metrics | PASS | VER-003 | 2026-05-21T19:08:55.599638 |
| tests/test_coca_ingestor_contract.py::test_graceful_failure_on_missing_data | COCA Ingestor → Missing Dataset Failure Mode | PASS | DAT-005 | 2026-05-21T19:08:53.296496 |
| dat002_list_patient_ids_sorted_numerically_20260521_120853_464022 | DAT-002: list_patient_ids returns patient ids in numeric sort order | PASS | DAT-002 | 2026-05-21T19:08:53.458653 |
| dat004_get_sample_generates_image_and_mask_20260521_120853_350690 | DAT-004: get_sample returns (image, mask) arrays with non-zero mask for annotated patient | PASS | DAT-004 | 2026-05-21T19:08:53.349652 |
| dat004_get_sample_multiple_rois_same_slice_20260521_120853_356867 | DAT-004: multiple ROIs on the same slice are merged into one mask | PASS | DAT-004 | 2026-05-21T19:08:53.355613 |
| dat004_get_sample_no_annotations_returns_empty_20260521_120853_354102 | DAT-004: get_sample returns empty arrays when patient has no annotations | PASS | DAT-004 | 2026-05-21T19:08:53.353543 |
| dat004_ingest_dataset_multiple_patients_20260521_120853_343002 | DAT-004: ingest_dataset loads all patients from the dataset | PASS | DAT-004 | 2026-05-21T19:08:53.341807 |
| dat004_nongated_annotations_always_none_20260521_120853_443096 | DAT-004: nongated ingestor always returns None for vector_rois (score-only dataset) | PASS | DAT-004 | 2026-05-21T19:08:53.437029 |
| dat004_nongated_hounsfield_rescale_applied_20260521_120853_435895 | DAT-004: RescaleSlope and RescaleIntercept are applied to nongated CT pixel values | PASS | DAT-004 | 2026-05-21T19:08:53.430539 |
| dat005_missing_dicom_files_20260521_120853_335908 | DAT-005: patient series dir with no DICOM files raises DatasetStructureError | PASS | DAT-005 | 2026-05-21T19:08:53.335567 |
| dat006_get_sample_returns_single_slice_20260521_120853_352627 | DAT-006: get_sample returns exactly one image/mask pair for a single-slice annotated patient | PASS | DAT-006 | 2026-05-21T19:08:53.351610 |
| dat006_get_volume_api_20260521_120853_340087 | DAT-006: load_patient_sample returns a volume with expected shape | PASS | DAT-006 | 2026-05-21T19:08:53.339280 |
| dat006_lazy_patient_loading_20260521_120853_330296 | DAT-006: COCAGatedIngestor loads each patient volume exactly once | PASS | DAT-006 | 2026-05-21T19:08:53.329476 |
| dat007_get_sample_skips_invalid_slice_annotations_20260521_120853_359079 | DAT-007: annotation with out-of-bounds ImageIndex is skipped; get_sample returns empty arrays | PASS | DAT-007 | 2026-05-21T19:08:53.357824 |
| dat007_slice_index_out_of_bounds_20260521_120853_332327 | DAT-007: annotation referencing out-of-bounds slice is silently ignored | PASS | DAT-007 | 2026-05-21T19:08:53.331540 |
| dat008_deterministic_slice_retrieval_20260521_120853_334448 | DAT-008: loading the same patient twice returns identical slice data | PASS | DAT-008 | 2026-05-21T19:08:53.333542 |
| dat009_annotation_missing_image_index_20260521_120853_346544 | DAT-009: annotation entry missing ImageIndex is treated as no annotation | PASS | DAT-009 | 2026-05-21T19:08:53.345648 |
| dat011_ingest_dataset_enumerates_patient_ids_20260521_120853_344750 | DAT-011: ingest_dataset enumerates all patient IDs without loading volumes | PASS | DAT-011 | 2026-05-21T19:08:53.344036 |
| dat015_empty_dataset_root_raises_20260521_120853_370297 | DAT-015: list_patient_ids raises when root has no patient directories | PASS | DAT-015 | 2026-05-21T19:08:53.361132 |
| dat015_missing_image_position_skipped_20260521_120853_450407 | DAT-015: DICOMs missing ImagePositionPatient are skipped; remaining slices still loaded | PASS | DAT-015 | 2026-05-21T19:08:53.444183 |
| dat015_missing_patient_directory_raises_20260521_120853_377353 | DAT-015: load_patient_sample raises for non-existent patient directory | PASS | DAT-015 | 2026-05-21T19:08:53.371703 |
| dat015_no_dicom_files_raises_20260521_120853_384065 | DAT-015: load_patient_sample raises when patient dir has no .dcm files | PASS | DAT-015 | 2026-05-21T19:08:53.378822 |
| dat015_spacing_fallback_on_missing_metadata_20260521_120853_457100 | DAT-015: missing PixelSpacing metadata falls back to (1,1,1) without raising | PASS | DAT-015 | 2026-05-21T19:08:53.451491 |
| dat016_blank_score_cell_treated_as_zero_20260521_120853_420868 | DAT-016: blank/None score cells in xlsx are coerced to 0.0 | PASS | DAT-016 | 2026-05-21T19:08:53.414918 |
| dat016_get_sample_volume_and_score_array_20260521_120853_472282 | DAT-016: get_sample returns numpy volume and score array with shape (4,) | PASS | DAT-016 | 2026-05-21T19:08:53.465218 |
| dat016_missing_score_entry_zero_fill_20260521_120853_405515 | DAT-016: patient absent from scores.xlsx gets zero-filled scores | PASS | DAT-016 | 2026-05-21T19:08:53.398546 |
| dat016_missing_score_warns_20260521_120853_413561 | DAT-016: missing score entry produces a warning on the ingestor report | PASS | DAT-016 | 2026-05-21T19:08:53.407002 |
| rsk003_ood_guard_20260521_120855_656232 | OOD guard test | PASS | RSK-003 | 2026-05-21T19:08:55.656053 |
| tests/test_project_structure.py::test_soup_inventory_complete | SOUP Inventory → All Dependencies Declared | PASS | DOC-001 | 2026-05-21T19:08:55.498744 |
| tests/test_coca_ingestor_synthetic.py::test_annotation_out_of_bounds_raises | COCA Gated Ingestor → Annotation Bounds Validation | PASS | DAT-004 | 2026-05-21T19:08:53.325904 |
| tests/test_coca_ingestor_synthetic.py::test_hounsfield_rescale_applied | COCA Gated Ingestor → HU Rescale | PASS | DAT-004 | 2026-05-21T19:08:53.323784 |
| tests/test_coca_ingestor_synthetic.py::test_slices_sorted_by_z | COCA Gated Ingestor → Slice Sorting | PASS | DAT-004 | 2026-05-21T19:08:53.321952 |
<!-- DHF_EVIDENCE_INDEX_END -->

## Artifact Locations

| Repository | Path |
|------------|------|
| <!-- DHF_VAR:CODE_REPO -->Coronary_prj, medical_image_ai_toolkit, regulatory_tools<!-- /DHF_VAR:CODE_REPO --> | `artifacts/evidence_runs/{YYYYMMDD_HHMMSS}/` |

*For real-time evidence, check CI workflow artifacts.*
