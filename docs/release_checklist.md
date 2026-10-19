# Release checklist

Snapshot checked on September 27, 2026.

## Expanded audio panel

- The repeated-speaker panel contains 12 executives, 286 calls meeting baseline requirements, and 3,273 eligible Q&A answers.
- The seven-executive expansion retrieved 182 of 182 selected calls with complete audio, transcript, and structured metadata files and no partial files or retrieval failures.
- Ten selected calls remain documented metadata-review items; they were not assigned focal-speaker evidence by assumption.
- Feature-family exclusions and stricter answer-length rules are released alongside the primary continuous score.

## Data integrity

- 30 unique interviews are present in the sample manifest and interview-level table.
- 360 frame-turn rows are present, with 12 sampled frames per interview.
- 355 sampled frames occur during detected speech.
- Continuous analysis detected 2,451 shots across 8.6 hours and aligned 1,178 speaker transitions with the editing timeline.
- Median two-second cut-transition coupling was .659, compared with .171 under within-video circular shifts; chance-adjusted responsiveness was positive in 27 of 30 videos.
- A second scene threshold and one-, two-, and three-second timing windows are included as sensitivity evidence.
- The portable summary script reproduces the counts and proposal-level descriptive statistics.
- Public identifiers and source URLs are retained so provenance can be audited.

## Privacy and credentials

- No local file paths are included in the released tables or documentation.
- No API keys, access tokens, browser cookies, or service-account files are included.
- No full video, audio, extracted frame, or verbatim transcript is included.
- Source media licensing must be assessed separately before any redistribution.

## Interpretive limits

- The release makes no automatic inference about emotion, confidence, intent, personality, culture, or deception.
- Speaker-neutral interaction measures are the primary outputs.
- Functional-role labels and measures derived from them are exploratory until independently validated.
- Sampled visual observations are not continuous behavior tracking.
- Temporal alignment does not establish that the person visible on screen is the active speaker.
- Camera cuts and framing are production measures, not interviewee traits or evidence of an editor's intention.

## Portability

- `scripts/summarize_pilot.py` uses only the Python standard library.
- Derived data use open CSV and JSON formats.
- The repository contains no machine-specific dependency paths.
