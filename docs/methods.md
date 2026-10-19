# Methods overview

## Data flow

1. Select public videos using predefined duration and production-format strata.
2. Preserve source identifiers, URLs, durations, and preparation metadata.
3. Extract mono 16 kHz audio and time-spread video frames.
4. Transcribe and diarize speech, retaining anonymous speaker identifiers and timestamps.
5. Group consecutive same-speaker segments into turns.
6. Compute speaker-neutral interaction and acoustic measures.
7. Code sampled frames using a structured observational schema that requires explicit uncertainty notes.
8. Align each sampled frame to the active or nearest diarized speech turn.
9. Detect continuous scene changes and align camera cuts to speaker transitions.
10. Compare observed cut-transition coupling with a circular-shift null that preserves the spacing of speaker transitions while breaking their alignment with the editing timeline.
11. For the event-aligned extension, sample matched frames before, shortly after, and after settling into a speaker transition; code coarse visible composition; and compare the codes with cuts detected in the exact frame window.
12. Export flat, analysis-ready tables and a variable dictionary.

## Measurement levels

- **Interview:** aggregate participation, turn structure, vocal delivery, production context, visible behavior, visual dynamics, and quality control.
- **Turn:** anonymous speaker, start and end times, duration, latency, gaps, speaking rate, pitch, intensity, transcript-observable fillers, and quality flags.
- **Frame-turn:** visual observation at a known timestamp plus the active or nearest diarized speech turn.
- **Transition event:** matched pre, entry, and settled composition classes, exact-window cut counts, incoming-turn acoustic and timing measures, and model uncertainty.
- **Produced interview:** shot frequency, shot duration, camera-cut timing around speaker transitions, and chance-adjusted editorial responsiveness.

## Primary and exploratory fields

Speaker-neutral identifiers and measures are primary outputs, subject to their stated validation requirements. Automatic interviewer and guest labels are exploratory because the pilot revealed role ambiguity. The variable dictionary records the recommended status of every shared field.

## Known structural limits

- Exclusive diarization cannot estimate reliable overlap or interruption duration.
- Automatic transcription can omit or normalize disfluencies.
- Pitch and intensity are sensitive to recording systems and production choices.
- Twelve sampled frames per interview do not provide continuous visual tracking.
- A visible person is not necessarily the active speaker.
- Camera choice and editing are part of the data-generating process.
- Scene-change thresholds and cut-transition time windows are measurement choices and require sensitivity analysis.
- Temporal coupling between cuts and turns does not identify editorial intent or a causal effect.
