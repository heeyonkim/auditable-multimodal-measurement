# Auditable multimodal measurement prototype

This repository accompanies a proposed research artifact for organizational and social science. It demonstrates how audiovisual recordings can be transformed into time-aligned, construct-neutral observations while preserving provenance, uncertainty, and validation requirements.

The current release is a proposal-stage, derived-data research object. It contains a verified snapshot of the pilot evidence and a dependency-free Measurement Recipe Studio; it is not yet a credential-free reproduction of the private media-processing pipeline.

## Included

- `data/derived/sample_manifest.csv`: public source identifiers, URLs, sampling strata, and screening notes for 30 Bloomberg videos.
- `data/derived/interview_measures.csv`: speaker-neutral audio, interaction, visual, production, and quality-control measures for 30 interviews.
- `data/derived/multimodal_frame_turn_alignment.csv`: 360 sampled visual observations aligned to active or nearest speech turns.
- `data/derived/video_organizational_measures.csv`: interview-level audio, visible-behavior, production, and cross-modal measures for the 30-video pilot.
- `data/derived/video_shot_dynamics.csv`: continuous shot counts, shot-duration distributions, and camera-cut alignment with speaker transitions.
- `data/derived/video_shot_segments.csv`: timestamped shot boundaries from the primary scene-change specification.
- `data/derived/speaker_transition_edit_alignment.csv`: each speaker change aligned to the nearest detected camera cut.
- `data/derived/editorial_responsiveness_chance_adjusted.csv`: observed camera-cut coupling compared with a within-video circular-shift null.
- `data/derived/video_measurement_sensitivity.csv`: stability across scene thresholds and one-, two-, and three-second alignment windows.
- `data/derived/video_variable_recipes.csv`: construct-neutral definitions, possible uses, validation status, and limitations for video measures.
- `data/derived/event_aligned_production_measures.csv`: 120 speaker-transition events with matched pre, entry, and settled composition codes, exact-window cut counts, audio-turn measures, and uncertainty flags.
- `data/derived/event_aligned_overall_rates.csv`: pooled rates and Wilson intervals for coarse composition change, focus gain, directional shifts, and fine-grained coding sensitivity.
- `data/derived/event_aligned_rates_by_format_and_cut.csv`: production measures stratified by video format and whether a cut occurred in the matched frame window.
- `data/derived/variable_dictionary.csv`: definitions, provenance, recommended status, validation targets, and limitations for 74 fields.
- `data/derived/validation_plan.csv`: proposed validation designs for 19 measure families and pipeline layers.
- `data/derived/expanded_audio_measurement_yield.csv`: usable calls, eligible answers, exclusions, and review-flag counts for 12 executives.
- `data/derived/expanded_audio_answer_scores.csv`: 3,273 answer-level continuous scores and specification variants, without transcript text or media.
- `data/derived/expanded_audio_feature_variant_summary.csv`: feature-family and leave-one-feature-out robustness results.
- `data/derived/expanded_audio_eligibility_sensitivity.csv`: stability under stricter answer-length requirements.
- `data/derived/expanded_audio_prepared_qa_summary.csv`: prepared-remarks versus Q&A contrasts across 259 calls.
- `data/derived/expanded_audio_call_concentration.csv`: call-level concentration of review flags.
- `data/derived/expanded_audio_primary_examples_robustness.csv`: specification support for 177 illustrative review flags.
- `data/derived/expanded_audio_candidate_audit.csv`: prespecified tenure windows, selection rationale, aliases, and tenure-source links for the seven-executive expansion.
- `data/derived/expanded_audio_metadata_status_summary.csv`: documented structured-metadata inclusions and review items.
- `data/derived/expanded_audio_archive_validation.json`: private-archive integrity counts without paths or credentials.
- `data/derived/answer_level_organizational_variables.csv`: detailed original-pilot versions of five theory-facing, construct-neutral measures for 1,260 executive answers.
- `data/derived/call_level_organizational_variables.csv`: call-level aggregation of construct-neutral behavioral measures for 118 calls.
- `data/derived/organizational_variable_recipes.csv`: definitions, possible research uses, validation needs, and prohibited interpretations.
- `data/derived/organizational_variable_summary.csv`: pooled and executive-specific descriptive distributions.
- `data/derived/outcome_variable_recipes.csv`: definitions and prohibited interpretations for three proximal outcome families.
- `data/derived/editorial_response_by_transition.csv`: camera-cut response rates by conversational floor transition.
- `data/derived/answer_space_within_video_associations.csv`: exploratory within-video associations with video-cluster bootstrap intervals.
- `data/derived/answer_space_robustness.csv`: alternative cutoffs, production-format heterogeneity, camera-cut windows, and leave-one-video-out influence checks.
- `data/derived/outcome_model_comparison.csv`: held-out diagnostics, including negative incremental-prediction results retained for auditability.
- `data/derived/pilot_summary_statistics.json`: compact counts and descriptive summaries for both pilots.
- `figures/`: eleven proposal-ready descriptive figures, including expanded-panel scale, audio robustness, continuous and event-aligned video measures, and proximal organizational outcomes.
- `scripts/summarize_pilot.py`: portable script that regenerates core summary statistics from the derived tables.
- `scripts/verify_research_object.py`: dependency-free integrity, structure, privacy, and credential verification for the release.
- `research_object_manifest.json`: machine-readable checksums, corpus scope, pipeline status, model provenance, limitations, and prohibited claims.
- `tools/measurement-recipe-studio/`: a dependency-free working interface for defining constructs, selecting observable evidence, retaining rivals, specifying validation, and exporting a versioned recipe.
- `docs/methods.md`: data flow and measurement boundaries.
- `docs/reproducibility.md`: environment, licensing, credential, and rerun guidance.
- `docs/release_checklist.md`: completed privacy, integrity, and portability checks for this snapshot.
- `docs/proximal_outcome_pilot.md`: construct boundaries and interpretation for the worked outcome illustration.
- `docs/event_aligned_video_measurement.md`: the frozen sampling and measurement specification written before event-frame model calls.
- `docs/event_aligned_video_results.md`: descriptive results, scientific claim boundary, and remaining validation requirements.
- `docs/research_object_manifest.md`: explanation of the research-object audit layer and its scientific boundary.
- `docs/research_opportunity_map.md`: eight theory-facing research programs linking new observables to possible outcomes, designs, and claim boundaries.
- `docs/reviewer_tour.md`: a five-minute path through the prototype, evidence, robustness, reproducibility, and remaining Stage 2 work.

