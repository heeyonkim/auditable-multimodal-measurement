# Proximal outcome pilot

This exploratory demonstration asks what organizational researchers can treat as an outcome once interviews become analyzable as synchronized language, voice, interaction, and produced video.

## Outcome families

1. **Editorial response:** whether a camera cut occurs within two seconds of a speaker transition. This is an observable production action, not a claim about editorial intent.
2. **Interviewer lexical uptake:** the share of a question-like interviewer's distinct content words that appeared in the preceding guest answer. This is a topic-contingent follow-up proxy, not a direct measure of understanding or engagement.
3. **Conversational space:** guest response latency and answer duration after an interviewer-to-guest transition. These are interaction-timing outcomes, not measures of cognition, confidence, or question difficulty.

## Worked result

The sample contains 304 eligible question-answer pairs across 27 videos. After removing each video's average level, longer questions, longer guest response delays, and camera cuts near the transition were each positively associated with guest answer duration. The accompanying table reports video-cluster bootstrap intervals.

The pooled direction persists across four eligibility thresholds and in leave-one-video-out influence checks. Format-specific estimates are heterogeneous, so setting should be modeled explicitly in any substantive study.

This is an exploratory illustration of what can be measured, not a confirmatory test. Automatic interviewer/guest labels and question types require targeted validation before substantive hypothesis testing. The added modalities did not improve leave-one-video-out prediction of editorial response or lexical uptake in this sample; those null demonstrations are retained for auditability.

## Files

- `data/derived/outcome_variable_recipes.csv`
- `data/derived/editorial_response_by_transition.csv`
- `data/derived/answer_space_within_video_associations.csv`
- `data/derived/answer_space_robustness.csv`
- `data/derived/outcome_model_comparison.csv`
- `figures/figure_8_proximal_outcomes.png`
