# Machine-verifiable research object

[Home](../README.md) / [Documentation](README.md)

This proposal-stage repository is packaged as a small research object rather than a folder of illustrative outputs. The root-level `research_object_manifest.json` records each released file's SHA-256 checksum, size, and lightweight structural metadata. It also records corpus scope, pipeline status, model provenance, known limitations, and prohibited interpretations.

## Verify the release

From the repository root, run:

```bash
python scripts/verify_research_object.py --check
```

The command uses only the Python standard library. It fails if a released file is missing, added, or changed, or if the current snapshot contains a common credential pattern or an absolute macOS user path.

## Rebuild after an intentional change

After reviewing an intentional edit, rebuild and then verify the manifest:

```bash
python scripts/verify_research_object.py
python scripts/verify_research_object.py --check
```

The manifest excludes itself, compressed packages, cache files, and version-control internals. It is an integrity and release-hygiene layer; it does not certify construct validity, model accuracy, licensing, or causal identification.

## Provenance status

The visual run metadata identify `gemini-3.8-flash` for structured sampled-frame observation. The sanitized snapshot does not contain exact transcription and diarization model versions. Rather than infer them, the manifest marks them as not recorded and makes version pinning a requirement for an archival release. This is a deliberate demonstration of transparent missing provenance.

## Why this matters scientifically

The manifest separates three questions that are often blurred in AI-enabled research:

1. **Integrity:** Is this exactly the object the authors reported?
2. **Computational reproducibility:** Can the released derived results be recomputed?
3. **Measurement validity:** Does a recipe measure the proposed construct in the intended setting?

Checksums and scripts address the first two. The measure-specification prototype, validation designs, rival explanations, and domain evidence address the third. No manifest can substitute for construct validation.
