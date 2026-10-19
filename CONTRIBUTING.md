# Contributing

This repository is a proposal-stage research object. Changes must preserve both computational integrity and the scientific claim boundary.

## Before making a change

1. Do not add source media, extracted frames, verbatim transcripts, credentials, cookies, tokens, or machine-specific paths.
2. Treat files in `data/derived/` as released evidence. Document the source, transformation, unit of analysis, exclusions, and validation status for any new or replaced table.
3. Describe observable properties rather than inferring emotion, confidence, intent, personality, cultural typicality, deception, editorial intention, or causal effects.
4. Keep the public checks dependency-free unless a dependency is scientifically necessary and pinned.

## Local checks

Run:

```bash
make check
```

If an intentional change affects a released file, rebuild the manifest only after reviewing the full diff:

```bash
python3 scripts/verify_research_object.py
python3 scripts/verify_research_object.py --check
```

The first command rewrites `research_object_manifest.json`. A passing checksum is not evidence that a scientific or privacy review has occurred, so review the release checklist and claim boundaries separately.

## Pull-request checklist

- Explain the research purpose and unit of analysis.
- Identify all added or changed data fields.
- State provenance, exclusions, uncertainty, and validation status.
- Include or update a regression test.
- Confirm that `make check` passes.
- Confirm that no private or licensed source content has been added.
