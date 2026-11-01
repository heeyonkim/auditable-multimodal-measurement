# Making Organizational Behavior Observable: An Auditable Multimodal Infrastructure for Measuring Behavior from Audio and Video

An AI-assisted measurement architecture for studying organizational audio and video. Its evidence layer aligns observations by person, time, and channel and links them to the recording. Its measure-specification layer records how researchers combine those observations into measures they can inspect, revise, and validate.

The submission demonstrates the approach using **286 earnings calls from 12 executives**, **30 video interviews**, and **eight additional interviews with the same interviewer**.

[Read the submitted proposal](docs/Making_Organizational_Behavior_Observable_Proposal.pdf) · Submitted to *Organization Science* on 1 November 2026.

## Start here

| What would you like to do? | Open |
| --- | --- |
| Follow a researcher's workflow | [Worked example and researcher guide](docs/researcher_walkthrough.md) |
| Try defining a measure | [Interactive prototype](tools/measure-specification-prototype/README.md) |
| Inspect the submission's results | [Submission evidence](docs/README.md) |
| Review methods, limits, and verification | [Technical appendix](docs/submission_technical_appendix.md) |

[Watch the 84-second narrated worked example](docs/media/researcher_walkthrough.mp4): follow one Tim Cook answer from source audio and transcript to feature-level measurements, robustness checks, and an exported observation. [Read the example and measurement notes](docs/researcher_walkthrough.md).

The repository contains the measurement-specification prototype, derived data, figures, technical appendix, and researcher guide described in the submitted proposal. The browser prototype lets researchers define and export measurement specifications. The released scripts reproduce summaries and check derived results. A complete guided interface for processing new recordings is planned for Stage 2. [What you can run and reproduce](docs/reproducibility.md).

Full source recordings and verbatim transcripts are excluded, apart from the short audio excerpt and transcript embedded in the worked-example video. Observable departures do not establish emotion, intent, deception, personality, or causal effects. [Access and reproduction requirements](docs/reproducibility.md) · [Licensing status](LICENSE.md)

[Code for reproducing and checking results](scripts/README.md) explains what each script does and how to run the checks.
