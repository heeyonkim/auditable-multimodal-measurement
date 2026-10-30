# Data catalog

[Home](../README.md) / [Submission evidence](README.md) / Data catalog

This inventory groups the released tables by the questions they support. Start with [submission evidence](README.md) for a short route through the main results.

## Earnings calls and score robustness

- [earnings_call_screening_ledger.csv](../data/derived/earnings_call_screening_ledger.csv): Retained calls, initial exclusions, and answer-summary availability.
- [worked_example_measure.csv](../data/derived/worked_example_measure.csv): one traceable observation shown in the narrated worked example, with source interval, scores, and feature-exclusion checks.
- [expanded_audio_answer_scores.csv](../data/derived/expanded_audio_answer_scores.csv): 3,273 eligible answers, including 3,233 with paired departure scores; component variants and missing scores are retained.
- [expanded_audio_archive_validation.json](../data/derived/expanded_audio_archive_validation.json): private-archive integrity counts without paths or credentials.
- [expanded_audio_call_concentration.csv](../data/derived/expanded_audio_call_concentration.csv): call-level concentration of review flags.
- [expanded_audio_candidate_audit.csv](../data/derived/expanded_audio_candidate_audit.csv): prespecified tenure windows, selection rationale, aliases, and tenure-source links for the seven-executive expansion.
- [expanded_audio_eligibility_sensitivity.csv](../data/derived/expanded_audio_eligibility_sensitivity.csv): stability under stricter answer-length requirements.
- [expanded_audio_feature_variant_summary.csv](../data/derived/expanded_audio_feature_variant_summary.csv): feature-family and leave-one-feature-out robustness results.
- [expanded_audio_measurement_yield.csv](../data/derived/expanded_audio_measurement_yield.csv): usable calls, eligible answers, exclusions, and review-flag counts for 12 executives.
- [expanded_audio_metadata_status_summary.csv](../data/derived/expanded_audio_metadata_status_summary.csv): documented structured-metadata inclusions and review items.
- [expanded_audio_prepared_qa_summary.csv](../data/derived/expanded_audio_prepared_qa_summary.csv): prepared-remarks versus Q&A contrasts across 259 calls.
- [expanded_audio_primary_examples_robustness.csv](../data/derived/expanded_audio_primary_examples_robustness.csv): specification support for 177 illustrative review flags.

## Exploratory market-outcome linkage

- [earnings_call_market_cohort_sensitivity.csv](../data/derived/earnings_call_market_cohort_sensitivity.csv): original, added, and pooled company-cohort comparisons.
- [earnings_call_market_leave_one_company_out.csv](../data/derived/earnings_call_market_leave_one_company_out.csv): influence checks that omit one firm at a time.
- [earnings_call_market_models.csv](../data/derived/earnings_call_market_models.csv): pooled model estimates and robustness specifications for the exploratory market linkage.
- [earnings_call_market_outcomes.csv](../data/derived/earnings_call_market_outcomes.csv): call-level behavioral summaries, event timing, and signed market-adjusted returns for 286 earnings calls, including 274 with eligible answer-level scores.
- [earnings_call_market_summary.json](../data/derived/earnings_call_market_summary.json): compact machine-readable results and interpretation boundary.

## 30-interview production archive

- [editorial_responsiveness_chance_adjusted.csv](../data/derived/editorial_responsiveness_chance_adjusted.csv): observed camera-cut coupling compared with a within-video circular-shift null.
- [event_aligned_overall_rates.csv](../data/derived/event_aligned_overall_rates.csv): pooled rates and Wilson intervals for coarse composition change, focus gain, directional shifts, and fine-grained coding sensitivity.
- [event_aligned_production_measures.csv](../data/derived/event_aligned_production_measures.csv): 120 speaker-transition events with matched pre, entry, and settled composition codes, exact-window cut counts, audio-turn measures, and uncertainty flags.
- [event_aligned_rates_by_format_and_cut.csv](../data/derived/event_aligned_rates_by_format_and_cut.csv): production measures stratified by video format and whether a cut occurred in the matched frame window.
- [interview_measures.csv](../data/derived/interview_measures.csv): speaker-neutral audio, interaction, visual, production, and quality-control measures for 30 interviews.
- [multimodal_frame_turn_alignment.csv](../data/derived/multimodal_frame_turn_alignment.csv): 360 sampled visual observations aligned to active or nearest speech turns.
- [sample_manifest.csv](../data/derived/sample_manifest.csv): public source identifiers, URLs, sampling strata, and screening notes for 30 Bloomberg videos.
- [speaker_transition_edit_alignment.csv](../data/derived/speaker_transition_edit_alignment.csv): each speaker change aligned to the nearest detected camera cut.
- [video_measure_summary.json](../data/derived/video_measure_summary.json): Supplementary numeric definitions or summary.
- [video_measurement_sensitivity.csv](../data/derived/video_measurement_sensitivity.csv): stability across scene thresholds and one-, two-, and three-second alignment windows.
- [video_organizational_measures.csv](../data/derived/video_organizational_measures.csv): interview-level audio, visible-behavior, production, and cross-modal measures for the 30-video pilot.
- [video_shot_dynamics.csv](../data/derived/video_shot_dynamics.csv): continuous shot counts, shot-duration distributions, and camera-cut alignment with speaker transitions.
- [video_shot_segments.csv](../data/derived/video_shot_segments.csv): timestamped shot boundaries from the primary scene-change specification.
- [video_variable_recipes.csv](../data/derived/video_variable_recipes.csv): construct-neutral definitions, possible uses, validation status, and limitations for video measures.

