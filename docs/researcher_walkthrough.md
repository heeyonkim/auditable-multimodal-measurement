# How a researcher uses the multimodal measurement system

[Home](../README.md) / [Documentation](README.md)

In its current form, a researcher uses the system through a conversational research assistant. The researcher begins with an organizational question, reviews the measurement choices, inspects examples, and decides what can be claimed. The assistant operates the underlying workflow, produces analysis-ready outputs, and preserves an audit trail.

Researchers do not need to begin with the repository or a command line. The repository is the verification layer: it lets collaborators and reviewers inspect how the measures were created, what evidence supports them, and where the limits are.

## A prompt to begin

A researcher can start with a prompt like this:

> I am studying **[organizational phenomenon]** using **[type of recordings]**. I want to compare **[people, events, periods, or settings]**. Help me separate the theoretical construct from what the recordings can directly show, propose one or more measurable recipes, identify the decisions I need to make, and show me examples before applying a recipe to the full dataset.

No technical vocabulary is required. The assistant should ask only the questions that materially change the measurement design, explain the consequences of each choice, and preserve the approved choices in the research record.

## A worked earnings call example

Suppose a researcher asks:

> Do chief executives depart from their usual speaking behavior when responding to analysts, and does that deviation contain information beyond the transcript?

The question names a theoretical interest, but it does not yet define a measurable variable. The assistant helps turn it into an explicit recipe before running a large analysis.

| Stage | Researcher contribution | Assistant and system contribution | Output for review |
| --- | --- | --- | --- |
| Frame the question | Explain the theoretical motivation and intended comparison | Separate the theoretical construct from what recordings can directly reveal | A narrow research question and a list of prohibited interpretations |
| Choose the observations | Decide whose behavior matters, which part of the call to study, and what counts as an observation | Inventory the recordings and propose feasible units such as an executive answer or an entire Q&A session | A documented sample and unit of analysis |
| Specify the baseline | Choose a trailing or leave-one-call-out personal baseline and decide which calls qualify | Calculate each executive's reference distribution while preserving the selected comparison rule | A versioned personal-baseline specification |
| Select evidence | Decide whether timing, speaking rate, pitch, intensity, transcript features, or other channels belong in the measure | Extract and align the selected observations without assigning psychological meaning to them | Time-aligned, construct-neutral measurements |
| Inspect examples | Judge whether flagged examples match the intended observational rule and identify rival explanations | Present source-linked segments, component scores, quality flags, and transcript comparisons | An evidence review rather than a black-box score |
| Freeze and scale the recipe | Approve the rule, exclusions, aggregation, and validation plan before outcome testing | Apply the same recipe across the eligible archive and record failures and exclusions | Answer-level and call-level variables with provenance |
| Analyze and report | Select an empirical design, outcomes, controls, and defensible interpretation | Produce tables, figures, sensitivity checks, and reproducible analysis files | A research package that can be audited and revised |

## What the conversation could look like

**Researcher:** I want to know whether executives sound different when analysts put them under pressure.

**Assistant:** Recordings can show departures in delivery and interaction, but they cannot by themselves establish pressure, anxiety, confidence, or deception. A defensible starting measure would compare each executive's Q&A answers with that executive's own behavior in other calls. We could measure response latency, speaking-rate change, long gaps, pitch, and intensity, while retaining a separate transcript-visible score. Would you like the unit to be each answer or the call as a whole?

**Researcher:** Start with each answer. Exclude very short answers and show me cases where delivery is unusual but the transcript looks routine.

**Assistant:** I will use the answer as the unit, apply the documented eligibility threshold, calculate audio and interaction deviation relative to the executive's personal baseline, and retain the transcript-visible comparison separately. Before scaling, I will show examples with the source interval, component contributions, and quality flags.

**Researcher:** The examples look reasonable, but use the median answer deviation for the main call-level measure and retain the upper-tail measure as a robustness check.

**Assistant:** I will record that aggregation choice in the recipe, apply it across the archive, and export the call-level variable, answer-level evidence, exclusions, variable definition, and validation requirements. We can then specify an outcome analysis without changing the measurement rule after seeing the result.

The exchange is collaborative by design. The assistant makes the technical workflow usable, but the researcher remains responsible for construct definition, sampling, validation, and interpretation.

## What the researcher receives

A completed run should return a compact research package rather than a folder of unexplained technical files:

- an analysis-ready table at the chosen unit of analysis;
- a plain-language variable definition and versioned measurement recipe;
- source identifiers, timestamps, exclusions, failures, and quality flags;
- inspectable examples showing how scores were produced;
- sensitivity and validation results, including null or heterogeneous findings;
- a record of models, prompts, thresholds, and processing decisions when available; and
- reproducible scripts and figures for collaborators or reviewers who want the technical detail.

The assistant can also produce a short narrative summary for a proposal or paper. That summary should remain tied to the recorded evidence and should not convert observable variation into an unsupported psychological label.

## Responsibilities of the researcher and assistant

| Researcher decides | Assistant and system handle |
| --- | --- |
| The theoretical question and why it matters | File inventory, processing, alignment, and structured extraction |
| The unit of analysis and target population | Feasibility checks and proposed operational alternatives |
| The reference group or personal baseline | Consistent calculation of the approved comparison |
| Which evidence belongs in the construct | Source-linked examples and component-level explanations |
| What validation is sufficient | Validation tables, sensitivity analyses, and error reporting |
| The empirical design and defensible claim | Dataset construction, statistical implementation, and audit files |

The researcher can reject or revise any proposed recipe. The system should make consequential choices visible rather than silently selecting them.

## What GitHub is for

GitHub supports inspection and reuse after the conversational workflow has made the project understandable. A reader can use it to:

1. inspect the measurement specification and claim boundaries;
2. examine sanitized derived data and worked examples;
3. review robustness checks and retained null results;
4. verify file integrity and reproduce released summaries; and
5. adapt the released recipes, tables, and validation logic to a new theory, setting, or dataset.

The repository does not need to expose source media, credentials, or every internal development file. Its purpose is to preserve the scientific record required to understand and audit the released measures.

## Access and remaining requirements

A conversational interface lowers programming and infrastructure barriers, which can broaden participation by researchers without specialized technical teams. It does not eliminate the need for lawful access to recordings, appropriate computing or model access, research judgment, human validation, privacy review, or domain expertise.

The workflow is therefore best described as assisted, auditable measurement. The researcher supplies the theory and judgment; the assistant operates the workflow; the research object preserves what was done and what the resulting variables can support.

## Preview the two-minute video

[Watch the current preview](media/researcher_walkthrough.mp4) · [Caption file](media/researcher_walkthrough_captions.srt).

**Final narration pending:** the author's voice recording still needs to be added. The preview and captions are available for review.

The video follows the same six-step sequence:

1. The researcher asks the earnings-call question in ordinary language.
2. The assistant distinguishes the construct from observable evidence and proposes a recipe.
3. The researcher changes one meaningful choice, such as the baseline or unit of analysis.
4. The system shows one source-linked answer with its transcript, timing, and score components.
5. The approved recipe runs across the archive and produces a clean table.
6. The researcher reviews a cautious result, then opens the audit record in GitHub.

This sequence shows the real division of labor without requiring viewers to watch code run or understand the repository structure first.
