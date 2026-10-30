# Data and artifact catalog

[Home](../README.md) / [Documentation](README.md)

This catalog contains the detailed inventory for the proposal-stage research object. Most readers should begin with the [repository home](../README.md) or the [five-minute reviewer tour](reviewer_tour.md).

## Pilot guides

For a shorter route through the evidence, use the [earnings-call guide](earnings_call_pilot.md), [video-interview guide](video_interview_pilot.md), or [figure index](../figures/README.md).

## Released files

- [data/derived/sample_manifest.csv](../data/derived/sample_manifest.csv): public source identifiers, URLs, sampling strata, and screening notes for 30 Bloomberg videos.
- [data/derived/interview_measures.csv](../data/derived/interview_measures.csv): speaker-neutral audio, interaction, visual, production, and quality-control measures for 30 interviews.
- [data/derived/multimodal_frame_turn_alignment.csv](../data/derived/multimodal_frame_turn_alignment.csv): 360 sampled visual observations aligned to active or nearest speech turns.
- [data/derived/video_organizational_measures.csv](../data/derived/video_organizational_measures.csv): interview-level audio, visible-behavior, production, and cross-modal measures for the 30-video pilot.
- [data/derived/video_shot_dynamics.csv](../data/derived/video_shot_dynamics.csv): continuous shot counts, shot-duration distributions, and camera-cut alignment with speaker transitions.
- [data/derived/video_shot_segments.csv](../data/derived/video_shot_segments.csv): timestamped shot boundaries from the primary scene-change specification.
- [data/derived/speaker_transition_edit_alignment.csv](../data/derived/speaker_transition_edit_alignment.csv): each speaker change aligned to the nearest detected camera cut.
- [data/derived/editorial_responsiveness_chance_adjusted.csv](../data/derived/editorial_responsiveness_chance_adjusted.csv): observed camera-cut coupling compared with a within-video circular-shift null.
- [data/derived/video_measurement_sensitivity.csv](../data/derived/video_measurement_sensitivity.csv): stability across scene thresholds and one-, two-, and three-second alignment windows.
- [data/derived/video_variable_recipes.csv](../data/derived/video_variable_recipes.csv): construct-neutral definitions, possible uses, validation status, and limitations for video measures.
- [data/derived/event_aligned_production_measures.csv](../data/derived/event_aligned_production_measures.csv): 120 speaker-transition events with matched pre, entry, and settled composition codes, exact-window cut counts, audio-turn measures, and uncertainty flags.
- [data/derived/event_aligned_overall_rates.csv](../data/derived/event_aligned_overall_rates.csv): pooled rates and Wilson intervals for coarse composition change, focus gain, directional shifts, and fine-grained coding sensitivity.
- [data/derived/event_aligned_rates_by_format_and_cut.csv](../data/derived/event_aligned_rates_by_format_and_cut.csv): production measures stratified by video format and whether a cut occurred in the matched frame window.
- [data/derived/variable_dictionary.csv](../data/derived/variable_dictionary.csv): definitions, provenance, recommended status, validation targets, and limitations for 74 fields.
- [data/derived/validation_plan.csv](../data/derived/validation_plan.csv): proposed validation designs for 19 measure families and pipeline layers.
- [data/derived/expanded_audio_measurement_yield.csv](../data/derived/expanded_audio_measurement_yield.csv): usable calls, eligible answers, exclusions, and review-flag counts for 12 executives.
- [data/derived/expanded_audio_answer_scores.csv](../data/derived/expanded_audio_answer_scores.csv): 3,273 answer-level continuous scores and specification variants, without transcript text or media.
- [data/derived/expanded_audio_feature_variant_summary.csv](../data/derived/expanded_audio_feature_variant_summary.csv): feature-family and leave-one-feature-out robustness results.
- [data/derived/expanded_audio_eligibility_sensitivity.csv](../data/derived/expanded_audio_eligibility_sensitivity.csv): stability under stricter answer-length requirements.
- [data/derived/expanded_audio_prepared_qa_summary.csv](../data/derived/expanded_audio_prepared_qa_summary.csv): prepared-remarks versus Q&A contrasts across 259 calls.
- [data/derived/expanded_audio_call_concentration.csv](../data/derived/expanded_audio_call_concentration.csv): call-level concentration of review flags.
- [data/derived/expanded_audio_primary_examples_robustness.csv](../data/derived/expanded_audio_primary_examples_robustness.csv): specification support for 177 illustrative review flags.
- [data/derived/expanded_audio_candidate_audit.csv](../data/derived/expanded_audio_candidate_audit.csv): prespecified tenure windows, selection rationale, aliases, and tenure-source links for the seven-executive expansion.
- [data/derived/expanded_audio_metadata_status_summary.csv](../data/derived/expanded_audio_metadata_status_summary.csv): documented structured-metadata inclusions and review items.
- [data/derived/expanded_audio_archive_validation.json](../data/derived/expanded_audio_archive_validation.json): private-archive integrity counts without paths or credentials.
- [data/derived/answer_level_organizational_variables.csv](../data/derived/answer_level_organizational_variables.csv): detailed original-pilot versions of five theory-facing, construct-neutral measures for 1,260 executive answers.
- [data/derived/call_level_organizational_variables.csv](../data/derived/call_level_organizational_variables.csv): call-level aggregation of construct-neutral behavioral measures for 118 calls.
- [data/derived/organizational_variable_recipes.csv](../data/derived/organizational_variable_recipes.csv): definitions, possible research uses, validation needs, and prohibited interpretations.
- [data/derived/organizational_variable_summary.csv](../data/derived/organizational_variable_summary.csv): pooled and executive-specific descriptive distributions.
- [data/derived/earnings_call_market_outcomes.csv](../data/derived/earnings_call_market_outcomes.csv): call-level behavioral summaries, event timing, and signed market-adjusted returns for 286 earnings calls, including 274 with eligible answer-level scores.
- [data/derived/earnings_call_market_models.csv](../data/derived/earnings_call_market_models.csv): pooled model estimates and robustness specifications for the exploratory market linkage.
- [data/derived/earnings_call_market_cohort_sensitivity.csv](../data/derived/earnings_call_market_cohort_sensitivity.csv): original, added, and pooled company-cohort comparisons.
- [data/derived/earnings_call_market_leave_one_company_out.csv](../data/derived/earnings_call_market_leave_one_company_out.csv): influence checks that omit one firm at a time.
- [data/derived/earnings_call_market_summary.json](../data/derived/earnings_call_market_summary.json): compact machine-readable results and interpretation boundary.
- [data/derived/pilot_summary_statistics.json](../data/derived/pilot_summary_statistics.json): compact counts and descriptive summaries for both pilots.
- [figures/](../figures/): eleven proposal-ready descriptive figures, including expanded-panel scale, audio robustness, continuous and event-aligned video measures, and the exploratory earnings-call market linkage.
- [scripts/summarize_pilot.py](../scripts/summarize_pilot.py): portable script that regenerates core summary statistics from the derived tables.
- [scripts/verify_research_object.py](../scripts/verify_research_object.py): dependency-free integrity, structure, privacy, and credential verification for the release.
- [research_object_manifest.json](../research_object_manifest.json): machine-readable checksums, corpus scope, pipeline status, model provenance, limitations, and prohibited claims.
- [tools/measure-specification-prototype/](../tools/measure-specification-prototype/): a dependency-free working interface for defining constructs, selecting observable evidence, retaining rivals, specifying validation, and exporting a versioned recipe.
- [docs/methods.md](../docs/methods.md): data flow and measurement boundaries.
- [docs/reproducibility.md](../docs/reproducibility.md): environment, licensing, credential, and rerun guidance.
- [docs/release_checklist.md](../docs/release_checklist.md): completed privacy, integrity, and portability checks for this snapshot.
- [docs/earnings_call_market_outcome.md](../docs/earnings_call_market_outcome.md): design, results, robustness evidence, and interpretation boundaries for the exploratory market linkage.
- [docs/event_aligned_video_measurement.md](../docs/event_aligned_video_measurement.md): the frozen sampling and measurement specification written before event-frame model calls.
- [docs/event_aligned_video_results.md](../docs/event_aligned_video_results.md): descriptive results, scientific claim boundary, and remaining validation requirements.
- [docs/research_object_manifest.md](../docs/research_object_manifest.md): explanation of the research-object audit layer and its scientific boundary.
- [docs/research_opportunity_map.md](../docs/research_opportunity_map.md): eight theory-facing research programs linking new observables to possible outcomes, designs, and claim boundaries.
- [docs/researcher_walkthrough.md](../docs/researcher_walkthrough.md): a worked, nontechnical path from a research question to an auditable dataset through a conversational research assistant.
- [docs/media/researcher_walkthrough.mp4](../docs/media/researcher_walkthrough.mp4): a two-minute preview of the researcher workflow; the author's voice recording is pending.
- [docs/media/researcher_walkthrough_poster.png](../docs/media/researcher_walkthrough_poster.png): the video preview image used on the repository home page.
- [docs/media/researcher_walkthrough_captions.srt](../docs/media/researcher_walkthrough_captions.srt): captions for the narrated walkthrough.
- [docs/reviewer_tour.md](../docs/reviewer_tour.md): a five-minute path through the prototype, evidence, robustness, reproducibility, and remaining Stage 2 work.

## Submission additions

- [300-call screening ledger](../data/derived/earnings_call_screening_ledger.csv): retained calls, 14 initial exclusions, and whether answer summaries are available.
- [Earnings scoring implementation](../scripts/score_earnings_answers.py): transformations, references, eligibility, and score construction.

- [Repeated-interviewer data](../data/derived/repeated_interviewer/): eight-interview manifest, numeric inputs, calibrated feature summaries, profiles, coverage, role corrections, and production sensitivity; see the [measurement guide](repeated_interviewer.md).
- [Submission technical appendix](submission_technical_appendix.md): scope and methods for the current submission.
- [Verification script](../scripts/verify_submission_evidence.py): reconstruction of scores and key reported counts.
- [Figure 3 builder](../scripts/build_submission_video_figure.py): redraw the [submission heatmap](../figures/submission_figure_3_repeated_interviewer.png).

## Excluded source material

The repository does not contain full videos, audio, extracted frames, verbatim transcripts, API keys, model tokens, credentials, or machine-specific paths. Source media should not be redistributed without a separate licensing determination.
