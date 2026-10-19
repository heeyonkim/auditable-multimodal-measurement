# Five-minute reviewer tour

This repository is a proposal-stage demonstration of a general scientific workflow: converting recordings into inspectable evidence, allowing researchers to define and contest construct mappings, and retaining provenance and validation boundaries. It is not a finished substantive paper and does not depend on a single significant outcome.

## Minute 1 — See the scientific object

Open `tools/measure-specification-prototype/index.html`. Choose among four worked recipes:

- conversational space;
- personal-baseline behavioral deviation;
- editorial responsiveness; and
- delivery–text divergence.

Change the construct, evidence layers, operational rule, rivals, or validation tests. The interface updates the claim boundary and readiness assessment, then exports a versioned JSON recipe. The key design principle is visible: AI extracts observations; researchers remain responsible for defining constructs and evaluating validity.

## Minute 2 — Inspect scale and variation

Open `data/derived/pilot_summary_statistics.json`, `figures/figure_9_expanded_audio_panel.png`, and `figures/figure_10_expanded_audio_robustness.png`.

- The earnings-call pilot contains 286 usable calls, 12 executives, and 3,273 eligible executive answers. The same prespecified recipe was applied throughout.
- The video pilot contains 30 interviews, 8.6 hours of material, 1,208 speaker turns, and 360 aligned frame observations across four production formats.

These pilots demonstrate that the workflow operates beyond hand-selected clips. The archive is still a feasibility sample, not a population estimate.

## Minute 3 — Inspect measures a transcript cannot supply

Open `figures/figure_11_event_aligned_production_responsiveness.png`, `data/derived/event_aligned_production_measures.csv`, and the two variable-recipe tables.

Examples include deviation from a speaker's own delivery baseline, response latency, vocal modulation, delivery–text divergence, framing, shot dynamics, and temporal coupling between camera cuts and changes in conversational floor. The event-aligned extension shows the distinction between detecting a cut and determining whether it changes the broad visible composition: 59 of 82 exact-window cuts changed composition class, whereas 23 preserved it. None of the 38 events without a detected cut changed class. Each recipe states possible uses, validation needs, and interpretations that the measure cannot support.

## Minute 4 — Inspect a worked bridge to outcomes

Open `docs/proximal_outcome_pilot.md` and `data/derived/answer_space_robustness.csv`.

Across 304 eligible question–answer pairs in 27 videos, longer questions, longer response latencies, and nearby camera cuts are associated with more subsequent conversational space within videos. The pooled directions survive alternative eligibility thresholds and leave-one-video-out checks, while format-specific estimates remain heterogeneous. The repository also retains held-out tests in which extra modalities did not improve prediction. This is a descriptive feasibility bridge, not a causal conclusion.

## Minute 5 — Verify the object and examine its frontier

Run:

```bash
python scripts/summarize_pilot.py --data-dir data/derived --output summary_check.json
python scripts/verify_research_object.py --check
```

Then read `docs/research_opportunity_map.md`. It shows how future researchers can connect the infrastructure to organizational outcomes and stronger designs without treating model labels as facts.

## What the prototype establishes

- **Novelty:** constructs can be specified as versioned, contestable recipes over multimodal evidence rather than fixed black-box labels.
- **Feasibility and scale:** two dissimilar audiovisual corpora have been processed into analysis-ready, time-aligned measures.
- **Auditability:** the release retains definitions, rivals, negative tests, provenance gaps, and per-file checksums.
- **Adoption potential:** researchers can reuse the prototype and flat tables without committing to the authors' preferred construct.

## What remains for Stage 2

- pin all model and package versions in a full-pipeline release;
- validate selected measures with trained human coders and external ground truth where available;
- estimate reliability and measurement invariance across speakers, settings, recording systems, and relevant groups;
- move from the deliberately varied repeated-speaker panel to a sampling design suitable for population claims; and
- preregister a small number of theory-facing recipes before linking them to outcomes.

## Nonclaims

The prototype does not infer deception, emotion, confidence, intent, personality, cultural typicality, or editorial intention. Descriptive temporal associations do not establish causal effects. These boundaries are part of the artifact rather than caveats left to prose.
