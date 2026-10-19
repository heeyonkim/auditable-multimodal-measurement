# Reproducibility and responsible release

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
