# Earnings-call pilot

[Home](../README.md) / [Documentation](README.md) / Earnings-call pilot

The pilot asks whether an executive's vocal delivery and interaction timing can depart from their usual pattern when transcript language appears relatively typical. Start with the findings below; the tables are linked in the order needed to inspect them.

## What the released pilot contains

**300 collected calls, 286 retained calls, 12 executives across seven sectors, approximately 313 hours of audio, and 3,273 eligible Q&A answers.** Each answer is compared with that executive's personal baseline. The released archive includes continuous scores and alternative specifications.

- **177 answers** have unusual audio or interaction scores while transcript language is relatively typical.
- **172 of those 177** remain unusual under at least two of three feature-family exclusions: timing and speaking rate, pitch, or vocal intensity.
- These are examples for further investigation. Departures do not establish emotion, pressure, intent, truthfulness, or executive quality.

These counts are recorded in the [pilot summary](../data/derived/pilot_summary_statistics.json) and can be regenerated using the [reproduction instructions](reproducibility.md).

## Why compare audio with transcript features?

The audio/interaction measure captures departures in how an answer is delivered and how the exchange unfolds, using speaking rate, response timing, pitch, and vocal intensity. The transcript measure uses answer length, filled pauses, discourse fillers, and adjacent repetitions. It does not analyze meaning or everything that text could reveal.

At the same departure-score cutoff of 2.0, the audio/interaction measure flags **325 answers**, while the transcript measure flags **321**. Only **66** are flagged by both. Thus **259 of the 325 audio/interaction flags (80%)** are not flagged by the selected transcript features. The comparison uses the **3,233 answers with both scores**. It shows that the two approaches direct researchers toward different answers to inspect; it does not establish which measure is better. The 177 highlighted answers in Figure 2 are a stricter subset, additionally requiring transcript departure of no more than 1.25.

[Watch one answer being inspected in the narrated worked example](researcher_walkthrough.md).

## Inspect the evidence

| Step | Open | What to look for |
| --- | --- | --- |
| 1. Check coverage | [Panel figure](../figures/supporting_figure_S1_expanded_audio_panel.png) · [Measurement yield](../data/derived/expanded_audio_measurement_yield.csv) | Calls, eligible answers, and exclusions across executives |
| 2. Inspect answer scores | [Continuous answer-level scores](../data/derived/expanded_audio_answer_scores.csv) | Separate audio/interaction and transcript-visible departures |
| 3. Examine the 177 cases | [Case robustness table](../data/derived/expanded_audio_primary_examples_robustness.csv) | Contributions and support under feature-family exclusions |
| 4. Check sensitivity | [Robustness figure](../figures/supporting_figure_S2_audio_robustness.png) · [Feature variants](../data/derived/expanded_audio_feature_variant_summary.csv) · [Eligibility sensitivity](../data/derived/expanded_audio_eligibility_sensitivity.csv) | Dependence on included features and answer-length requirements |
| 5. Understand possible variables | [Measurement recipes](../data/earlier_pilot/organizational_variable_recipes.csv) | Definitions, research uses, validation needs, and prohibited interpretations |

**Earlier examples:** the [five-executive tables](../data/earlier_pilot/README.md) cover 118 calls. They are separate from the current `expanded_audio_` tables for the 12-executive panel.

## Optional outcome extension

The [market-outcome analysis](earnings_call_market_outcome.md) links the archive to returns, with 274 calls eligible for answer-level analysis. The association is exploratory, imprecise, cohort-sensitive, and noncausal. It demonstrates linkage to outcomes rather than validating the behavioral measure.

## What can be checked here

The repository supplies sanitized measures, specifications, and robustness checks. The worked-example video includes one short source-audio excerpt and its transcript. Full source recordings and transcripts remain excluded, so this snapshot does not support listening to every answer or a complete media-processing rerun. See [methods and limitations](submission_technical_appendix.md) and [reproducibility](reproducibility.md).

**Next:** [Video-interview pilot](video_interview_pilot.md) · [Researcher walkthrough](researcher_walkthrough.md) · [All documentation](README.md)
