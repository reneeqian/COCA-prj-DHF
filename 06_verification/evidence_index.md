# Verification Evidence Index — <!-- DHF_VAR:PROJECT_NAME -->COCA-prj<!-- /DHF_VAR:PROJECT_NAME -->

Evidence reports are stored as JSON artifacts in `artifacts/evidence_runs/` in each code
repository. CI uploads them as workflow artifacts.

## Evidence Summary

| Repository | Latest CI Run | Grade |
|------------|--------------|-------|
| <!-- DHF_VAR:CODE_REPO -->Coronary_prj, medical_image_ai_toolkit, regulatory_tools<!-- /DHF_VAR:CODE_REPO --> | {{CI_RUN}} | — |

## Evidence Artifacts

<!-- DHF_EVIDENCE_INDEX_START -->
*Latest run: `20260526_130952`*

| Test ID | Subject | Result | Requirements | Timestamp |
|---------|---------|--------|--------------|-----------|
| DAT001_dataset_structure_validation_20260526_130952_669027 | DAT-001: missing patient/ directory raises DatasetStructureError | PASS | DAT-001 | 2026-05-26T20:09:52.669008 |
| DAT001_missing_patient_root_20260526_130952_648822 | Missing patient root raises DatasetStructureError | PASS | DAT-001 | 2026-05-26T20:09:52.648802 |
| DAT001_no_patient_directories_20260526_130952_666638 | Empty patient root raises DatasetStructureError | PASS | DAT-001 | 2026-05-26T20:09:52.666546 |
| DAT002_slice_determinism_20260526_130952_668151 | Repeated slice retrieval produces identical arrays | PASS | DAT-002 | 2026-05-26T20:09:52.667502 |
| DAT003_invalid_patient_id_20260526_130952_675333 | DAT-003: patient directory with no DICOM series raises DatasetStructureError | PASS | DAT-003 | 2026-05-26T20:09:52.675175 |
| DAT004_get_slice_success_20260526_130952_663724 | Slice retrieved with correct HU conversion | PASS | DAT-004 | 2026-05-26T20:09:52.663164 |
| DAT004_missing_image_position_20260526_130952_662337 | DICOM missing ImagePositionPatient raises DatasetStructureError | PASS | DAT-004 | 2026-05-26T20:09:52.661799 |
| DAT004_nongated_z_sort_20260526_130952_759960 | COCANongatedIngestor Z-sort | PASS | DAT-004 | 2026-05-26T20:09:52.753571 |
| DAT004_skip_dicom_without_position_20260526_130952_810967 | DAT-004: DICOMs missing ImagePositionPatient are skipped with a warning | PASS | DAT-004 | 2026-05-26T20:09:52.809988 |
| DAT005_annotation_xml_parse_failure_20260526_130952_654016 | Malformed annotation XML raises DatasetStructureError | PASS | DAT-005 | 2026-05-26T20:09:52.653211 |
| DAT005_invalid_dicom_file_20260526_130952_655620 | Invalid DICOM file raises DatasetStructureError | PASS | DAT-005 | 2026-05-26T20:09:52.654997 |
| DAT005_missing_image_position_patient_20260526_130952_652399 | DICOM missing ImagePositionPatient raises DatasetStructureError | PASS | DAT-005 | 2026-05-26T20:09:52.651855 |
| DAT005_no_dicom_files_20260526_130952_665755 | Series with no DICOM files raises DatasetStructureError | PASS | DAT-005 | 2026-05-26T20:09:52.665521 |
| DAT005_no_series_directories_20260526_130952_664710 | Patient with no series directories raises DatasetStructureError | PASS | DAT-005 | 2026-05-26T20:09:52.664558 |
| DAT005_patient_without_series_20260526_130952_650059 | Patient directory without series raises DatasetStructureError | PASS | DAT-005 | 2026-05-26T20:09:52.649892 |
| DAT005_series_without_dicoms_20260526_130952_651100 | Series directory with no DICOM files raises DatasetStructureError | PASS | DAT-005 | 2026-05-26T20:09:52.650851 |
| DAT006_get_patient_api_20260526_130952_682778 | DAT-006: load_patient_sample returns PatientSample with correct patient_id | PASS | DAT-006 | 2026-05-26T20:09:52.682206 |
| DAT007_annotation_slice_out_of_bounds_20260526_130952_657502 | Annotation slice index outside volume is ignored | PASS | DAT-007 | 2026-05-26T20:09:52.656585 |
| DAT008_nongated_deterministic_loading_20260526_130952_808662 | DAT-008: loading the same nongated patient twice returns identical volumes | PASS | DAT-008 | 2026-05-26T20:09:52.802563 |
| DAT009_invalid_polygon_skipped_20260526_130952_635263 | ROI with <3 points is skipped | PASS | DAT-009 | 2026-05-26T20:09:52.634405 |
| DAT009_roi_insufficient_points_ignored_20260526_130952_659267 | ROI with fewer than 3 points is ignored | PASS | DAT-009 | 2026-05-26T20:09:52.658399 |
| DAT009_valid_annotation_geometry_20260526_130952_633351 | Valid annotation geometry: polygon shape and dtype | PASS | DAT-009 | 2026-05-26T20:09:52.630808 |
| DAT010_dataset_without_annotations_20260526_130952_660841 | Dataset with no annotation files returns empty annotations | PASS | DAT-010 | 2026-05-26T20:09:52.660138 |
| DAT010_missing_annotation_file_empty_20260526_130952_636682 | Missing annotation file returns empty annotations | PASS | DAT-010 | 2026-05-26T20:09:52.636132 |
| DAT011_datasource_partition_assignment_20260526_130952_851351 | Datasource partition generation | PASS | DAT-011 | 2026-05-26T20:09:52.851302 |
| DAT012_ct_volume_sorted_by_z_20260526_130952_691302 | DAT-012: CT volume slices are sorted by Z position | PASS | DAT-012 | 2026-05-26T20:09:52.690568 |
| DAT013_contour_rasterization_20260526_130952_639964 | Annotation rasterization — polygon to mask | PASS | DAT-013 | 2026-05-26T20:09:52.639344 |
| DAT013_mask_dimension_alignment_20260526_130952_640704 | Annotation rasterization — mask shape matches source | PASS | DAT-013 | 2026-05-26T20:09:52.640528 |
| DAT013_task_rasterizes_contour_to_nonzero_mask_20260526_130952_826928 | DAT-013: CoronaryCalciumTask rasterizes contour annotations to non-zero binary mask | PASS | DAT-013 | 2026-05-26T20:09:52.826804 |
| DAT014_domain_safe_ingestion_errors_20260526_130952_641965 | Domain-safe ingestion errors — DatasetStructureError | PASS | DAT-014 | 2026-05-26T20:09:52.641564 |
| DAT014_missing_patient_directory_20260526_130952_642801 | Domain-safe ingestion errors — missing patient directory | PASS | DAT-014 | 2026-05-26T20:09:52.642781 |
| DAT015_scores_file_not_found_20260526_130952_701485 | DAT-015: missing scores.xlsx raises DatasetStructureError | PASS | DAT-015 | 2026-05-26T20:09:52.701287 |
| DAT016_scores_attached_20260526_130952_733265 | COCANongatedIngestor score loading | PASS | DAT-016 | 2026-05-26T20:09:52.728003 |
| DOC001_readme_exists_with_heading_20260526_130954_626456 | DOC-001: README.md exists and contains at least one Markdown heading | PASS | DOC-001 | 2026-05-26T20:09:54.626207 |
| DOC002_requirements_yaml_valid_structure_20260526_130954_625577 | DOC-002: requirements.yaml exists and has required structure | PASS | DOC-002 | 2026-05-26T20:09:54.608018 |
| DOC003_traceability_matrix_row_schema_20260526_130954_768318 | Traceability matrix row schema — requirement_id field present in every row | PASS | DOC-003 | 2026-05-26T20:09:54.746315 |
| INF001_inference_capability_20260526_130954_472599 | Inference capability on new data | PASS | INF-001 | 2026-05-26T20:09:54.469021 |
| INF002_inference_determinism_20260526_130954_476910 | Inference determinism — identical inputs produce identical outputs | PASS | INF-002 | 2026-05-26T20:09:54.473335 |
| MOD001_small_cnn_output_shape_20260526_130954_478895 | SmallSegmentationCNN output shape | PASS | MOD-001 | 2026-05-26T20:09:54.478065 |
| MOD001_unet2d_configurable_channels_20260526_130954_495430 | UNet2D base_channels configuration | PASS | MOD-001 | 2026-05-26T20:09:54.484248 |
| MOD001_unet2d_finite_outputs_20260526_130954_500298 | UNet2D outputs are finite on random input | PASS | MOD-001 | 2026-05-26T20:09:54.496458 |
| MOD001_unet2d_gradient_flow_20260526_130954_512869 | UNet2D gradient flow verification | PASS | MOD-001 | 2026-05-26T20:09:54.501121 |
| MOD001_unet2d_output_shape_20260526_130954_483402 | UNet2D output shape preserves spatial dimensions | PASS | MOD-001 | 2026-05-26T20:09:54.479734 |
| MOD002_model_persistence_20260526_130953_873139 | Model artifact persistence — save and reload | PASS | MOD-002 | 2026-05-26T20:09:53.854545 |
| MOD003_model_evaluation_20260526_130954_468032 | Model evaluation capability on test partition | PASS | MOD-003 | 2026-05-26T20:09:53.874553 |
| MOD004_regressor_finite_output_20260526_130954_576377 | CalciumScoreRegressor finite outputs | PASS | MOD-004 | 2026-05-26T20:09:54.573367 |
| MOD004_regressor_gradient_flow_20260526_130954_582452 | CalciumScoreRegressor gradient flow | PASS | MOD-004 | 2026-05-26T20:09:54.577239 |
| MOD004_regressor_output_shape_20260526_130954_518319 | CalciumScoreRegressor output shape | PASS | MOD-004 | 2026-05-26T20:09:54.513867 |
| MOD004_regressor_spatial_flexibility_20260526_130954_571839 | CalciumScoreRegressor spatial size flexibility | PASS | MOD-004 | 2026-05-26T20:09:54.519024 |
| MOD005_segmentation_min_dice_20260526_130954_595422 | MOD-005: SEGMENTATION_MIN_DICE equals approved floor 0.50 | PASS | MOD-005 | 2026-05-26T20:09:54.595412 |
| MOD006_regression_max_mae_20260526_130954_596078 | MOD-006: REGRESSION_MAX_MAE_AU equals approved ceiling 100.0 AU | PASS | MOD-006 | 2026-05-26T20:09:54.596074 |
| REP001_training_report_generation_20260526_130954_630344 | Training report generation | PASS | REP-001 | 2026-05-26T20:09:54.628826 |
| REP002_visualization_support_20260526_130954_717674 | Visualization support — training curve figure | PASS | REP-002 | 2026-05-26T20:09:54.631361 |
| REP003_status_report_section_headers_20260526_130954_776303 | REP-003: status_report produces TRAINING, TUNING, and MODEL TESTING section headers | PASS | REP-003 | 2026-05-26T20:09:54.775243 |
| REP004_status_report_model_testing_section_20260526_130954_781242 | REP-004: status_report prints model testing metrics (dice, iou, precision, recall) | PASS | REP-004 | 2026-05-26T20:09:54.780814 |
| REP004_status_report_no_runs_20260526_130954_774161 | status_report handles missing artifact directories | PASS | REP-004 | 2026-05-26T20:09:54.774075 |
| REP004_status_report_training_section_20260526_130954_777973 | REP-004: status_report prints training metrics (final_loss, learning_rate) | PASS | REP-004 | 2026-05-26T20:09:54.777313 |
| REP004_status_report_tuning_section_20260526_130954_779852 | REP-004: status_report prints tuning metrics (num_trials, best_val_loss) | PASS | REP-004 | 2026-05-26T20:09:54.779412 |
| RSK001_segmentation_threshold_20260526_130954_768932 | RSK-001: SEGMENTATION_MIN_DICE equals the approved clinical floor value 0.50 | PASS | RSK-001 | 2026-05-26T20:09:54.768926 |
| RSK002_negative_score_clamped_20260526_130954_769627 | RSK-002: negative calcium scores are clamped before log1p transform | PASS | RSK-002 | 2026-05-26T20:09:54.769420 |
| RSK002_regression_threshold_20260526_130954_770146 | RSK-002: REGRESSION_MAX_MAE_AU equals the approved clinical ceiling 100.0 AU | PASS | RSK-002 | 2026-05-26T20:09:54.770142 |
| RSK003_missing_xlsx_error_20260526_130954_771228 | RSK-003: ingestor raises DatasetStructureError on missing scores.xlsx | PASS | RSK-003 | 2026-05-26T20:09:54.771203 |
| RSK004_log1p_finite_20260526_130954_772729 | RSK-004: log1p target is finite for zero, large, and negative inputs | PASS | RSK-004 | 2026-05-26T20:09:54.772364 |
| SYS001_volume_sorted_by_z_20260526_130952_638765 | Volume slices are sorted by Z position | PASS | SYS-001 | 2026-05-26T20:09:52.637513 |
| SYS002_DAT011_split_generates_partitions_20260526_130952_849815 | Deterministic holdout split — three-partition generation | PASS | DAT-011, SYS-002 | 2026-05-26T20:09:52.849764 |
| SYS002_split_reproducibility_20260526_130952_850346 | Deterministic holdout split — seed reproducibility | PASS | SYS-002 | 2026-05-26T20:09:52.850290 |
| SYS003_traceability_matrix_generation_20260526_130954_745666 | Traceable verification — traceability matrix generation | PASS | SYS-003 | 2026-05-26T20:09:54.721741 |
| SYS004_coronary_calcium_task_is_instantiable_20260526_130954_783677 | SYS-004: CoronaryCalciumTask can be instantiated without error | PASS | SYS-004 | 2026-05-26T20:09:54.783674 |
| SYS005_coca_gated_ingestor_subclasses_base_ingestor_20260526_130954_784172 | SYS-005: COCAGatedIngestor subclasses BaseIngestor | PASS | SYS-005 | 2026-05-26T20:09:54.784169 |
| SYS006_task_encapsulation_20260526_130954_781809 | Dataset task encapsulation — project-level ownership | PASS | SYS-006 | 2026-05-26T20:09:54.781806 |
| SYS007_intended_use_20260526_130954_784646 | Intended use — advisory, radiologist-facing | PASS | SYS-007 | 2026-05-26T20:09:54.784642 |
| TRN001_initialization_determinism_20260526_130952_899460 | Controlled model initialization — seed determinism | PASS | TRN-001 | 2026-05-26T20:09:52.889978 |
| TRN002_training_artifact_generation_20260526_130953_731958 | Training artifact generation | PASS | TRN-002 | 2026-05-26T20:09:52.900828 |
| TRN003_compute_loss_finite_scalar_20260526_130952_843279 | CoronaryCalciumTask compute_loss returns finite scalar | PASS | TRN-003 | 2026-05-26T20:09:52.828016 |
| TRN003_loss_penalises_wrong_predictions_20260526_130952_848519 | CoronaryCalciumTask loss ordering: wrong > correct | PASS | TRN-003 | 2026-05-26T20:09:52.848320 |
| TRN003_loss_perfect_prediction_20260526_130952_847813 | CoronaryCalciumTask combined loss near zero on perfect prediction | PASS | TRN-003 | 2026-05-26T20:09:52.846685 |
| TRN003_nongated_gradient_flow_20260526_130954_607332 | NongatedCalciumScoreTask gradient flow | PASS | TRN-003 | 2026-05-26T20:09:54.605733 |
| TRN004_model_retraining_20260526_130953_853077 | Coronary model retraining capability | PASS | TRN-004 | 2026-05-26T20:09:53.733489 |
| TRN005_dataset_training_interface_20260526_130952_889041 | Coronary dataset training interface | PASS | TRN-005 | 2026-05-26T20:09:52.852224 |
| TSK001_task_definition_interface_20260526_130954_782290 | Task definition interface — toolkit contract | PASS | TSK-001 | 2026-05-26T20:09:54.782282 |
| TSK001_task_yields_one_sample_per_slice_20260526_130952_821498 | TSK-001: CoronaryCalciumTask yields one sample per CT slice | PASS | TSK-001 | 2026-05-26T20:09:52.811658 |
| TSK002_ignore_short_contours_20260526_130952_827513 | CoronaryCalciumTask ignores contours with fewer than 3 points | PASS | TSK-002 | 2026-05-26T20:09:52.827466 |
| TSK002_task_input_hu_normalised_20260526_130952_845472 | TSK-002: CoronaryCalciumTask normalises input HU values to [-1, +1] range | PASS | TSK-002 | 2026-05-26T20:09:52.844296 |
| TSK002_task_yields_masks_for_annotated_slices_20260526_130952_826151 | TSK-002: CoronaryCalciumTask input/target shapes are (1,1,H,W); unannotated slices get zero target | PASS | TSK-002 | 2026-05-26T20:09:52.822311 |
| TSK003_task_determinism_20260526_130954_783094 | Task determinism — identical inputs produce identical outputs | PASS | TSK-003 | 2026-05-26T20:09:54.782748 |
| TSK004_task_applies_cardiac_hu_window_20260526_130952_846117 | TSK-004: CoronaryCalciumTask applies the cardiac HU window [-160, 240] | PASS | TSK-004 | 2026-05-26T20:09:52.846048 |
| TSK005_hu_above_window_20260526_130954_602681 | NongatedCalciumScoreTask HU window — above | PASS | TSK-004, TSK-005 | 2026-05-26T20:09:54.602642 |
| TSK005_hu_below_window_20260526_130954_602121 | NongatedCalciumScoreTask HU window — below | PASS | TSK-004, TSK-005 | 2026-05-26T20:09:54.602082 |
| TSK005_input_tensor_shape_20260526_130954_597304 | NongatedCalciumScoreTask input tensor shape is (1,1,H,W) | PASS | TSK-005 | 2026-05-26T20:09:54.597254 |
| TSK005_log1p_target_20260526_130954_599659 | NongatedCalciumScoreTask target log1p transform | PASS | TSK-005 | 2026-05-26T20:09:54.598520 |
| TSK005_loss_finite_scalar_20260526_130954_604227 | NongatedCalciumScoreTask MSE loss is finite | PASS | TRN-003, TSK-005 | 2026-05-26T20:09:54.603688 |
| TSK005_loss_higher_for_wrong_20260526_130954_605271 | NongatedCalciumScoreTask MSE loss is monotone in error magnitude | PASS | TSK-005 | 2026-05-26T20:09:54.605226 |
| TSK005_loss_zero_on_perfect_20260526_130954_604754 | NongatedCalciumScoreTask MSE loss near zero on perfect prediction | PASS | TSK-005 | 2026-05-26T20:09:54.604722 |
| TSK005_missing_metadata_zero_score_20260526_130954_601563 | NongatedCalciumScoreTask missing metadata defaults to zero score | PASS | TSK-005 | 2026-05-26T20:09:54.601512 |
| TSK005_target_tensor_shape_20260526_130954_597868 | NongatedCalciumScoreTask target tensor shape is (4,) | PASS | TSK-005 | 2026-05-26T20:09:54.597814 |
| TSK005_wl40_maps_to_zero_20260526_130954_603203 | NongatedCalciumScoreTask WL=40 HU normalises to 0.0 | PASS | TSK-005 | 2026-05-26T20:09:54.603163 |
| TSK005_yields_one_per_slice_20260526_130954_596754 | NongatedCalciumScoreTask yields one sample per slice | PASS | TSK-005 | 2026-05-26T20:09:54.596617 |
| TSK005_zero_score_target_20260526_130954_600986 | NongatedCalciumScoreTask zero-calcium patient yields zero target | PASS | TSK-005 | 2026-05-26T20:09:54.600915 |
| TSK006_gated_broadcast_20260526_130952_849225 | CoronaryCalciumTask broadcast design — every slice receives a target mask | PASS | TSK-006 | 2026-05-26T20:09:52.849084 |
| TSK006_nongated_broadcast_20260526_130954_600382 | NongatedCalciumScoreTask — patient label broadcast to every slice | PASS | TSK-005, TSK-006 | 2026-05-26T20:09:54.600272 |
| VER001_test_suite_existence_20260526_130954_718798 | Automated verification execution — test suite existence | PASS | VER-001 | 2026-05-26T20:09:54.718607 |
| VER002_evidence_capture_20260526_130954_720193 | Evidence capture — auto_save produces loadable JSON | PASS | VER-002 | 2026-05-26T20:09:54.719823 |
| VER003_model_performance_verification_20260526_130954_721215 | Model performance verification — segmentation metrics | PASS | VER-003 | 2026-05-26T20:09:54.720710 |
| tests/test_coca_ingestor_contract.py::test_graceful_failure_on_missing_data | COCA Ingestor → Missing Dataset Failure Mode | PASS | DAT-005 | 2026-05-26T20:09:52.646785 |
| dat002_list_patient_ids_sorted_numerically_20260526_130952_794859 | DAT-002: list_patient_ids returns patient ids in numeric sort order | PASS | DAT-002 | 2026-05-26T20:09:52.789765 |
| dat004_get_sample_generates_image_and_mask_20260526_130952_693131 | DAT-004: get_sample returns (image, mask) arrays with non-zero mask for annotated patient | PASS | DAT-004 | 2026-05-26T20:09:52.692177 |
| dat004_get_sample_multiple_rois_same_slice_20260526_130952_698236 | DAT-004: multiple ROIs on the same slice are merged into one mask | PASS | DAT-004 | 2026-05-26T20:09:52.697281 |
| dat004_get_sample_no_annotations_returns_empty_20260526_130952_696428 | DAT-004: get_sample returns empty arrays when patient has no annotations | PASS | DAT-004 | 2026-05-26T20:09:52.695888 |
| dat004_ingest_dataset_multiple_patients_20260526_130952_686181 | DAT-004: ingest_dataset loads all patients from the dataset | PASS | DAT-004 | 2026-05-26T20:09:52.685099 |
| dat004_nongated_annotations_always_none_20260526_130952_774575 | DAT-004: nongated ingestor always returns None for vector_rois (score-only dataset) | PASS | DAT-004 | 2026-05-26T20:09:52.767981 |
| dat004_nongated_hounsfield_rescale_applied_20260526_130952_766775 | DAT-004: RescaleSlope and RescaleIntercept are applied to nongated CT pixel values | PASS | DAT-004 | 2026-05-26T20:09:52.761254 |
| dat005_missing_dicom_files_20260526_130952_681297 | DAT-005: patient series dir with no DICOM files raises DatasetStructureError | PASS | DAT-005 | 2026-05-26T20:09:52.680982 |
| dat006_get_sample_returns_single_slice_20260526_130952_695026 | DAT-006: get_sample returns exactly one image/mask pair for a single-slice annotated patient | PASS | DAT-006 | 2026-05-26T20:09:52.694030 |
| dat006_get_volume_api_20260526_130952_684266 | DAT-006: load_patient_sample returns a volume with expected shape | PASS | DAT-006 | 2026-05-26T20:09:52.683654 |
| dat006_lazy_patient_loading_20260526_130952_676836 | DAT-006: COCAGatedIngestor loads each patient volume exactly once | PASS | DAT-006 | 2026-05-26T20:09:52.676149 |
| dat007_get_sample_skips_invalid_slice_annotations_20260526_130952_700324 | DAT-007: annotation with out-of-bounds ImageIndex is skipped; get_sample returns empty arrays | PASS | DAT-007 | 2026-05-26T20:09:52.699086 |
| dat007_slice_index_out_of_bounds_20260526_130952_678376 | DAT-007: annotation referencing out-of-bounds slice is silently ignored | PASS | DAT-007 | 2026-05-26T20:09:52.677734 |
| dat008_deterministic_slice_retrieval_20260526_130952_680023 | DAT-008: loading the same patient twice returns identical slice data | PASS | DAT-008 | 2026-05-26T20:09:52.679263 |
| dat009_annotation_missing_image_index_20260526_130952_689696 | DAT-009: annotation entry missing ImageIndex is treated as no annotation | PASS | DAT-009 | 2026-05-26T20:09:52.688826 |
| dat011_ingest_dataset_enumerates_patient_ids_20260526_130952_687834 | DAT-011: ingest_dataset enumerates all patient IDs without loading volumes | PASS | DAT-011 | 2026-05-26T20:09:52.687152 |
| dat015_empty_dataset_root_raises_20260526_130952_709723 | DAT-015: list_patient_ids raises when root has no patient directories | PASS | DAT-015 | 2026-05-26T20:09:52.702393 |
| dat015_missing_image_position_skipped_20260526_130952_782108 | DAT-015: DICOMs missing ImagePositionPatient are skipped; remaining slices still loaded | PASS | DAT-015 | 2026-05-26T20:09:52.775795 |
| dat015_missing_patient_directory_raises_20260526_130952_715835 | DAT-015: load_patient_sample raises for non-existent patient directory | PASS | DAT-015 | 2026-05-26T20:09:52.710835 |
| dat015_no_dicom_files_raises_20260526_130952_721738 | DAT-015: load_patient_sample raises when patient dir has no .dcm files | PASS | DAT-015 | 2026-05-26T20:09:52.716882 |
| dat015_spacing_fallback_on_missing_metadata_20260526_130952_788675 | DAT-015: missing PixelSpacing metadata falls back to (1,1,1) without raising | PASS | DAT-015 | 2026-05-26T20:09:52.783344 |
| dat016_blank_score_cell_treated_as_zero_20260526_130952_752157 | DAT-016: blank/None score cells in xlsx are coerced to 0.0 | PASS | DAT-016 | 2026-05-26T20:09:52.746853 |
| dat016_get_sample_volume_and_score_array_20260526_130952_801389 | DAT-016: get_sample returns numpy volume and score array with shape (4,) | PASS | DAT-016 | 2026-05-26T20:09:52.795881 |
| dat016_missing_score_entry_zero_fill_20260526_130952_739363 | DAT-016: patient absent from scores.xlsx gets zero-filled scores | PASS | DAT-016 | 2026-05-26T20:09:52.734365 |
| dat016_missing_score_warns_20260526_130952_745831 | DAT-016: missing score entry produces a warning on the ingestor report | PASS | DAT-016 | 2026-05-26T20:09:52.740400 |
| rsk003_ood_guard_20260526_130954_771849 | OOD guard test | PASS | RSK-003 | 2026-05-26T20:09:54.771707 |
| tests/test_project_structure.py::test_soup_inventory_complete | SOUP Inventory → All Dependencies Declared | PASS | DOC-001 | 2026-05-26T20:09:54.627034 |
| tests/test_coca_ingestor_synthetic.py::test_annotation_out_of_bounds_raises | COCA Gated Ingestor → Annotation Bounds Validation | PASS | DAT-004 | 2026-05-26T20:09:52.673544 |
| tests/test_coca_ingestor_synthetic.py::test_hounsfield_rescale_applied | COCA Gated Ingestor → HU Rescale | PASS | DAT-004 | 2026-05-26T20:09:52.671795 |
| tests/test_coca_ingestor_synthetic.py::test_slices_sorted_by_z | COCA Gated Ingestor → Slice Sorting | PASS | DAT-004 | 2026-05-26T20:09:52.669817 |
<!-- DHF_EVIDENCE_INDEX_END -->

## Artifact Locations

| Repository | Path |
|------------|------|
| <!-- DHF_VAR:CODE_REPO -->Coronary_prj, medical_image_ai_toolkit, regulatory_tools<!-- /DHF_VAR:CODE_REPO --> | `artifacts/evidence_runs/{YYYYMMDD_HHMMSS}/` |

*For real-time evidence, check CI workflow artifacts.*
