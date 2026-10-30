# Reproducibility and responsible release

[Home](../README.md) / [Documentation](README.md)

## Verify this release

Download and extract the repository, then open a terminal in its main folder. With Python 3.10 or newer installed, run:

```bash
make check
```

If `make` is unavailable, run the same checks directly:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/verify_research_object.py --check
```

To regenerate a summary separately:

```bash
python3 scripts/summarize_pilot.py --data-dir data/derived --output summary_check.json
```

The summary script and checks use the Python standard library. The [data catalog](data_catalog.md) explains the files; the [manifest guide](research_object_manifest.md) explains integrity and provenance.

## Two reproducibility levels

### Derived-data reproduction

The included standard-library summary script recomputes core descriptive results from the shared CSV files. This level does not require source media, model downloads, or credentials.

### Full-pipeline reproduction

A full rerun requires access to the public source recordings, compatible transcription and diarization models, a visual model or substitute, and sufficient local compute. A complete release should pin package versions and record:

- source identifiers and retrieval dates;
- media checksums and preparation settings;
- model names and versions;
- prompts and structured schemas;
- segmentation and threshold parameters;
- run timestamps and nondeterministic settings; and
- exclusions, failures, retries, and manual interventions.

## Credentials

Never commit API keys, Hugging Face tokens, `.env` files, browser cookies, or service-account files. The repository `.gitignore` blocks common credential and media patterns.

## Media and licensing

Public availability does not itself authorize redistribution. The shareable package contains source URLs and derived measures but excludes full recordings, extracted audio, frames, and transcripts. A final public artifact should include only media whose redistribution is permitted, or use synthetic and legally shareable substitutes that exercise the same pipeline.

## Model access

The full artifact should expose model adapters so researchers can substitute accessible models. Proprietary services can be used for demonstration, but the scientific claims should not depend on one inaccessible model. Model-specific results must retain their provenance.

## Privacy and misuse

The artifact should prohibit unsupported inference of deception, emotion, intent, personality, or cultural typicality. Researchers should document consent, privacy, representation, subgroup performance, and foreseeable misuse for each application setting.
