# Repository roadmap

Aligned with Section 4 of the [proposal submitted on 1 November 2026](docs/Making_Organizational_Behavior_Observable_Proposal.pdf). Stage 2 will extend the working prototype into reusable measurement infrastructure through four areas:

- **Technical benchmarking:** compare speaker identification, timing, vocal features, cuts, visibility, and facial movement with human-reviewed examples; report errors, unavailable evidence, correction needs, processing time, and cost across recording conditions.
- **Measure validation:** evaluate construct measures separately from extraction accuracy, including agreement with human coding, sensitivity to measurement choices, added information beyond transcripts, and performance in new settings.
- **Researcher use:** develop a guided interface for processing recordings, inspecting sources, correcting assignments, comparing specifications, and exporting results; assess independent use by researchers outside the project.
- **Empirical expansion:** enlarge the executive panel, use prior-only personal baselines, define outcome tests in advance, and study repeated executives and interviewers across programs and time.

The release and implementation tasks below support that plan.

## 1. Public foundation — complete

- Promote the sanitized research object to a standalone repository.
- Preserve derived data, figures, methods, and the measure-specification prototype.
- Add dependency-free tests, integrity verification, and continuous checks.
- Document contribution rules, claim boundaries, and current licensing status.

## 2. Archival release — next

- Confirm the author list and preferred citation.
- Choose separate code and data licenses where needed.
- Record the repository URL, tagged release, and archival DOI.
- Pin transcription, diarization, acoustic-analysis, and frame-observation model versions.
- Replace remaining provenance gaps in `research_object_manifest.json`.

## 3. Reproduction package

- Separate public orchestration code from private or licensed source material.
- Add environment lock files and machine-readable pipeline configuration.
- Publish small licensed or synthetic fixtures for end-to-end tests.
- Add adapters that recreate each released table from approved inputs.
- Record deterministic seeds, failure logs, and stage-level checksums.

## 4. Validation expansion

- Run human agreement studies for functional roles and frame observations.
- Validate timing, diarization, and acoustic measures against independent references.
- Add subgroup and production-format measurement-invariance checks.
- Version construct recipes and link each substantive claim to its validation evidence.

## 5. Researcher adoption

- Add searchable field documentation and worked analyses.
- Support recipe comparison, dataset field mapping, and export to statistical software.
- Publish a governance process for proposed variables and prohibited interpretations.
