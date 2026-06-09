# Verification Evidence Index — <!-- DHF_VAR:PROJECT_NAME -->COCA-prj<!-- /DHF_VAR:PROJECT_NAME -->

Evidence reports are stored as JSON artifacts in `artifacts/evidence_runs/` in each code
repository. CI uploads them as workflow artifacts.

## Evidence Summary

| Repository | Latest CI Run | Grade |
|------------|--------------|-------|
| <!-- DHF_VAR:CODE_REPO -->Coronary_prj, medical_image_ai_toolkit, regulatory_tools<!-- /DHF_VAR:CODE_REPO --> | See evidence artifacts below (local run 20260609_073512) | — |

## Evidence Artifacts

<!-- DHF_EVIDENCE_INDEX_START -->
*Latest run: `20260609_131645`*

| Test ID | Subject | Result | Requirements | Timestamp |
|---------|---------|--------|--------------|-----------|
| DAT001_base_ingestor_abstract_methods_20260609_131645_683267 | BaseIngestor abstract method bodies raise NotImplementedError | PASS | DAT-001 | 2026-06-09T20:16:45.683252 |
| DAT001_dataset_structure_validation_20260609_131645_719884 | DAT-001: missing patient/ directory raises DatasetStructureError | PASS | DAT-001 | 2026-06-09T20:16:45.719848 |
| DAT001_list_patient_ids_os_error_20260609_131645_696071 | list_patient_ids wraps OSError into DatasetStructureError | PASS | DAT-001 | 2026-06-09T20:16:45.695914 |
| DAT001_missing_patient_root_20260609_131645_684652 | Missing patient root raises DatasetStructureError | PASS | DAT-001 | 2026-06-09T20:16:45.684617 |
| DAT001_no_patient_directories_20260609_131645_716230 | Empty patient root raises DatasetStructureError | PASS | DAT-001 | 2026-06-09T20:16:45.716107 |
| DAT002_load_unexpected_exception_20260609_131645_697657 | load_patient_sample wraps unexpected exceptions into DatasetStructureError | PASS | DAT-002 | 2026-06-09T20:16:45.697280 |
| DAT002_slice_determinism_20260609_131645_718472 | Repeated slice retrieval produces identical arrays | PASS | DAT-002 | 2026-06-09T20:16:45.717482 |
| DAT003_invalid_patient_id_20260609_131645_729183 | DAT-003: patient directory with no DICOM series raises DatasetStructureError | PASS | DAT-003 | 2026-06-09T20:16:45.728990 |
| DAT004_get_slice_success_20260609_131645_711001 | Slice retrieved with correct HU conversion | PASS | DAT-004 | 2026-06-09T20:16:45.709527 |
| DAT004_missing_image_position_20260609_131645_708159 | DICOM missing ImagePositionPatient raises DatasetStructureError | PASS | DAT-004 | 2026-06-09T20:16:45.707302 |
| DAT004_nongated_z_sort_20260609_131645_864958 | COCANongatedIngestor Z-sort | PASS | DAT-004 | 2026-06-09T20:16:45.855731 |
| DAT004_skip_dicom_without_position_20260609_131645_949016 | DAT-004: DICOMs missing ImagePositionPatient are skipped with a warning | PASS | DAT-004 | 2026-06-09T20:16:45.947823 |
| DAT005_annotation_xml_parse_failure_20260609_131645_692023 | Malformed annotation XML raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T20:16:45.690868 |
| DAT005_invalid_dicom_file_20260609_131645_694326 | Invalid DICOM file raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T20:16:45.693475 |
| DAT005_missing_image_position_patient_20260609_131645_689457 | DICOM missing ImagePositionPatient raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T20:16:45.688720 |
| DAT005_no_dicom_files_20260609_131645_714765 | Series with no DICOM files raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T20:16:45.714451 |
| DAT005_no_series_directories_20260609_131645_713067 | Patient with no series directories raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T20:16:45.712859 |
| DAT005_patient_without_series_20260609_131645_686038 | Patient directory without series raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T20:16:45.685806 |
| DAT005_series_without_dicoms_20260609_131645_687496 | Series directory with no DICOM files raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T20:16:45.687197 |
| DAT006_get_patient_api_20260609_131645_740417 | DAT-006: load_patient_sample returns PatientSample with correct patient_id | PASS | DAT-006 | 2026-06-09T20:16:45.739537 |
| DAT007_annotation_slice_out_of_bounds_20260609_131645_700136 | Annotation slice index outside volume is ignored | PASS | DAT-007 | 2026-06-09T20:16:45.698976 |
| DAT008_nongated_deterministic_loading_20260609_131645_946146 | DAT-008: loading the same nongated patient twice returns identical volumes | PASS | DAT-008 | 2026-06-09T20:16:45.937447 |
| DAT009_invalid_polygon_skipped_20260609_131645_661517 | ROI with <3 points is skipped | PASS | DAT-009 | 2026-06-09T20:16:45.660151 |
| DAT009_roi_insufficient_points_ignored_20260609_131645_703286 | ROI with fewer than 3 points is ignored | PASS | DAT-009 | 2026-06-09T20:16:45.701901 |
| DAT009_valid_annotation_geometry_20260609_131645_658243 | Valid annotation geometry: polygon shape and dtype | PASS | DAT-009 | 2026-06-09T20:16:45.656028 |
| DAT010_dataset_without_annotations_20260609_131645_705625 | Dataset with no annotation files returns empty annotations | PASS | DAT-010 | 2026-06-09T20:16:45.704807 |
| DAT010_missing_annotation_file_empty_20260609_131645_664085 | Missing annotation file returns empty annotations | PASS | DAT-010 | 2026-06-09T20:16:45.663160 |
| DAT011_datasource_partition_assignment_20260609_131645_992291 | Datasource partition generation | PASS | DAT-011 | 2026-06-09T20:16:45.992235 |
| DAT012_ct_volume_sorted_by_z_20260609_131645_754030 | DAT-012: CT volume slices are sorted by Z position | PASS | DAT-012 | 2026-06-09T20:16:45.752552 |
| DAT013_contour_rasterization_20260609_131645_668743 | Annotation rasterization — polygon to mask | PASS | DAT-013 | 2026-06-09T20:16:45.668052 |
| DAT013_mask_dimension_alignment_20260609_131645_669920 | Annotation rasterization — mask shape matches source | PASS | DAT-013 | 2026-06-09T20:16:45.669724 |
| DAT013_task_rasterizes_contour_to_nonzero_mask_20260609_131645_963415 | DAT-013: CoronaryCalciumTask rasterizes contour annotations to non-zero binary mask | PASS | DAT-013 | 2026-06-09T20:16:45.963225 |
| DAT014_domain_safe_ingestion_errors_20260609_131645_671766 | Domain-safe ingestion errors — DatasetStructureError | PASS | DAT-014 | 2026-06-09T20:16:45.671247 |
| DAT014_missing_patient_directory_20260609_131645_673031 | Domain-safe ingestion errors — missing patient directory | PASS | DAT-014 | 2026-06-09T20:16:45.672993 |
| DAT015_scores_file_not_found_20260609_131645_769434 | DAT-015: missing scores.xlsx raises DatasetStructureError | PASS | DAT-015 | 2026-06-09T20:16:45.769197 |
| DAT016_scores_attached_20260609_131645_822375 | COCANongatedIngestor score loading | PASS | DAT-016 | 2026-06-09T20:16:45.812712 |
| DOC001_readme_exists_with_heading_20260609_131648_411406 | DOC-001: README.md exists and contains at least one Markdown heading | PASS | DOC-001 | 2026-06-09T20:16:48.411195 |
| DOC002_requirements_yaml_valid_structure_20260609_131648_409921 | DOC-002: requirements.yaml exists and has required structure | PASS | DOC-002 | 2026-06-09T20:16:48.358238 |
| DOC003_traceability_matrix_row_schema_20260609_131648_685763 | Traceability matrix row schema — requirement_id field present in every row | PASS | DOC-003 | 2026-06-09T20:16:48.623396 |
| INF001_inference_capability_20260609_131648_168697 | Inference capability on new data | PASS | INF-001 | 2026-06-09T20:16:48.163664 |
| INF002_inference_determinism_20260609_131648_176180 | Inference determinism — identical inputs produce identical outputs | PASS | INF-002 | 2026-06-09T20:16:48.169934 |
| MOD001_small_cnn_output_shape_20260609_131648_178991 | SmallSegmentationCNN output shape | PASS | MOD-001 | 2026-06-09T20:16:48.177629 |
| MOD001_unet2d_configurable_channels_20260609_131648_204805 | UNet2D base_channels configuration | PASS | MOD-001 | 2026-06-09T20:16:48.187600 |
| MOD001_unet2d_finite_outputs_20260609_131648_213420 | UNet2D outputs are finite on random input | PASS | MOD-001 | 2026-06-09T20:16:48.206622 |
| MOD001_unet2d_gradient_flow_20260609_131648_227878 | UNet2D gradient flow verification | PASS | MOD-001 | 2026-06-09T20:16:48.214631 |
| MOD001_unet2d_output_shape_20260609_131648_186286 | UNet2D output shape preserves spatial dimensions | PASS | MOD-001 | 2026-06-09T20:16:48.180295 |
| MOD002_model_persistence_20260609_131647_395203 | Model artifact persistence — save and reload | PASS | MOD-002 | 2026-06-09T20:16:47.362284 |
| MOD003_model_evaluation_20260609_131648_162378 | Model evaluation capability on test partition | PASS | MOD-003 | 2026-06-09T20:16:47.397222 |
| MOD004_regressor_finite_output_20260609_131648_307221 | CalciumScoreRegressor finite outputs | PASS | MOD-004 | 2026-06-09T20:16:48.302744 |
| MOD004_regressor_gradient_flow_20260609_131648_315896 | CalciumScoreRegressor gradient flow | PASS | MOD-004 | 2026-06-09T20:16:48.308528 |
| MOD004_regressor_output_shape_20260609_131648_235205 | CalciumScoreRegressor output shape | PASS | MOD-004 | 2026-06-09T20:16:48.229424 |
| MOD004_regressor_spatial_flexibility_20260609_131648_301093 | CalciumScoreRegressor spatial size flexibility | PASS | MOD-004 | 2026-06-09T20:16:48.236491 |
| MOD005_segmentation_min_dice_20260609_131648_336307 | MOD-005: SEGMENTATION_MIN_DICE equals approved floor 0.50 | PASS | MOD-005 | 2026-06-09T20:16:48.336293 |
| MOD006_regression_max_mae_20260609_131648_337246 | MOD-006: REGRESSION_MAX_MAE_AU equals approved ceiling 100.0 AU | PASS | MOD-006 | 2026-06-09T20:16:48.337240 |
| REP001_training_report_generation_20260609_131648_417595 | Training report generation | PASS | REP-001 | 2026-06-09T20:16:48.415206 |
| REP002_visualization_support_20260609_131648_549494 | Visualization support — training curve figure | PASS | REP-002 | 2026-06-09T20:16:48.419221 |
| REP003_status_report_section_headers_20260609_131648_698681 | REP-003: status_report produces TRAINING, TUNING, and MODEL TESTING section headers | PASS | REP-003 | 2026-06-09T20:16:48.697217 |
| REP004_status_report_model_testing_section_20260609_131648_705832 | REP-004: status_report prints model testing metrics (dice, iou, precision, recall) | PASS | REP-004 | 2026-06-09T20:16:48.705214 |
| REP004_status_report_no_runs_20260609_131648_695745 | status_report handles missing artifact directories | PASS | REP-004 | 2026-06-09T20:16:48.695608 |
| REP004_status_report_training_section_20260609_131648_700848 | REP-004: status_report prints training metrics (final_loss, learning_rate) | PASS | REP-004 | 2026-06-09T20:16:48.700196 |
| REP004_status_report_tuning_section_20260609_131648_703436 | REP-004: status_report prints tuning metrics (num_trials, best_val_loss) | PASS | REP-004 | 2026-06-09T20:16:48.702702 |
| RSK001_segmentation_threshold_20260609_131648_687174 | RSK-001: SEGMENTATION_MIN_DICE equals the approved clinical floor value 0.50 | PASS | RSK-001 | 2026-06-09T20:16:48.687161 |
| RSK002_negative_score_clamped_20260609_131648_688568 | RSK-002: negative calcium scores are clamped before log1p transform | PASS | RSK-002 | 2026-06-09T20:16:48.688271 |
| RSK002_regression_threshold_20260609_131648_689527 | RSK-002: REGRESSION_MAX_MAE_AU equals the approved clinical ceiling 100.0 AU | PASS | RSK-002 | 2026-06-09T20:16:48.689522 |
| RSK003_missing_xlsx_error_20260609_131648_691015 | RSK-003: ingestor raises DatasetStructureError on missing scores.xlsx | PASS | RSK-003 | 2026-06-09T20:16:48.690973 |
| RSK003_ood_hu_warning_20260609_131648_357165 | NongatedCalciumScoreTask emits OOD HU warning when mean HU is extreme | PASS | RSK-003 | 2026-06-09T20:16:48.357053 |
| RSK004_log1p_finite_20260609_131648_693612 | RSK-004: log1p target is finite for zero, large, and negative inputs | PASS | RSK-004 | 2026-06-09T20:16:48.693107 |
| SYS001_volume_sorted_by_z_20260609_131645_666729 | Volume slices are sorted by Z position | PASS | SYS-001 | 2026-06-09T20:16:45.665377 |
| SYS002_DAT011_split_generates_partitions_20260609_131645_989589 | Deterministic holdout split — three-partition generation | PASS | DAT-011, SYS-002 | 2026-06-09T20:16:45.989527 |
| SYS002_split_reproducibility_20260609_131645_990714 | Deterministic holdout split — seed reproducibility | PASS | SYS-002 | 2026-06-09T20:16:45.990622 |
| SYS003_traceability_matrix_generation_20260609_131648_622019 | Traceable verification — traceability matrix generation | PASS | SYS-003 | 2026-06-09T20:16:48.556041 |
| SYS004_coronary_calcium_task_is_instantiable_20260609_131648_710456 | SYS-004: CoronaryCalciumTask can be instantiated without error | PASS | SYS-004 | 2026-06-09T20:16:48.710447 |
| SYS005_coca_gated_ingestor_subclasses_base_ingestor_20260609_131648_711378 | SYS-005: COCAGatedIngestor subclasses BaseIngestor | PASS | SYS-005 | 2026-06-09T20:16:48.711371 |
| SYS006_task_encapsulation_20260609_131648_706844 | Dataset task encapsulation — project-level ownership | PASS | SYS-006 | 2026-06-09T20:16:48.706837 |
| SYS007_intended_use_20260609_131648_712217 | Intended use — advisory, radiologist-facing | PASS | SYS-007 | 2026-06-09T20:16:48.712212 |
| TRN001_initialization_determinism_20260609_131646_048945 | Controlled model initialization — seed determinism | PASS | TRN-001 | 2026-06-09T20:16:46.036124 |
| TRN002_training_artifact_generation_20260609_131647_204821 | Training artifact generation | PASS | TRN-002 | 2026-06-09T20:16:46.050683 |
| TRN003_compute_loss_finite_scalar_20260609_131645_978559 | CoronaryCalciumTask compute_loss returns finite scalar | PASS | TRN-003 | 2026-06-09T20:16:45.965331 |
| TRN003_loss_penalises_wrong_predictions_20260609_131645_987457 | CoronaryCalciumTask loss ordering: wrong > correct | PASS | TRN-003 | 2026-06-09T20:16:45.987202 |
| TRN003_loss_perfect_prediction_20260609_131645_986124 | CoronaryCalciumTask combined loss near zero on perfect prediction | PASS | TRN-003 | 2026-06-09T20:16:45.985112 |
| TRN003_nongated_gradient_flow_20260609_131648_355847 | NongatedCalciumScoreTask gradient flow | PASS | TRN-003 | 2026-06-09T20:16:48.354159 |
| TRN004_model_retraining_20260609_131647_360224 | Coronary model retraining capability | PASS | TRN-004 | 2026-06-09T20:16:47.206757 |
| TRN005_dataset_training_interface_20260609_131646_034838 | Coronary dataset training interface | PASS | TRN-005 | 2026-06-09T20:16:45.993670 |
| TSK001_task_definition_interface_20260609_131648_707668 | Task definition interface — toolkit contract | PASS | TSK-001 | 2026-06-09T20:16:48.707655 |
| TSK001_task_yields_one_sample_per_slice_20260609_131645_958000 | TSK-001: CoronaryCalciumTask yields one sample per CT slice | PASS | TSK-001 | 2026-06-09T20:16:45.949942 |
| TSK002_ignore_short_contours_20260609_131645_964341 | CoronaryCalciumTask ignores contours with fewer than 3 points | PASS | TSK-002 | 2026-06-09T20:16:45.964282 |
| TSK002_task_input_hu_normalised_20260609_131645_982837 | TSK-002: CoronaryCalciumTask normalises input HU values to [-1, +1] range | PASS | TSK-002 | 2026-06-09T20:16:45.979781 |
| TSK002_task_yields_masks_for_annotated_slices_20260609_131645_962062 | TSK-002: CoronaryCalciumTask input/target shapes are (1,1,H,W); unannotated slices get zero target | PASS | TSK-002 | 2026-06-09T20:16:45.959214 |
| TSK003_task_determinism_20260609_131648_709024 | Task determinism — identical inputs produce identical outputs | PASS | TSK-003 | 2026-06-09T20:16:48.708514 |
| TSK004_task_applies_cardiac_hu_window_20260609_131645_983934 | TSK-004: CoronaryCalciumTask applies the cardiac HU window [-160, 240] | PASS | TSK-004 | 2026-06-09T20:16:45.983825 |
| TSK005_hu_above_window_20260609_131648_348111 | NongatedCalciumScoreTask HU window — above | PASS | TSK-004, TSK-005 | 2026-06-09T20:16:48.348061 |
| TSK005_hu_below_window_20260609_131648_347233 | NongatedCalciumScoreTask HU window — below | PASS | TSK-004, TSK-005 | 2026-06-09T20:16:48.347176 |
| TSK005_input_tensor_shape_20260609_131648_339214 | NongatedCalciumScoreTask input tensor shape is (1,1,H,W) | PASS | TSK-005 | 2026-06-09T20:16:48.339144 |
| TSK005_log1p_target_20260609_131648_342543 | NongatedCalciumScoreTask target log1p transform | PASS | TSK-005 | 2026-06-09T20:16:48.341585 |
| TSK005_loss_finite_scalar_20260609_131648_351027 | NongatedCalciumScoreTask MSE loss is finite | PASS | TRN-003, TSK-005 | 2026-06-09T20:16:48.350094 |
| TSK005_loss_higher_for_wrong_20260609_131648_353353 | NongatedCalciumScoreTask MSE loss is monotone in error magnitude | PASS | TSK-005 | 2026-06-09T20:16:48.353277 |
| TSK005_loss_zero_on_perfect_20260609_131648_352377 | NongatedCalciumScoreTask MSE loss near zero on perfect prediction | PASS | TSK-005 | 2026-06-09T20:16:48.352288 |
| TSK005_missing_metadata_zero_score_20260609_131648_346318 | NongatedCalciumScoreTask missing metadata defaults to zero score | PASS | TSK-005 | 2026-06-09T20:16:48.346241 |
| TSK005_target_tensor_shape_20260609_131648_340507 | NongatedCalciumScoreTask target tensor shape is (4,) | PASS | TSK-005 | 2026-06-09T20:16:48.340269 |
| TSK005_wl40_maps_to_zero_20260609_131648_349231 | NongatedCalciumScoreTask WL=40 HU normalises to 0.0 | PASS | TSK-005 | 2026-06-09T20:16:48.349143 |
| TSK005_yields_one_per_slice_20260609_131648_338309 | NongatedCalciumScoreTask yields one sample per slice | PASS | TSK-005 | 2026-06-09T20:16:48.338106 |
| TSK005_zero_score_target_20260609_131648_345315 | NongatedCalciumScoreTask zero-calcium patient yields zero target | PASS | TSK-005 | 2026-06-09T20:16:48.345190 |
| TSK006_gated_broadcast_20260609_131645_988591 | CoronaryCalciumTask broadcast design — every slice receives a target mask | PASS | TSK-006 | 2026-06-09T20:16:45.988357 |
| TSK006_nongated_broadcast_20260609_131648_343933 | NongatedCalciumScoreTask — patient label broadcast to every slice | PASS | TSK-005, TSK-006 | 2026-06-09T20:16:48.343750 |
| VER001_test_suite_existence_20260609_131648_551331 | Automated verification execution — test suite existence | PASS | VER-001 | 2026-06-09T20:16:48.550934 |
| VER002_evidence_capture_20260609_131648_553643 | Evidence capture — auto_save produces loadable JSON | PASS | VER-002 | 2026-06-09T20:16:48.553075 |
| VER003_model_performance_verification_20260609_131648_555112 | Model performance verification — segmentation metrics | PASS | VER-003 | 2026-06-09T20:16:48.554551 |
| tests/test_coca_ingestor_contract.py::test_graceful_failure_on_missing_data | COCA Ingestor → Missing Dataset Failure Mode | PASS | DAT-005 | 2026-06-09T20:16:45.680096 |
| dat002_list_patient_ids_sorted_numerically_20260609_131645_925211 | DAT-002: list_patient_ids returns patient ids in numeric sort order | PASS | DAT-002 | 2026-06-09T20:16:45.911030 |
| dat004_get_sample_generates_image_and_mask_20260609_131645_757209 | DAT-004: get_sample returns (image, mask) arrays with non-zero mask for annotated patient | PASS | DAT-004 | 2026-06-09T20:16:45.755769 |
| dat004_get_sample_multiple_rois_same_slice_20260609_131645_764657 | DAT-004: multiple ROIs on the same slice are merged into one mask | PASS | DAT-004 | 2026-06-09T20:16:45.763245 |
| dat004_get_sample_no_annotations_returns_empty_20260609_131645_761963 | DAT-004: get_sample returns empty arrays when patient has no annotations | PASS | DAT-004 | 2026-06-09T20:16:45.761228 |
| dat004_ingest_dataset_multiple_patients_20260609_131645_746161 | DAT-004: ingest_dataset loads all patients from the dataset | PASS | DAT-004 | 2026-06-09T20:16:45.744778 |
| dat004_nongated_annotations_always_none_20260609_131645_886704 | DAT-004: nongated ingestor always returns None for vector_rois (score-only dataset) | PASS | DAT-004 | 2026-06-09T20:16:45.877690 |
| dat004_nongated_hounsfield_rescale_applied_20260609_131645_875538 | DAT-004: RescaleSlope and RescaleIntercept are applied to nongated CT pixel values | PASS | DAT-004 | 2026-06-09T20:16:45.866692 |
| dat005_missing_dicom_files_20260609_131645_738234 | DAT-005: patient series dir with no DICOM files raises DatasetStructureError | PASS | DAT-005 | 2026-06-09T20:16:45.737860 |
| dat006_get_sample_returns_single_slice_20260609_131645_759877 | DAT-006: get_sample returns exactly one image/mask pair for a single-slice annotated patient | PASS | DAT-006 | 2026-06-09T20:16:45.758640 |
| dat006_get_volume_api_20260609_131645_743251 | DAT-006: load_patient_sample returns a volume with expected shape | PASS | DAT-006 | 2026-06-09T20:16:45.742255 |
| dat006_lazy_patient_loading_20260609_131645_731767 | DAT-006: COCAGatedIngestor loads each patient volume exactly once | PASS | DAT-006 | 2026-06-09T20:16:45.730448 |
| dat007_get_sample_skips_invalid_slice_annotations_20260609_131645_767358 | DAT-007: annotation with out-of-bounds ImageIndex is skipped; get_sample returns empty arrays | PASS | DAT-007 | 2026-06-09T20:16:45.766058 |
| dat007_slice_index_out_of_bounds_20260609_131645_734037 | DAT-007: annotation referencing out-of-bounds slice is silently ignored | PASS | DAT-007 | 2026-06-09T20:16:45.733255 |
| dat008_deterministic_slice_retrieval_20260609_131645_736471 | DAT-008: loading the same patient twice returns identical slice data | PASS | DAT-008 | 2026-06-09T20:16:45.735363 |
| dat009_annotation_missing_image_index_20260609_131645_751195 | DAT-009: annotation entry missing ImageIndex is treated as no annotation | PASS | DAT-009 | 2026-06-09T20:16:45.750106 |
| dat011_ingest_dataset_enumerates_patient_ids_20260609_131645_748690 | DAT-011: ingest_dataset enumerates all patient IDs without loading volumes | PASS | DAT-011 | 2026-06-09T20:16:45.747605 |
| dat015_empty_dataset_root_raises_20260609_131645_780989 | DAT-015: list_patient_ids raises when root has no patient directories | PASS | DAT-015 | 2026-06-09T20:16:45.770791 |
| dat015_missing_image_position_skipped_20260609_131645_898519 | DAT-015: DICOMs missing ImagePositionPatient are skipped; remaining slices still loaded | PASS | DAT-015 | 2026-06-09T20:16:45.888722 |
| dat015_missing_patient_directory_raises_20260609_131645_791519 | DAT-015: load_patient_sample raises for non-existent patient directory | PASS | DAT-015 | 2026-06-09T20:16:45.782693 |
| dat015_no_dicom_files_raises_20260609_131645_801681 | DAT-015: load_patient_sample raises when patient dir has no .dcm files | PASS | DAT-015 | 2026-06-09T20:16:45.793052 |
| dat015_spacing_fallback_on_missing_metadata_20260609_131645_909301 | DAT-015: missing PixelSpacing metadata falls back to (1,1,1) without raising | PASS | DAT-015 | 2026-06-09T20:16:45.900110 |
| dat016_blank_score_cell_treated_as_zero_20260609_131645_854067 | DAT-016: blank/None score cells in xlsx are coerced to 0.0 | PASS | DAT-016 | 2026-06-09T20:16:45.845206 |
| dat016_get_sample_volume_and_score_array_20260609_131645_935885 | DAT-016: get_sample returns numpy volume and score array with shape (4,) | PASS | DAT-016 | 2026-06-09T20:16:45.926855 |
| dat016_missing_score_entry_zero_fill_20260609_131645_832976 | DAT-016: patient absent from scores.xlsx gets zero-filled scores | PASS | DAT-016 | 2026-06-09T20:16:45.823994 |
| dat016_missing_score_warns_20260609_131645_843718 | DAT-016: missing score entry produces a warning on the ingestor report | PASS | DAT-016 | 2026-06-09T20:16:45.834574 |
| rsk003_ood_guard_20260609_131648_692183 | OOD guard test | PASS | RSK-003 | 2026-06-09T20:16:48.691995 |
| tests/test_project_structure.py::test_soup_inventory_complete | SOUP Inventory → All Dependencies Declared | PASS | DOC-001 | 2026-06-09T20:16:48.412927 |
| tests/test_coca_ingestor_synthetic.py::test_annotation_out_of_bounds_raises | COCA Gated Ingestor → Annotation Bounds Validation | PASS | DAT-004 | 2026-06-09T20:16:45.726791 |
| tests/test_coca_ingestor_synthetic.py::test_hounsfield_rescale_applied | COCA Gated Ingestor → HU Rescale | PASS | DAT-004 | 2026-06-09T20:16:45.724425 |
| tests/test_coca_ingestor_synthetic.py::test_slices_sorted_by_z | COCA Gated Ingestor → Slice Sorting | PASS | DAT-004 | 2026-06-09T20:16:45.721435 |
<!-- DHF_EVIDENCE_INDEX_END -->

## Artifact Locations

| Repository | Path |
|------------|------|
| <!-- DHF_VAR:CODE_REPO -->Coronary_prj, medical_image_ai_toolkit, regulatory_tools<!-- /DHF_VAR:CODE_REPO --> | `artifacts/evidence_runs/{YYYYMMDD_HHMMSS}/` |

*For real-time evidence, check CI workflow artifacts.*
