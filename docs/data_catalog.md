# Data catalog

[Home](../README.md) / [Submission evidence](README.md) / Data catalog

Start with the files below for the submitted results. The full inventory follows, grouped by analysis.

| To inspect… | Start with… |
| --- | --- |
| Figure 2 and the audio/transcript comparison | [Answer scores](../data/derived/expanded_audio_answer_scores.csv) |
| Figure 3 and the interviewer’s patterns across channels | [Repeated-interviewer profiles](../data/derived/repeated_interviewer/francine_multimodal_deviation_profiles.csv) |
| Speaker changes near camera cuts | [Observed and chance overlap](../data/derived/editorial_responsiveness_chance_adjusted.csv) |
| The narrated example | [One exported observation](../data/derived/worked_example_measure.csv) |
| Sample sizes | [Pilot counts](../data/derived/pilot_scale.csv) |

Each file description explains what to look for. The [technical appendix](submission_technical_appendix.md) gives the measurement rules and limitations.

## Earnings calls and score robustness

| File | What it contains |
| --- | --- |
| [earnings_call_screening_ledger.csv](../data/derived/earnings_call_screening_ledger.csv) | Shows which of the 300 collected calls were retained or excluded and which have usable answer summaries. |
| [worked_example_measure.csv](../data/derived/worked_example_measure.csv) | One traceable observation shown in the narrated worked example, with source interval, scores, and feature-exclusion checks. |
| [expanded_audio_answer_scores.csv](../data/derived/expanded_audio_answer_scores.csv) | 3,273 eligible answers, including 3,233 with paired departure scores; component variants and missing scores are retained. |
| [expanded_audio_archive_validation.json](../data/derived/expanded_audio_archive_validation.json) | Counts of processed recordings, files, and checks in the underlying archive; no private paths or credentials. |
| [expanded_audio_call_concentration.csv](../data/derived/expanded_audio_call_concentration.csv) | Shows whether flagged answers are spread across calls or concentrated in particular calls. |
| [expanded_audio_candidate_audit.csv](../data/derived/expanded_audio_candidate_audit.csv) | Documents the selection windows, reasons for inclusion, name variants, and tenure sources for the seven added executives. |
| [expanded_audio_eligibility_sensitivity.csv](../data/derived/expanded_audio_eligibility_sensitivity.csv) | Shows how the results change when answers must meet stricter length requirements. |
| [expanded_audio_feature_variant_summary.csv](../data/derived/expanded_audio_feature_variant_summary.csv) | Shows how results change when groups of audio features or individual features are excluded. |
| [expanded_audio_measurement_yield.csv](../data/derived/expanded_audio_measurement_yield.csv) | Usable calls, eligible answers, exclusions, and review-flag counts for 12 executives. |
| [expanded_audio_metadata_status_summary.csv](../data/derived/expanded_audio_metadata_status_summary.csv) | Lists which call metadata were included and which identification or metadata items require review. |
| [expanded_audio_prepared_qa_summary.csv](../data/derived/expanded_audio_prepared_qa_summary.csv) | Compares prepared remarks with Q&A delivery in the 259 calls covered by this table. |
| [expanded_audio_primary_examples_robustness.csv](../data/derived/expanded_audio_primary_examples_robustness.csv) | Lists the 177 highlighted answers and whether they remain flagged when audio feature groups are excluded. |

## Exploratory market-outcome linkage

| File | What it contains |
| --- | --- |
| [earnings_call_market_cohort_sensitivity.csv](../data/derived/earnings_call_market_cohort_sensitivity.csv) | Original, added, and pooled company-cohort comparisons. |
| [earnings_call_market_leave_one_company_out.csv](../data/derived/earnings_call_market_leave_one_company_out.csv) | Influence checks that omit one firm at a time. |
| [earnings_call_market_models.csv](../data/derived/earnings_call_market_models.csv) | Pooled model estimates and robustness specifications for the exploratory market linkage. |
| [earnings_call_market_outcomes.csv](../data/derived/earnings_call_market_outcomes.csv) | Call-level behavioral summaries, event timing, and signed market-adjusted returns for 286 earnings calls, including 274 with eligible answer-level scores. |
| [earnings_call_market_summary.json](../data/derived/earnings_call_market_summary.json) | Compact machine-readable results and interpretation boundary. |

## 30-interview production archive

| File | What it contains |
| --- | --- |
| [editorial_responsiveness_chance_adjusted.csv](../data/derived/editorial_responsiveness_chance_adjusted.csv) | Compares speaker changes near camera cuts with overlap expected from randomly shifted times within each video. |
| [event_aligned_overall_rates.csv](../data/derived/event_aligned_overall_rates.csv) | Pooled rates and Wilson intervals for coarse composition change, focus gain, directional shifts, and fine-grained coding sensitivity. |
| [event_aligned_production_measures.csv](../data/derived/event_aligned_production_measures.csv) | 120 speaker-transition events with matched pre, entry, and settled composition codes, exact-window cut counts, audio-turn measures, and uncertainty flags. |
| [event_aligned_rates_by_format_and_cut.csv](../data/derived/event_aligned_rates_by_format_and_cut.csv) | Production measures stratified by video format and whether a cut occurred in the matched frame window. |
| [interview_measures.csv](../data/derived/interview_measures.csv) | Speaker-neutral audio, interaction, visual, production, and quality-control measures for 30 interviews. |
| [multimodal_frame_turn_alignment.csv](../data/derived/multimodal_frame_turn_alignment.csv) | 360 sampled visual observations aligned to active or nearest speech turns. |
| [sample_manifest.csv](../data/derived/sample_manifest.csv) | Public source identifiers, URLs, sampling strata, and screening notes for 30 Bloomberg videos. |
| [speaker_transition_edit_alignment.csv](../data/derived/speaker_transition_edit_alignment.csv) | Each speaker change aligned to the nearest detected camera cut. |
| [video_measure_summary.json](../data/derived/video_measure_summary.json) | Compact totals for the 30-video sample, shots and speaker changes, plus observed and chance camera-cut overlap. |
| [video_measurement_sensitivity.csv](../data/derived/video_measurement_sensitivity.csv) | Stability across scene thresholds and one-, two-, and three-second alignment windows. |
| [video_organizational_measures.csv](../data/derived/video_organizational_measures.csv) | Interview-level audio, visible-behavior, production, and cross-modal measures for the 30-video pilot. |
| [video_shot_dynamics.csv](../data/derived/video_shot_dynamics.csv) | Continuous shot counts, shot-duration distributions, and camera-cut alignment with speaker transitions. |
| [video_shot_segments.csv](../data/derived/video_shot_segments.csv) | Timestamped shot boundaries from the primary scene-change specification. |
| [video_variable_recipes.csv](../data/derived/video_variable_recipes.csv) | Construct-neutral definitions, possible uses, validation status, and limitations for video measures. |

