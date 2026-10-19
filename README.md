# Auditable multimodal measurement

A proposal-stage research repository showing how audiovisual records can be transformed into time-aligned, construct-neutral observations while preserving provenance, uncertainty, and validation requirements.

> **Start here:** Read the [five-minute reviewer tour](docs/reviewer_tour.md). It points to the strongest evidence, the working prototype, and the limits of the current release.

## What this repository demonstrates

The project combines two pilot settings:

- **Earnings calls:** 12 executives, 286 calls, and 3,273 eligible answers.
- **Bloomberg interviews:** 30 interviews, 360 aligned frame observations, and 120 event-aligned speaker transitions.

The release supports feasibility, auditability, descriptive variation, and construct development. It does not claim that automated measures reveal psychological states or causal effects.

## Quick tour

1. Read the [reviewer tour](docs/reviewer_tour.md) for the main argument and evidence.
2. Browse the [figures](figures/) for the proposal-level results.
3. Review the [methods](docs/methods.md) and [reproducibility guide](docs/reproducibility.md).
4. Open `tools/measurement-recipe-studio/index.html` locally to explore the construct-specification prototype.
5. Use the [full data and artifact catalog](docs/data_catalog.md) only when you need the detailed inventory.

## Repository map

| Location | Purpose |
| --- | --- |
| `data/derived/` | Sanitized derived measures and robustness checks |
| `figures/` | Eleven proposal-ready descriptive figures |
| `docs/` | Reviewer tour, methods, results, and detailed catalog |
| `tools/measurement-recipe-studio/` | Dependency-free browser prototype |
| `scripts/` and `tests/` | Summary reproduction and integrity checks |
| `research_object_manifest.json` | Checksums, schemas, provenance status, and claim boundaries |

## Verify the snapshot

The repository requires only Python 3.10 or newer:

```bash
make check
```

This runs the regression tests, reproduces the checked-in summary, verifies every released file against its SHA-256 checksum, and scans text files for common path or credential leaks.

## Scientific boundary

The released fields describe observable or mechanically derived properties of recordings. They do not establish emotion, confidence, intent, personality, cultural typicality, deception, editorial intention, or causal effects.

Camera cuts, framing, and shot duration describe the produced interview rather than stable characteristics of the interviewee. Response latency and answer duration describe conversational timing and floor allocation; they do not independently identify cognition or question difficulty.

## Privacy and licensing

No source videos, audio, extracted frames, verbatim transcripts, credentials, or API keys are included. No open-source or open-data license has been selected yet; see [licensing status](LICENSE.md).

## Project development

- [Roadmap](ROADMAP.md)
- [Contributing guidance](CONTRIBUTING.md)
- [Release checklist](docs/release_checklist.md)
- [Detailed research-object documentation](docs/research_object_manifest.md)