## Excluded

The repository does not contain full videos, audio, extracted frames, verbatim transcripts, API keys, model tokens, or local file paths. Source media should not be redistributed without a separate licensing determination.

## Quick start

The repository requires only Python 3.10 or newer. Run the complete local check with:

```bash
make check
```

The command regenerates the pilot summary in a temporary directory, compares it with the checked-in snapshot, runs the repository tests, and verifies every released file against the manifest.

To run the two core commands directly:

```bash
python3 scripts/summarize_pilot.py --data-dir data/derived --output /tmp/pilot-summary.json
python3 scripts/verify_research_object.py --check
```

Both scripts use only the Python standard library. The summary script checks expected row counts and recomputes the central descriptive statistics used in the proposal package. The verifier confirms that every released file matches its recorded SHA-256 checksum and that the snapshot passes the built-in local-path and credential scan.

## Repository map

- `data/derived/` — sanitized pilot outputs; no media or verbatim transcripts.
- `docs/` — methods, reproducibility guidance, reviewer tour, and measurement boundaries.
- `figures/` — proposal-ready descriptive figures.
- `scripts/` — portable summary and release-integrity checks.
- `tests/` — dependency-free regression tests for the public research object.
- `tools/measurement-recipe-studio/` — browser-based construct specification prototype.
- `research_object_manifest.json` — checksums, table schemas, provenance status, and claim boundaries.

See [`ROADMAP.md`](ROADMAP.md) for the next repository milestones and [`CONTRIBUTING.md`](CONTRIBUTING.md) before changing data, documentation, or release metadata.

## Scientific boundary

The released fields describe observable or mechanically derived properties of recordings. They do not establish emotion, confidence, intent, personality, cultural typicality, or deception. Fields marked exploratory depend on automatic functional-role labels or sparse identity assumptions and require validation before substantive use.

Camera cuts, framing, and shot duration describe the produced interview rather than stable characteristics of the interviewee. Chance-adjusted editorial responsiveness indicates temporal coupling beyond an editing-frequency null; it does not reveal an editor's intention or establish a causal effect.

Response latency and answer duration describe conversational timing and floor allocation. They do not, without further validation and research design, identify question difficulty, deliberation, confidence, or cognition.

## Researcher-facing prototype

Open `tools/measurement-recipe-studio/index.html` in a browser. Four worked recipes show how the same evidence archive can support competing construct specifications without turning a model's interpretation into ground truth. Recipe exports preserve the construct definition, unit, evidence layers, operational rule, rival explanations, validation tests, prohibited interpretations, and audit requirements.


## Licensing and citation

No open-source or open-data license has been selected yet. See [`LICENSE.md`](LICENSE.md) for the current terms. Citation metadata will be added once the author list, repository URL, and archival identifier are finalized.