## Definitions and compact summaries

| File | What it contains |
| --- | --- |
| [pilot_scale.csv](../data/derived/pilot_scale.csv) | Sample-size table listing calls, executives, answers, interviews, hours, turns, and sampled frames. |
| [pilot_summary_statistics.json](../data/derived/pilot_summary_statistics.json) | Compact counts and descriptive summaries for both pilots. |
| [validation_plan.csv](../data/derived/validation_plan.csv) | Proposed validation designs for 19 measure families and pipeline layers. |
| [variable_dictionary.csv](../data/derived/variable_dictionary.csv) | Definitions, provenance, recommended status, validation targets, and limitations for 74 fields. |

## Eight additional repeated-interviewer interviews

The [repeated-interviewer guide](repeated_interviewer.md) defines the sample, features, reference rules, and limitations. Its [data folder](../data/derived/repeated_interviewer/) contains:

| File | What it contains |
| --- | --- |
| [francine_audio_transcript_profiles.csv](../data/derived/repeated_interviewer/francine_audio_transcript_profiles.csv) | Per-interview numeric inputs used to calculate transcript, turn-taking, and voice scores. |
| [francine_multimodal_deviation_profiles.csv](../data/derived/repeated_interviewer/francine_multimodal_deviation_profiles.csv) | The interviewer’s departure scores across channels: the values plotted in Figure 3. |
| [francine_nonvisual_domain_deviations.csv](../data/derived/repeated_interviewer/francine_nonvisual_domain_deviations.csv) | Feature-by-feature standardized departures and combined scores for transcript, timing, and voice. |
| [francine_speaker_role_audit.csv](../data/derived/repeated_interviewer/francine_speaker_role_audit.csv) | Records of checks on automatic interviewer/interviewee assignments, without transcript quotations. |
| [francine_speaker_state_coverage.csv](../data/derived/repeated_interviewer/francine_speaker_state_coverage.csv) | Counts of observable frames while the interviewer speaks or listens, showing where visual scores have enough evidence. |
| [francine_speaker_state_deviations.csv](../data/derived/repeated_interviewer/francine_speaker_state_deviations.csv) | Separate visible-speaking/listening scores and original bootstrap intervals. |
| [manifest.csv](../data/derived/repeated_interviewer/manifest.csv) | Public source IDs, dates, durations, interviewer, and interviewees. |
| [speaker_role_overrides.csv](../data/derived/repeated_interviewer/speaker_role_overrides.csv) | Recorded corrections to automatic role assignments, without quotations. |
| [video_episode_comparison.csv](../data/derived/repeated_interviewer/video_episode_comparison.csv) | Scores under alternate visibility and adjustment specifications. |
| [video_observability_coverage.csv](../data/derived/repeated_interviewer/video_observability_coverage.csv) | Coverage under the alternate sampling specifications. |
| [video_production_aware_summary.json](../data/derived/repeated_interviewer/video_production_aware_summary.json) | Summary of eligible interviews and how their rankings change under alternative handling of unavailable visual evidence. |
| [visual_feature_calibration.csv](../data/derived/repeated_interviewer/visual_feature_calibration.csv) | Adjusted feature averages and reference scales needed to recalculate the visual scores. |

## Code, figures, and verification

| File | What it contains |
| --- | --- |
| [Figures](../figures/README.md) | The three submission figures and supporting robustness/production figures. |
| [Earnings scoring implementation](../scripts/score_earnings_answers.py) | Transformations, eligibility, and reference rules. |
| [Submission verification](../scripts/verify_submission_evidence.py) | Reconstruct profiles and check the reported sample and score counts. |
| [Figure 3 builder](../scripts/build_submission_video_figure.py) | Redraw the repeated-interviewer heatmap with Matplotlib and NumPy. |
| [Summary script](../scripts/summarize_pilot.py) | Regenerate the compact descriptive summaries. |
| [Reproducibility guide](reproducibility.md) | Verification commands and full-pipeline requirements. |
| [Release manifest](../research_object_manifest.json) | File checksums and recorded model information. |

## Historical material

[Earlier five-executive pilot](../data/earlier_pilot/README.md): the original 118-call, 1,260-answer examples, retained for the research record. These are separate from the submitted 12-executive panel.

Full source recordings, extracted frames, verbatim transcripts, face embeddings, and credentials are excluded, apart from the short audio excerpt and transcript embedded in the worked-example video.
