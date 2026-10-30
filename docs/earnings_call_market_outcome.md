# Exploratory earnings call market outcome linkage

[Home](../README.md) / [Documentation](README.md)

This analysis asks whether earnings calls with greater vocal and interactional departure from an executive's personal baseline are followed by a different short-run stock-market response after accounting for transcript-visible departure.

## Design

- The panel contains 286 calls from 12 executives and firms; 274 calls have eligible answer-level scores.
- The outcome is the company's signed stock return minus the SPY return over the first trading session associated with the call. Negative values indicate worse performance relative to the broader market.
- The behavioral predictors summarize answer-level vocal and interactional departure from each executive's leave-one-call-out personal baseline.
- The matching transcript-visible departure, firm, and calendar year are included as controls. Regression uncertainty is clustered by firm.
- Robustness checks use alternative behavioral summaries, a two-session outcome window, calendar-quarter controls, outcome winsorization, within-firm permutation, and leave-one-company-out analyses.

## Results

The pooled panel shows a small negative but statistically inconclusive association. For median answer-level departure, the partial Spearman correlation is -.102 (descriptive p = .094). A one-standard-deviation increase corresponds to a 0.54-percentage-point lower market-adjusted return, but the firm-clustered 95% interval crosses zero (95% CI [-1.29, 0.21], p = .142).

The pattern is sensitive to cohort composition. The correlation is .060 in the original five-firm cohort and -.235 in the seven additional firms. The previously specified 90th-percentile summary is weaker than the secondary median specification. The result is therefore an exploratory outcome linkage, not validation of the behavioral measure or evidence of a reliable causal effect.

## Interpretation boundaries

- The analysis does not control for earnings surprises, guidance surprises, analyst expectations, or contemporaneous news.
- Daily returns cannot isolate the portion of the market response occurring during the call.
- The personal baseline is leave-one-call-out rather than strictly prior-only.
- Twelve firms provide few clusters for precise inference.
- Behavioral departure is not evidence of deception, emotion, confidence, or intent.

## Released files

- `data/derived/earnings_call_market_outcomes.csv`: call-level behavioral summaries, event timing, and market outcomes for the analysis panel.
- `data/derived/earnings_call_market_models.csv`: pooled model estimates and robustness specifications.
- `data/derived/earnings_call_market_cohort_sensitivity.csv`: original, added, and pooled cohort comparisons.
- `data/derived/earnings_call_market_leave_one_company_out.csv`: influence checks that omit one firm at a time.
- `data/derived/earnings_call_market_summary.json`: compact machine-readable results.
- `figures/supporting_figure_S3_market_outcomes.png`: proposal-ready summary figure.
