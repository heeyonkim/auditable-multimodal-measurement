# Video-interview pilot

[Home](../README.md) / [Documentation](README.md) / Video-interview pilot

The pilot examines what can be measured from produced interviews and how camera cuts and participant visibility affect what researchers can observe. Visible behavior and production choices must be recorded separately.

## What the released pilot contains

**30 Bloomberg interviews, 8.6 hours, 1,208 speaker turns, and 360 sampled frame observations**, spanning studio, remote, stage/event, and panel formats. The [source manifest](../data/derived/sample_manifest.csv) identifies the interviews; the [pilot summary](../data/derived/pilot_summary_statistics.json) records the counts.

Camera cuts often occur near changes in speaker. The released summaries report median two-second cut-transition coupling of .659, compared with .171 under within-video circular shifts. This pattern describes production timing; it does not establish an editor's intent or a participant's psychological state.

## Inspect the evidence

| Step | Open | What to look for |
| --- | --- | --- |
| 1. Check the sample | [Source manifest](../data/derived/sample_manifest.csv) · [Production-format figure](../figures/supporting_figure_S4_production_formats.png) | Variation in interviews and production formats |
| 2. Inspect measures | [Interview measures](../data/derived/interview_measures.csv) · [Variable dictionary](../data/derived/variable_dictionary.csv) | Interaction, voice, visible behavior, quality, and definitions |
| 3. Inspect production timing | [Shot dynamics](../data/derived/video_shot_dynamics.csv) · [Chance-adjusted responsiveness](../data/derived/editorial_responsiveness_chance_adjusted.csv) | Camera-cut alignment and the within-video comparison |
| 4. Check sensitivity | [Measurement sensitivity](../data/derived/video_measurement_sensitivity.csv) | Different scene thresholds and alignment windows |
| 5. Review event-aligned evidence | [Results and figure](event_aligned_video_results.md) · [Event table](../data/derived/event_aligned_production_measures.csv) | Whether a detected cut changes the broad visible composition |
| 6. Consider new measures | [Video measurement recipes](../data/derived/video_variable_recipes.csv) | Possible uses, validation needs, and claim boundaries |

## Separate repeated-interviewer demonstration

The submission also analyzes eight additional *Leaders with Lacqua* interviews, separate from this 30-interview archive. See the [repeated-interviewer guide](repeated_interviewer.md) for Figure 3, within-person profiles, and ranking sensitivity.

## Go deeper

The event-aligned extension studies **120 speaker-transition events** using matched frames before, shortly after, and after settling into a transition. Read the [frozen measurement specification](event_aligned_video_measurement.md) before the [detailed results](event_aligned_video_results.md).

Sampled frames do not provide continuous tracking. An off-camera person is unobservable, and a visible person is not necessarily the active speaker. Source media and extracted frames are excluded from this release. See [methods and limitations](submission_technical_appendix.md).

**Next:** [Earnings-call pilot](earnings_call_pilot.md) · [Researcher walkthrough](researcher_walkthrough.md) · [All documentation](README.md)
