# Submission technical appendix

[Home](../README.md) / [Documentation](README.md) / Technical appendix

This appendix describes the current proposal prototype and the limits of the shared research object. It distinguishes processed recordings, eligible observations, scored observations, and analyses that require additional inputs.

## Samples and exclusions

The proposal reports 300 collected earnings calls and 286 retained calls from 12 executives. The [300-call screening ledger](../data/derived/earnings_call_screening_ledger.csv) records the selection flow. Fourteen calls were excluded: ten had no identified focal-speaker segments and remained focal-name review items; one had no focal-executive turns in the extracted metrics; one had prepared remarks but no focal Q&A; and two had no focal Q&A answers meeting the 20-word and ten-second thresholds. The [measurement-yield table](../data/derived/expanded_audio_measurement_yield.csv) records retained calls and answer eligibility by executive. The panel was chosen for repeated coverage and variation, not population representativeness.

The 286 retained calls yield 3,273 eligible executive Q&A answers. Of these, 3,233 have both audio/interaction and transcript-visible departure scores. The remaining 40 answers occur in 12 calls with fewer than five eligible answers, below the within-call reference requirement. Their score fields remain missing rather than being imputed. Thus the case-selection comparison uses 3,233 paired scores, and the answer-summary market analysis uses 274 calls. The [outcome table](../data/derived/earnings_call_market_outcomes.csv) includes all 286 calls and documents the missing behavioral summaries.

Video evidence comes from two disjoint samples: a 30-interview Bloomberg archive covering 8.6 hours and four production formats, and eight additional *Leaders with Lacqua* interviews covering 192.4 minutes. The latter supports the repeated-interviewer demonstration and Figure 3. See the [30-interview source manifest](../data/derived/sample_manifest.csv) and [eight-interview source manifest](../data/derived/repeated_interviewer/manifest.csv).

## Processing and observation levels

The 30-interview pipeline preserves public source identifiers and preparation metadata, extracts mono 16 kHz audio and time-spread frames, transcribes and diarizes speech, groups consecutive same-speaker segments into turns, and aligns sampled visual observations to active or nearest speech turns. Continuous shot detection is aligned to speaker changes; circular shifts supply within-video chance comparisons. The event-aligned extension uses matched pre-transition, entry, and settled frames and exact-window cut counts. Derived outputs use flat CSV/JSON tables.

Observation levels include interviews, conversational turns, frame-turn alignments, and transition events. Produced-interview features such as framing, cut frequency, and shot duration describe production as well as participants. Twelve time-spread frames per interview do not provide continuous tracking. A visible person is not necessarily speaking; exclusive diarization cannot reliably estimate overlap or interruption duration. Functional-role labels remain exploratory without external validation. The [variable dictionary](../data/derived/variable_dictionary.csv), [validation plan](../data/derived/validation_plan.csv), and detailed [event-aligned specification](event_aligned_video_measurement.md) preserve field-level definitions and requirements.

## Earnings-call measurement

Eligibility requires an executive Q&A answer with at least 20 words and ten seconds of duration. Scoring requires at least five eligible answers in the call, with baseline requirements of 40 reference turns and 15 reference calls in the scoring implementation. Recording-sensitive features use the same call's prepared remarks as an anchor, with a documented Q&A fallback where prepared remarks are unavailable.

The [scoring implementation](../scripts/score_earnings_answers.py) records transformations, centering, eligibility rules, feature coverage, and scoring. It requires authorized numeric turn-level inputs for a full rescore; the shared answer-score snapshot alone is not that full input archive.

Audio/interaction features include speaking-rate change, response latency, long word-onset gaps, pitch level and variability, and intensity level and variability. Transcript-visible features are answer length, filled pauses, discourse fillers, and adjacent repetitions. The transcript score therefore does not represent all information obtainable from text, semantic embeddings, sentiment, or every transcript-only approach in prior research.

Answer-level scores describe within-call departures against an executive's other calls. Within each call, features are centered at the call median; the target answer's residuals are compared with residuals from that executive's other calls. A robust median/MAD scale is used with a standard-deviation fallback when needed. Feature contributions are capped at five standardized units and combined by root mean square within the audio/interaction and transcript groups. Target-call exclusion applies to the personal reference, but current-call centering uses its eligible answers. The current design uses other calls from both before and after a target call; it is not a prospective forecasting design. Stage 2 proposes prior-only baselines.

