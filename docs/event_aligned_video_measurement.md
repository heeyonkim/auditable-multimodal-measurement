# Event-aligned video measurement specification

This specification was written before the new event-aligned frames were sent
to the visual model.

## Scientific target

Measure observable production responsiveness around speaker transitions: cuts
and changes in visible composition immediately before and after a new speaker
begins. The analysis concerns the produced video, not a stable characteristic
of the person shown. It does not infer emotion, attention, confidence,
engagement, deception, or editorial intent.

## Sample

- Twelve videos: three each from Remote, Studio, Stage/event, and Panel formats.
- Within each format, videos span lower, middle, and higher values of the
  previously calculated chance-adjusted cut-responsiveness measure.
- 10 eligible speaker transitions per video, for a target of
  120 events.
- Within each video, up to half the events have a detected cut within two
  seconds and half do not. If a category has fewer than five eligible events,
  the other category supplies the remainder.
- Events within each category are selected at evenly spaced positions across
  the interview timeline.
- Eligibility requires at least 3.2 seconds remaining in the incoming turn so
  that all three frame positions are comparable.

## Event-aligned observations

- **Pre:** 1.50 seconds before the incoming turn.
- **Entry:** 0.75 seconds after the incoming turn begins.
- **Settled:** 3.00 seconds after the incoming turn begins.
- The visual model records only visible features already used in the main
  pilot: person count, shot type, camera context, visible people, shared
  content, on-screen text, a factual description, and uncertainty notes.

## Primary derived measures

1. Any composition change from pre to settled.
2. Focus gain: the settled frame is a single-person close or medium shot while
   the pre frame is not.
3. Multi-to-single shift: pre shows multiple people or a two/split-screen shot,
   while settled shows one person.
4. Single-to-multi shift, retained as a directional comparison.
5. Agreement between deterministic cut detection and model-observed
   composition change.
6. Model uncertainty rate, always reported with the measure.

All relationships with response latency, turn duration, speech rate, pitch
variability, and intensity variability are descriptive and exploratory. No
causal claim will be made, and null or heterogeneous results will be retained.

## Selected videos

| ID | Format | Prior responsiveness | Title |
|---|---|---:|---|
| C004 | Stage/event | 0.672 | BNY CEO on Clients’ Tariff Questions, US Treasury Market |
| C006 | Studio | 0.138 | Roche Has Over Five Weight-Loss Companion Medicines, CEO Says |
| C008 | Remote | 0.861 | John Bolton on Gaza Truce Talks, Israel-Iran Tensions |
| C019 | Studio | 0.450 | Ken Moelis on Banker Pay, Private Equity, China |
| C028 | Remote | 0.513 | Stellantis CEO Says ‘No Taboos’ on Brands as Profit Falls |
| C032 | Remote | 0.323 | Steve Wozniak Talks YouTube Lawsuit, Apple and TikTok |
| C034 | Panel | 0.376 | Steve Pagliuca on NBA Valuations, Sports Streaming, AI |
| C038 | Panel | -0.050 | Cathie Wood on Bank Turmoil, Bitcoin and Strategy |
| C039 | Stage/event | 0.493 | Gorman on Succession Plan, Debt Ceiling |
| C043 | Stage/event | 0.000 | Oaktree's Howard Marks on Unpredictablility, Importance and Investing in AI |
| C054 | Studio | 0.703 | How Andrea Orcel Transformed UniCredit: Full Interview |
| C058 | Panel | 0.610 | Bloomberg New Economy Gateway Europe - Trade, Energy, Banking in Europe |
