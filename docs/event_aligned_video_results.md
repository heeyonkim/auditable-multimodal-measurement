# Event-aligned video extension: descriptive results

## What was added

The original pilot detected camera cuts continuously. This extension adds a
second, independently generated measure: observable changes in visual
composition across matched frames 1.5 seconds before, 0.75 seconds after, and
3 seconds after a speaker transition. It covers 120 transitions in
12 videos (360 frames) across four
production formats. The primary composition classes are deliberately coarse:
focused single-person view, multiple-person view, or other composition.

## Main descriptive results

- Visible composition changed from the pre-transition to settled frame in
  **49.2%** of events
  (59/120).
- A focused single-person close or medium shot appeared after, but not before,
  the transition in **25.8%** of
  events.
- Multi-person to focused-single shifts occurred in
  **22.5%** of events; the
  reverse shift occurred in **22.5%**.
- Composition changed in **72.0%** of events with a deterministically
  detected cut between the pre and settled frames, compared with
  **0.0%** without such a cut. These are descriptive rates from
  a deliberately balanced measurement sample, not population estimates.
- The model recorded an uncertainty note for **73.3%** of
  frames. The most common topic was posture (218 notes), which the
  production-responsiveness measure does not use; no note explicitly flagged
  ambiguity in person count, shot type, or composition (0 notes).
  All flags are retained rather than silently discarded.

## Defensible claim for the proposal

This demonstrates a variable that transcripts cannot supply: how the produced
visual field reorganizes around conversational events. The pipeline aligns
speaker timing from audio, continuous cuts from video, structured visible
composition from a multimodal model, and acoustic properties of the incoming
turn. Researchers can then define and validate constructs such as production
responsiveness or visual allocation without asking the model to infer hidden
psychological states.

## Limits

- The sample was selected to span formats and low-to-high prior responsiveness;
  it is a measurement demonstration, not a representative Bloomberg estimate.
- A still frame cannot establish who is speaking or why an editor chose a shot.
- Model-coded composition requires human validation before substantive use.
- Audio-derived speaker roles remain exploratory for complex panels and stage
  events.
- Relationships with response latency, speech rate, pitch, or intensity are
  exploratory and are not treated as causal evidence.