The paired-score table reproduces 325 audio/interaction flags and 321 transcript flags at cutoff 2.0, with 66 common flags. The 259 audio-only flags represent 79.7% of the 325. The stricter illustrative subset additionally requires transcript departure at most 1.25, yielding 177 answers. Of these, 172 remain flagged under at least two of three feature-family exclusions. The thresholds define review sets; they are not validated psychological boundaries. See the [answer scores](../data/derived/expanded_audio_answer_scores.csv), [177-case table](../data/derived/expanded_audio_primary_examples_robustness.csv), and [eligibility sensitivity](../data/derived/expanded_audio_eligibility_sensitivity.csv).

## Market-outcome extension

The outcome is the company's signed return minus the SPY return over the first trading session associated with the call. The exploratory partial Spearman correlation between median answer departure and that return is -0.102 (descriptive p = .094), controlling for transcript-visible departure, firm, and year. The corresponding standardized regression estimate is -0.54 percentage points, with firm-clustered 95% interval [-1.29, 0.21] and p = .142. These are different tests and should not be conflated.

The correlation is .060 in the original five-firm cohort and -.235 in the seven added firms. The previously specified 90th-percentile measure is weaker than the secondary median measure. Earnings and guidance surprises and contemporaneous news are not controlled; daily returns cannot isolate the portion occurring during the call. Twelve firms provide few clusters. This extension demonstrates outcome linkage, not predictive validity or causality. [Full design, results, and sensitivity tables](earnings_call_market_outcome.md).

## Video production and repeated-person measurement

In the 30-interview archive, the median within-interview proportion of speaker transitions occurring within two seconds of a cut is .65895; the median chance expectation under circular shifts is .1714. These are medians across interviews, not pooled percentages of all transitions. The pooled observed share is approximately .611. [Production measures](../data/derived/editorial_responsiveness_chance_adjusted.csv) and [sensitivity checks](../data/derived/video_measurement_sensitivity.csv).

For the separate eight-interview demonstration, see the [complete measurement rules](repeated_interviewer.md), including the distinction between seven reference interviews for nonvisual/speaking channels and five eligible reference interviews for listening. Hatched cells mean insufficient evidence for a score, rather than proof that no frames exist. The production-sensitivity analysis compares sampling and adjustment specifications jointly; the rank change is evaluated among the six common eligible interviews.

## Models, access, and scope of reproduction

The released manifest records known model information and explicitly marks missing transcription and diarization versions. The architecture is designed to retain model/version records, but the current sanitized snapshot is incomplete on this dimension. It supports derived-data verification, not a complete credential-free rerun of extraction. Stage 2 must pin extraction versions, preserve run settings, validate against human-reviewed examples, and provide shareable end-to-end fixtures.

Full source recordings, frames, face embeddings, and verbatim transcripts are excluded, apart from the short audio excerpt and transcript embedded in the [worked-example video](researcher_walkthrough.md). Authorized source access and appropriate model/computing access are required for a new extraction run. Current code and data have no selected open-source/open-data license; the intended Stage 2 system will be released under appropriate terms. Repository visibility alone should not be described as an open-source license. [Licensing status](../LICENSE.md) and [reproducibility](reproducibility.md).

The included browser prototype defines and exports measurement recipes. It does not process new recordings. This distinction separates the working specification interface, the derived-data demonstrations, and the proposed guided processing interface.

## Ethics and AI disclosure

The authors report that IRB review was not required because the project did not involve human-subjects research. Neither pilot was preregistered. Frozen measurement plans and documented choices should not be described as external preregistration. AI assisted analysis and manuscript drafting/editing; researchers remain responsible for the design, measurement choices, validation, and interpretation.

Observable departures do not establish emotion, intent, deception, personality, culture, or executive quality. Model errors, demographic and cultural differences, recording systems, topic, and production choices may affect measurements. Speaker-role corrections and missing-evidence flags are retained.

## Verify the reported evidence

Run `make check` with Python 3.10 or newer, or follow the [direct commands](reproducibility.md). The [submission verification script](../scripts/verify_submission_evidence.py) reconstructs the repeated-interviewer composites from released numeric inputs and checks sample separation, answer-score exclusions, flag counts, robustness support, and common-sample ranks. These checks establish consistency of released derived evidence; they do not establish extraction accuracy or construct validity.