## Definitions and compact summaries

- [pilot_scale.csv](../data/derived/pilot_scale.csv): Supplementary numeric definitions or summary.
- [pilot_summary_statistics.json](../data/derived/pilot_summary_statistics.json): compact counts and descriptive summaries for both pilots.
- [validation_plan.csv](../data/derived/validation_plan.csv): proposed validation designs for 19 measure families and pipeline layers.
- [variable_dictionary.csv](../data/derived/variable_dictionary.csv): definitions, provenance, recommended status, validation targets, and limitations for 74 fields.

## Eight additional repeated-interviewer interviews

The [repeated-interviewer guide](repeated_interviewer.md) defines the sample, features, reference rules, and limitations. Its [data folder](../data/derived/repeated_interviewer/) contains:

- [francine_audio_transcript_profiles.csv](../data/derived/repeated_interviewer/francine_audio_transcript_profiles.csv): Numeric episode inputs for transcript, timing, and voice channels.
- [francine_multimodal_deviation_profiles.csv](../data/derived/repeated_interviewer/francine_multimodal_deviation_profiles.csv): The cross-channel matrix used in Figure 3.
- [francine_nonvisual_domain_deviations.csv](../data/derived/repeated_interviewer/francine_nonvisual_domain_deviations.csv): Standardized feature contributions and nonvisual composites.
- [francine_speaker_role_audit.csv](../data/derived/repeated_interviewer/francine_speaker_role_audit.csv): Functional-role audit without transcript quotations.
- [francine_speaker_state_coverage.csv](../data/derived/repeated_interviewer/francine_speaker_state_coverage.csv): Observable frame counts and state-specific coverage.
- [francine_speaker_state_deviations.csv](../data/derived/repeated_interviewer/francine_speaker_state_deviations.csv): Separate visible-speaking/listening scores and original bootstrap intervals.
- [manifest.csv](../data/derived/repeated_interviewer/manifest.csv): Public source IDs, dates, durations, interviewer, and interviewees.
- [speaker_role_overrides.csv](../data/derived/repeated_interviewer/speaker_role_overrides.csv): Recorded corrections to automatic role assignments, without quotations.
- [video_episode_comparison.csv](../data/derived/repeated_interviewer/video_episode_comparison.csv): Scores under alternate visibility and adjustment specifications.
- [video_observability_coverage.csv](../data/derived/repeated_interviewer/video_observability_coverage.csv): Coverage under the alternate sampling specifications.
- [video_production_aware_summary.json](../data/derived/repeated_interviewer/video_production_aware_summary.json): Eligibility, common-sample rank comparisons, and sensitivity limits.
- [visual_feature_calibration.csv](../data/derived/repeated_interviewer/visual_feature_calibration.csv): Adjusted episode means and pooled scales for reconstructing visual composites.

## Earlier five-executive pilot

[Earlier pilot tables](../data/earlier_pilot/README.md) retain the original 118-call, 1,260-answer variable examples. They do not replace the current 12-executive panel.

## Code, figures, and verification

- [Figures](../figures/README.md): the three submission figures and supporting robustness/production figures.
- [Earnings scoring implementation](../scripts/score_earnings_answers.py): transformations, eligibility, and reference rules.
- [Submission verification](../scripts/verify_submission_evidence.py): reconstruct profiles and check the reported sample and score counts.
- [Figure 3 builder](../scripts/build_submission_video_figure.py): redraw the repeated-interviewer heatmap with Matplotlib and NumPy.
- [Summary script](../scripts/summarize_pilot.py): regenerate the compact descriptive summaries.
- [Reproducibility guide](reproducibility.md): verification commands and full-pipeline requirements.
- [Release manifest](../research_object_manifest.json): file checksums and recorded model information.

Source recordings, extracted frames, verbatim transcripts, face embeddings, and credentials are excluded.
