# Five-minute reviewer tour

[Home](../README.md) / [Documentation](README.md) / Reviewer tour

This proposal-stage prototype turns recordings into inspectable measures. The central contribution is a measurement architecture that preserves evidence and researcher choices, demonstrated through two pilots.

## 1. Understand the workflow

Read the [worked researcher example](researcher_walkthrough.md#a-worked-earnings-call-example). A researcher defines the question, chooses observations and a baseline, inspects evidence, and freezes a measurement recipe before analysis.

The [video preview](media/researcher_walkthrough.mp4) presents the workflow in two minutes. The author's voice recording is pending.

## 2. Inspect the earnings-call pilot

Open the [earnings-call guide](earnings_call_pilot.md). The panel contains 286 calls, 12 executives, and 3,273 eligible answers. Of 177 answers with unusual delivery or timing and relatively typical transcript language, 172 retain support under at least two feature-family exclusions.

Follow the guide's direct links from coverage to answer scores and robustness. These are cases for investigation, not validated psychological labels.

## 3. Inspect the video-interview pilot

Open the [video-interview guide](video_interview_pilot.md). Thirty interviews across four production formats demonstrate the need to distinguish visible behavior from camera choices and unavailable observations.

The [event-aligned results](event_aligned_video_results.md) provide a detailed extension: 59 of 82 exact-window cuts changed broad composition class, while 23 preserved it. None of the 38 events without a detected cut changed class. Detecting a cut and detecting a composition change are different measurements.

## 4. Try a measurement recipe

Follow the [prototype opening instructions](../tools/measure-specification-prototype/README.md). Choose conversational space, personal-baseline behavioral deviation, editorial responsiveness, or delivery–text divergence. Change the observations, operational rule, rival explanations, or validation tests, then export a versioned recipe.

The prototype illustrates measure specification. It does not process new recordings or validate a construct.

## 5. Check what is reproducible and what remains

Use the [verification instructions](reproducibility.md#verify-this-release) to reproduce shared summaries and check the release manifest. Read the [methods and limits](methods.md) and [roadmap](../ROADMAP.md) for remaining work on extraction accuracy, human validation, subgroup performance, and broader sampling.

The release supports derived-data verification. It excludes source recordings and transcripts and does not provide a complete credential-free media rerun.

## Optional further reading

- [Market-outcome linkage](earnings_call_market_outcome.md): an exploratory, imprecise, cohort-sensitive extension, not the central demonstration.
- [Research opportunities](research_opportunity_map.md): possible future questions and designs.
- [Complete data catalog](data_catalog.md): the detailed artifact inventory.

The prototype does not establish emotion, confidence, deception, intent, personality, cultural typicality, editorial intention, or causal effects.
