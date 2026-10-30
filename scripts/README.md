# Code for reproducing and checking results

[Home](../README.md) / Code

These scripts calculate measures from numeric inputs, summarize the pilot data, redraw Figure 3, and check the released results.

| Script | What it does |
| --- | --- |
| [Calculate earnings-call scores](score_earnings_answers.py) | Calculates answer-level departures from each executive’s usual patterns. A full rescore requires the authorized turn-level input data described in the [technical appendix](../docs/submission_technical_appendix.md). |
| [Summarize pilot data](summarize_pilot.py) | Recalculates descriptive summaries from the released tables. |
| [Draw proposal Figure 3](build_submission_video_figure.py) | Recreates the repeated-interviewer figure from the released data. Requires Matplotlib and NumPy. |
| [Check submission results](verify_submission_evidence.py) | Reconstructs video profiles and checks the reported sample sizes, score counts, robustness results, and rankings. |
| [Check repository files](verify_research_object.py) | Checks that files match the saved inventory and scans for common accidental disclosures. It also rebuilds the inventory after an intentional update. |

## Run the checks

From the repository’s main folder, using Python 3.10 or newer:

```sh
make check
```

This runs the tests, checks the file inventory, and verifies the submission results. These checks use Python’s standard library. See [reproduction instructions](../docs/reproducibility.md) for individual commands and requirements.

The released code verifies derived results. It does not provide a complete pipeline for transcribing and processing new recordings.
