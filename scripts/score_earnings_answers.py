"""Build auditable call- and answer-level behavioral deviation measures.

The measures are deliberately descriptive.  The call-level score captures how
far one executive's complete-call Q&A profile departs from that executive's other calls.  The
answer-level score first removes each call's typical Q&A profile, then captures
unusual moments within that call.  Neither score infers emotion, uncertainty,
intent, truthfulness, or deception.

Inputs are the turn-level outputs written by ``build_apple_baseline.py``.  The
leave-one-call-out design prevents a target answer from helping define its own
reference distribution.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path
from statistics import mean, median, stdev
from typing import Any, Callable


MIN_WORDS = 20
MIN_DURATION_S = 10.0
MIN_BASELINE_TURNS = 40
MIN_WITHIN_CALL_TURNS = 5
MIN_BASELINE_CALLS = 15
Z_CAP = 5.0


def _float(row: dict[str, str], key: str) -> float | None:
    value = row.get(key)
    if value in (None, ""):
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None


def _quantile(values: list[float], probability: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    position = (len(ordered) - 1) * probability
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    weight = position - lower
    return ordered[lower] * (1 - weight) + ordered[upper] * weight


def _robust_center_scale(values: list[float]) -> tuple[float, float | None]:
    center = median(values)
    deviations = [abs(value - center) for value in values]
    scale = 1.4826 * median(deviations)
    if scale <= 1e-9 and len(values) > 1:
        scale = stdev(values)
    return center, scale if scale > 1e-9 else None


def _round(value: float | None, digits: int = 4) -> float | None:
    if value is None or not math.isfinite(value):
        return None
    return round(value, digits)


def _rate(count: float | None, words: float | None, multiplier: float) -> float | None:
    if count is None or words in (None, 0):
        return None
    return multiplier * count / words


def _log1p_nonnegative(value: float | None) -> float | None:
    if value is None:
        return None
    return math.log1p(max(value, 0.0))


def _log_positive(value: float | None) -> float | None:
    if value is None or value <= 0:
        return None
    return math.log(value)


def _identity(value: float | None) -> float | None:
    return value


FEATURES: list[dict[str, Any]] = [
    {
        "key": "speaking_rate_delta_from_prepared_wpm",
        "group": "audio_interaction",
        "label": "speaking rate relative to prepared remarks",
        "unit": "words/min",
        "transform": _identity,
    },
    {
        "key": "response_latency_s",
        "group": "audio_interaction",
        "label": "response latency",
        "unit": "seconds",
        "transform": _log1p_nonnegative,
    },
    {
        "key": "long_gap_rate_delta_from_prepared_per_100_words",
        "group": "audio_interaction",
        "label": "long word-onset gaps relative to prepared remarks",
        "unit": "per 100 words",
        "transform": _identity,
    },
    {
        "key": "f0_relative_to_prepared_semitones",
        "group": "audio_interaction",
        "label": "pitch relative to prepared remarks",
        "unit": "semitones",
        "transform": _identity,
    },
    {
        "key": "f0_cv_delta_from_prepared",
        "group": "audio_interaction",
        "label": "pitch variability relative to prepared remarks",
        "unit": "ratio",
        "transform": _identity,
    },
    {
        "key": "intensity_relative_to_prepared_db",
        "group": "audio_interaction",
        "label": "intensity relative to prepared remarks",
        "unit": "dB",
        "transform": _identity,
    },
    {
        "key": "intensity_sd_delta_from_prepared_db",
        "group": "audio_interaction",
        "label": "intensity variability relative to prepared remarks",
        "unit": "dB",
        "transform": _identity,
    },
    {
        "key": "word_count",
        "group": "transcript_visible",
        "label": "answer length",
        "unit": "words",
        "transform": _log_positive,
    },
    {
        "key": "filled_pauses_per_1000_words",
        "group": "transcript_visible",
        "label": "transcribed filled pauses",
        "unit": "per 1,000 words",
        "transform": _log1p_nonnegative,
    },
    {
        "key": "discourse_fillers_per_1000_words",
        "group": "transcript_visible",
        "label": "transcribed discourse fillers",
        "unit": "per 1,000 words",
        "transform": _log1p_nonnegative,
    },
    {
        "key": "adjacent_repetitions_per_1000_words",
        "group": "transcript_visible",
        "label": "transcribed adjacent repetitions",
        "unit": "per 1,000 words",
        "transform": _log1p_nonnegative,
    },
]


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _weighted_source_mean(rows: list[dict[str, str]], key: str) -> float | None:
    pairs = []
    for row in rows:
        value = _float(row, key)
        weight = _float(row, "elapsed_duration_s")
        if value is not None and weight is not None and weight > 0:
            pairs.append((value, weight))
    if not pairs:
        return None
    return sum(value * weight for value, weight in pairs) / sum(weight for _, weight in pairs)


def _prepared_anchors(rows: list[dict[str, str]]) -> dict[str, dict[str, float | None]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        if row.get("section") == "Prepared remarks":
            grouped[row["call_id"]].append(row)
    anchors: dict[str, dict[str, float | None]] = {}
    for call_id, call_rows in grouped.items():
        words = sum(_float(row, "word_count") or 0 for row in call_rows)
        duration = sum(_float(row, "elapsed_duration_s") or 0 for row in call_rows)
        long_gaps = sum(_float(row, "long_onset_gap_count_1s") or 0 for row in call_rows)
        anchors[call_id] = {
            "word_count": words,
            "elapsed_duration_s": duration,
            "speaking_rate_wpm": 60 * words / duration if duration > 0 else None,
            "long_gap_rate_1s_per_100_words": 100 * long_gaps / words if words > 0 else None,
            "f0_median_hz": _weighted_source_mean(call_rows, "f0_median_hz"),
            "f0_cv": _weighted_source_mean(call_rows, "f0_cv"),
            "intensity_mean_dbfs": _weighted_source_mean(call_rows, "intensity_mean_dbfs"),
            "intensity_sd_db": _weighted_source_mean(call_rows, "intensity_sd_db"),
            "voiced_frame_fraction": _weighted_source_mean(call_rows, "voiced_frame_fraction"),
            "prepared_segment_count": float(len(call_rows)),
        }
    return anchors


def _q_and_a_anchors(rows: list[dict[str, str]]) -> dict[str, dict[str, float | None]]:
    """Build a within-call fallback anchor when the target has no prepared remarks."""
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        if row.get("section") != "Questions and answers":
            continue
        words = _float(row, "word_count")
        duration = _float(row, "elapsed_duration_s")
        if words is None or words < MIN_WORDS or duration is None or duration < MIN_DURATION_S:
            continue
        grouped[row["call_id"]].append(row)
    anchors: dict[str, dict[str, float | None]] = {}
    for call_id, call_rows in grouped.items():
        def center(key: str) -> float | None:
            values = [_float(row, key) for row in call_rows]
            usable = [value for value in values if value is not None]
            return median(usable) if usable else None

        gap_rates = [
            _rate(_float(row, "long_onset_gap_count_1s"), _float(row, "word_count"), 100)
            for row in call_rows
        ]
        gap_rates = [value for value in gap_rates if value is not None]
        anchors[call_id] = {
            "speaking_rate_wpm": center("speaking_rate_wpm"),
            "long_gap_rate_1s_per_100_words": median(gap_rates) if gap_rates else None,
            "f0_median_hz": center("f0_median_hz"),
            "f0_cv": center("f0_cv"),
            "intensity_mean_dbfs": center("intensity_mean_dbfs"),
            "intensity_sd_db": center("intensity_sd_db"),
            "voiced_frame_fraction": center("voiced_frame_fraction"),
            "prepared_segment_count": 0.0,
        }
    return anchors


def prepare_turns(rows: list[dict[str, str]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    prepared_by_call = _prepared_anchors(rows)
    q_and_a_by_call = _q_and_a_anchors(rows)

    included: list[dict[str, Any]] = []
    excluded: list[dict[str, Any]] = []
    for source in rows:
        if source.get("section") != "Questions and answers":
            continue
        words = _float(source, "word_count")
        duration = _float(source, "elapsed_duration_s")
        reason = None
        if words is None or words < MIN_WORDS:
            reason = f"fewer than {MIN_WORDS} words"
        elif duration is None or duration < MIN_DURATION_S:
            reason = f"shorter than {MIN_DURATION_S:g} seconds"
        if reason:
            excluded.append({
                "call_id": source.get("call_id"),
                "source_segment_index": source.get("source_segment_index"),
                "word_count": words,
                "elapsed_duration_s": duration,
                "exclusion_reason": reason,
                "text": source.get("text", ""),
            })
            continue

        prepared = prepared_by_call.get(source["call_id"])
        acoustic_anchor = "Prepared remarks"
        if not prepared:
            prepared = q_and_a_by_call.get(source["call_id"], {})
            acoustic_anchor = "Same-call Q&A median"
        prepared_f0 = prepared.get("f0_median_hz")
        turn_f0 = _float(source, "f0_median_hz")
        prepared_voiced = prepared.get("voiced_frame_fraction")
        turn_voiced = _float(source, "voiced_frame_fraction")
        pitch_tracking_usable = (
            prepared_voiced is not None
            and turn_voiced is not None
            and prepared_voiced >= 0.25
            and turn_voiced >= 0.25
            and prepared_f0 is not None
            and turn_f0 is not None
            and 70 <= prepared_f0 <= 300
            and 70 <= turn_f0 <= 300
        )
        f0_relative = None
        if pitch_tracking_usable and prepared_f0 and turn_f0:
            f0_relative = 12 * math.log2(turn_f0 / prepared_f0)
        prepared_intensity = prepared.get("intensity_mean_dbfs")
        turn_intensity = _float(source, "intensity_mean_dbfs")
        intensity_relative = None
        if prepared_intensity is not None and turn_intensity is not None:
            intensity_relative = turn_intensity - prepared_intensity
        prepared_rate = prepared.get("speaking_rate_wpm")
        turn_rate = _float(source, "speaking_rate_wpm")
        prepared_gap_rate = prepared.get("long_gap_rate_1s_per_100_words")
        turn_gap_rate = _rate(_float(source, "long_onset_gap_count_1s"), words, 100)
        prepared_f0_cv = prepared.get("f0_cv")
        turn_f0_cv = _float(source, "f0_cv")
        pitch_variability_usable = (
            pitch_tracking_usable
            and prepared_f0_cv is not None
            and turn_f0_cv is not None
            and 0 <= prepared_f0_cv <= 1.0
            and 0 <= turn_f0_cv <= 1.0
        )
        prepared_intensity_sd = prepared.get("intensity_sd_db")
        turn_intensity_sd = _float(source, "intensity_sd_db")

        row: dict[str, Any] = {
            "call_id": source["call_id"],
            "year": int(float(source["year"])),
            "quarter": int(float(source["quarter"])),
            "source_segment_index": int(float(source["source_segment_index"])),
            "started_at_s": _float(source, "started_at_s"),
            "ended_at_s": _float(source, "ended_at_s"),
            "elapsed_duration_s": duration,
            "word_count": words,
            "speaking_rate_wpm": turn_rate,
            "speaking_rate_delta_from_prepared_wpm": (
                turn_rate - prepared_rate
                if turn_rate is not None and prepared_rate is not None
                else None
            ),
            "response_latency_s": _float(source, "response_latency_s"),
            "long_gap_rate_1s_per_100_words": turn_gap_rate,
            "long_gap_rate_delta_from_prepared_per_100_words": (
                turn_gap_rate - prepared_gap_rate
                if turn_gap_rate is not None and prepared_gap_rate is not None
                else None
            ),
            "f0_relative_to_prepared_semitones": f0_relative,
            "f0_cv": turn_f0_cv,
            "f0_cv_delta_from_prepared": (
                turn_f0_cv - prepared_f0_cv
                if pitch_variability_usable
                else None
            ),
            "intensity_relative_to_prepared_db": intensity_relative,
            "intensity_sd_db": turn_intensity_sd,
            "intensity_sd_delta_from_prepared_db": (
                turn_intensity_sd - prepared_intensity_sd
                if turn_intensity_sd is not None and prepared_intensity_sd is not None
                else None
            ),
            "filled_pauses_per_1000_words": _rate(
                _float(source, "filled_pause_count"), words, 1000
            ),
            "discourse_fillers_per_1000_words": _rate(
                _float(source, "discourse_filler_count"), words, 1000
            ),
            "adjacent_repetitions_per_1000_words": _rate(
                _float(source, "adjacent_repetition_count"), words, 1000
            ),
            "prepared_segment_count": int(prepared.get("prepared_segment_count") or 0),
            "acoustic_anchor": acoustic_anchor,
            "pitch_tracking_usable": "Yes" if pitch_tracking_usable else "No",
            "pitch_variability_usable": "Yes" if pitch_variability_usable else "No",
            "text": source.get("text", ""),
        }
        included.append(row)
    return included, excluded


def _transformed_value(row: dict[str, Any], feature: dict[str, Any]) -> float | None:
    transform: Callable[[float | None], float | None] = feature["transform"]
    return transform(row.get(feature["key"]))


def _attach_within_call_residuals(turns: list[dict[str, Any]]) -> None:
    """Remove each call's median Q&A profile before answer-level scoring."""
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in turns:
        grouped[row["call_id"]].append(row)
    for call_rows in grouped.values():
        transformed_centers: dict[str, float] = {}
        raw_centers: dict[str, float] = {}
        for feature in FEATURES:
            key = feature["key"]
            transformed = [
                value
                for row in call_rows
                if (value := _transformed_value(row, feature)) is not None
            ]
            raw = [row.get(key) for row in call_rows if row.get(key) is not None]
            if transformed:
                transformed_centers[key] = median(transformed)
            if raw:
                raw_centers[key] = median(raw)
        for row in call_rows:
            residuals: dict[str, float | None] = {}
            for feature in FEATURES:
                key = feature["key"]
                value = _transformed_value(row, feature)
                residuals[key] = (
                    value - transformed_centers[key]
                    if value is not None and key in transformed_centers
                    else None
                )
            row["_within_call_residuals"] = residuals
            row["_within_call_raw_medians"] = raw_centers
            row["within_call_reference_turns"] = len(call_rows)


def _score_answer_group(
    row: dict[str, Any],
    baseline: list[dict[str, Any]],
    group: str,
) -> tuple[float | None, list[dict[str, Any]]]:
    components: list[dict[str, Any]] = []
    if row["within_call_reference_turns"] < MIN_WITHIN_CALL_TURNS:
        return None, components
    for feature in FEATURES:
        if feature["group"] != group:
            continue
        key = feature["key"]
        value = row["_within_call_residuals"].get(key)
        transformed = [
            candidate["_within_call_residuals"].get(key)
            for candidate in baseline
            if candidate["within_call_reference_turns"] >= MIN_WITHIN_CALL_TURNS
            and candidate["_within_call_residuals"].get(key) is not None
        ]
        if value is None or len(transformed) < MIN_BASELINE_TURNS:
            continue
        center, scale = _robust_center_scale(transformed)
        if scale is None:
            continue
        z = (value - center) / scale
        label = feature["label"]
        if row.get("acoustic_anchor") == "Same-call Q&A median":
            label = label.replace("relative to prepared remarks", "relative to same-call Q&A median")
        components.append({
            "key": key,
            "label": label,
            "unit": feature["unit"],
            "value": row.get(key),
            "same_call_median": row["_within_call_raw_medians"].get(key),
            "baseline_median": center,
            "z": z,
            "capped_z": max(-Z_CAP, min(Z_CAP, z)),
        })
    minimum = 5 if group == "audio_interaction" else 2
    if len(components) < minimum:
        return None, components
    return math.sqrt(mean(component["capped_z"] ** 2 for component in components)), components


def _component_text(components: list[dict[str, Any]], limit: int = 3) -> str:
    ranked = sorted(components, key=lambda item: abs(item["z"]), reverse=True)[:limit]
    pieces = []
    for item in ranked:
        direction = "above" if item["z"] > 0 else "below"
        value = item["value"]
        comparison = item.get("same_call_median", item["baseline_median"])
        pieces.append(
            f"{item['label']} {direction} comparison median "
            f"({value:.2f} vs {comparison:.2f} {item['unit']}; z={item['z']:+.2f})"
        )
    return "; ".join(pieces)


def score_turns(turns: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    _attach_within_call_residuals(turns)
    calls = sorted({row["call_id"] for row in turns})
    feature_rows: list[dict[str, Any]] = []
    output: list[dict[str, Any]] = []
    for row in turns:
        baseline = [candidate for candidate in turns if candidate["call_id"] != row["call_id"]]
        audio_score, audio_components = _score_answer_group(row, baseline, "audio_interaction")
        transcript_score, transcript_components = _score_answer_group(row, baseline, "transcript_visible")
        all_components = audio_components + transcript_components
        combined = math.sqrt(mean(component["capped_z"] ** 2 for component in all_components)) if all_components else None
        record = {
            **{key: value for key, value in row.items() if not key.startswith("_")},
            "reference_design": "Within-call residual; leave one call out",
            "reference_call_count": len(calls) - 1,
            "reference_turn_count": len(baseline),
            "audio_interaction_deviation": _round(audio_score, 3),
            "transcript_visible_deviation": _round(transcript_score, 3),
            "combined_deviation": _round(combined, 3),
            "audio_minus_transcript": _round(
                audio_score - transcript_score
                if audio_score is not None and transcript_score is not None
                else None, 3,
            ),
            "audio_top_contributors": _component_text(audio_components),
            "transcript_top_contributors": _component_text(transcript_components),
            "evidence_clip_start_s": _round(max(0.0, float(row["started_at_s"]) - 2.0), 3),
            "evidence_clip_end_s": _round(float(row["ended_at_s"]) + 2.0, 3),
        }
        output.append(record)
        for component in all_components:
            feature_rows.append({
                "call_id": row["call_id"],
                "source_segment_index": row["source_segment_index"],
                "feature_group": next(
                    feature["group"] for feature in FEATURES if feature["key"] == component["key"]
                ),
                "feature_key": component["key"],
                "feature": component["label"],
                "unit": component["unit"],
                "observed_value": _round(component["value"]),
                "same_call_q_and_a_median": _round(component["same_call_median"]),
                "leave_one_call_out_residual_median": _round(component["baseline_median"]),
                "robust_z_score": _round(component["z"], 3),
                "capped_z_used_in_composite": _round(component["capped_z"], 3),
            })

    score_values = sorted(
        float(row["audio_interaction_deviation"])
        for row in output if row["audio_interaction_deviation"] is not None
    )
    for row in output:
        score = row["audio_interaction_deviation"]
        transcript = row["transcript_visible_deviation"]
        percentile = (
            100 * sum(value <= float(score) for value in score_values) / len(score_values)
            if score is not None and score_values else None
        )
        row["audio_deviation_percentile"] = _round(percentile, 1)
        row["audio_outlier_flag"] = "Yes" if score is not None and float(score) >= 2.0 else "No"
        row["transcript_appears_routine"] = "Yes" if transcript is not None and float(transcript) <= 1.25 else "No"
        row["priority_for_clip_review"] = (
            "Insufficient within-call reference"
            if row["within_call_reference_turns"] < MIN_WITHIN_CALL_TURNS
            else "High"
            if row["audio_outlier_flag"] == "Yes" and row["transcript_appears_routine"] == "Yes"
            else "Review"
            if row["audio_outlier_flag"] == "Yes"
            else "Routine"
        )
    output.sort(key=lambda row: (
        -(float(row["audio_interaction_deviation"]) if row["audio_interaction_deviation"] is not None else -1),
        row["call_id"], row["source_segment_index"],
    ))
    return output, feature_rows


def score_calls(turns: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Score each call's median Q&A profile against the other calls."""
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in turns:
        grouped[row["call_id"]].append(row)
    profiles: list[dict[str, Any]] = []
    for call_id, rows in sorted(grouped.items()):
        profile: dict[str, Any] = {
            "call_id": call_id,
            "year": rows[0]["year"],
            "quarter": rows[0]["quarter"],
            "eligible_q_and_a_turns": len(rows),
            "prepared_segment_count": max(int(row.get("prepared_segment_count") or 0) for row in rows),
            "acoustic_anchor": (
                "Prepared remarks"
                if any(row.get("acoustic_anchor") == "Prepared remarks" for row in rows)
                else "Same-call Q&A median"
            ),
        }
        for feature in FEATURES:
            key = feature["key"]
            raw = [row.get(key) for row in rows if row.get(key) is not None]
            transformed = [value for row in rows if (value := _transformed_value(row, feature)) is not None]
            profile[key] = median(raw) if raw else None
            profile[f"_transformed_{key}"] = median(transformed) if transformed else None
        profiles.append(profile)

    detail: list[dict[str, Any]] = []
    output: list[dict[str, Any]] = []
    for profile in profiles:
        target_eligible = (
            profile["eligible_q_and_a_turns"] >= MIN_WITHIN_CALL_TURNS
            and profile["prepared_segment_count"] > 0
        )
        other = [
            candidate for candidate in profiles
            if candidate["call_id"] != profile["call_id"]
            and candidate["eligible_q_and_a_turns"] >= MIN_WITHIN_CALL_TURNS
            and candidate["prepared_segment_count"] > 0
        ]
        by_group: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for feature in FEATURES:
            if not target_eligible:
                continue
            key = feature["key"]
            value = profile.get(f"_transformed_{key}")
            baseline = [candidate.get(f"_transformed_{key}") for candidate in other]
            baseline = [item for item in baseline if item is not None]
            if value is None or len(baseline) < MIN_BASELINE_CALLS:
                continue
            center, scale = _robust_center_scale(baseline)
            if scale is None:
                continue
            z = (value - center) / scale
            raw_baseline = [candidate.get(key) for candidate in other if candidate.get(key) is not None]
            component = {
                "key": key, "label": feature["label"], "unit": feature["unit"],
                "value": profile.get(key),
                "baseline_median": median(raw_baseline) if raw_baseline else None,
                "z": z, "capped_z": max(-Z_CAP, min(Z_CAP, z)),
            }
            by_group[feature["group"]].append(component)
            detail.append({
                "call_id": profile["call_id"], "feature_group": feature["group"],
                "feature_key": key, "feature": feature["label"], "unit": feature["unit"],
                "call_q_and_a_median": _round(profile.get(key)),
                "other_call_median": _round(component["baseline_median"]),
                "robust_z_score": _round(z, 3),
                "capped_z_used_in_composite": _round(component["capped_z"], 3),
            })
        scores: dict[str, float | None] = {}
        for group, minimum in (("audio_interaction", 5), ("transcript_visible", 2)):
            components = by_group[group]
            scores[group] = math.sqrt(mean(item["capped_z"] ** 2 for item in components)) if len(components) >= minimum else None
        record = {key: value for key, value in profile.items() if not key.startswith("_")}
        record.update({
            "reference_design": "Call Q&A median; leave one call out",
            "reference_call_count": len(other),
            "call_profile_status": (
                "Scored"
                if target_eligible
                else "Answer-level only: no prepared-remarks anchor"
                if profile["prepared_segment_count"] == 0
                else "Insufficient eligible Q&A turns"
            ),
            "call_audio_interaction_deviation": _round(scores["audio_interaction"], 3),
            "call_transcript_visible_deviation": _round(scores["transcript_visible"], 3),
            "audio_top_contributors": _component_text(by_group["audio_interaction"]),
            "transcript_top_contributors": _component_text(by_group["transcript_visible"]),
        })
        output.append(record)
    audio_values = sorted(float(row["call_audio_interaction_deviation"]) for row in output if row["call_audio_interaction_deviation"] is not None)
    for row in output:
        score = row["call_audio_interaction_deviation"]
        row["call_audio_deviation_percentile"] = _round(
            100 * sum(value <= float(score) for value in audio_values) / len(audio_values), 1
        ) if score is not None and audio_values else None
    output.sort(key=lambda row: -float(row["call_audio_interaction_deviation"] or -1))
    return output, detail


def summarize_calls(scored: list[dict[str, Any]], call_profiles: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in scored:
        grouped[row["call_id"]].append(row)
    call_profile_by_id = {row["call_id"]: row for row in call_profiles}
    summaries = []
    for call_id, rows in sorted(grouped.items()):
        audio = [float(row["audio_interaction_deviation"]) for row in rows if row["audio_interaction_deviation"] is not None]
        transcript = [float(row["transcript_visible_deviation"]) for row in rows if row["transcript_visible_deviation"] is not None]
        top = max(rows, key=lambda row: float(row["audio_interaction_deviation"] or -1))
        summaries.append({
            **call_profile_by_id[call_id],
            "median_within_call_answer_audio_deviation": _round(median(audio), 3) if audio else None,
            "p90_within_call_answer_audio_deviation": _round(_quantile(audio, 0.9), 3),
            "maximum_within_call_answer_audio_deviation": _round(max(audio), 3) if audio else None,
            "median_within_call_answer_transcript_deviation": _round(median(transcript), 3) if transcript else None,
            "audio_outlier_turns": sum(row["audio_outlier_flag"] == "Yes" for row in rows),
            "high_priority_audio_not_transcript_turns": sum(row["priority_for_clip_review"] == "High" for row in rows),
            "most_deviant_source_segment_index": top["source_segment_index"],
            "most_deviant_started_at_s": top["started_at_s"],
            "most_deviant_audio_score": top["audio_interaction_deviation"],
            "most_deviant_top_contributors": top["audio_top_contributors"],
        })
    return summaries


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def write_report(
    path: Path,
    scored: list[dict[str, Any]],
    calls: list[dict[str, Any]],
    excluded: list[dict[str, Any]],
    executive_name: str = "Tim Cook",
    company_name: str = "Apple",
) -> None:
    high = [row for row in scored if row["priority_for_clip_review"] == "High"]
    top = [
        row for row in scored
        if row["audio_interaction_deviation"] is not None
        and row["transcript_visible_deviation"] is not None
    ][:10]
    lines = [
        f"# {executive_name} behavioral deviation pilot",
        "",
        "## What the measure captures",
        "",
        f"Two scores separate different scientific objects. The call-level score measures how far {executive_name}'s median Q&A profile in a complete call departs from the executive's other calls. The answer-level score first subtracts the median Q&A profile of that same call, then compares the residual with answer residuals from the other calls. This prevents a call-wide shift from turning every answer into an apparent moment-level anomaly.",
        "",
        "To reduce recording-condition artifacts, speaking rate, long word-onset gaps, pitch, pitch variability, intensity, and intensity variability are expressed relative to the same executive's prepared remarks in the same call. Response latency is measured directly.",
        "",
        "A separate transcript-visible score uses answer length and disfluency markers present in the transcript. The comparison identifies answers whose vocal or interactional delivery is unusual even when the written transcript appears routine.",
        "",
        "The score is descriptive. It does not measure emotion, uncertainty, intent, truthfulness, or deception.",
        "",
        "## Current evidence base",
        "",
        f"- {company_name} calls: {len(calls)}",
        f"- Eligible {executive_name} Q&A turns extracted: {len(scored)}",
        f"- Calls spanning: {min(row['year'] for row in calls)} to {max(row['year'] for row in calls)}",
        f"- Short or unstable turns excluded: {len(excluded)}",
        f"- Audio-interaction outliers with routine transcript-visible scores: {len(high)}",
        "- Eligibility rule: at least 20 words and 10 seconds",
        "- Call baseline: each call compared with the other calls",
        "- Answer baseline: within-call residuals compared with residuals from other calls",
        "",
        "## Highest audio-interaction deviations",
        "",
        "| Rank | Call | Segment | Audio score | Transcript score | Audio percentile | Review priority | Main contributors |",
        "|---:|---|---:|---:|---:|---:|---|---|",
    ]
    for rank, row in enumerate(top, 1):
        lines.append(
            f"| {rank} | {row['call_id']} | {row['source_segment_index']} | "
            f"{row['audio_interaction_deviation']:.3f} | {row['transcript_visible_deviation']:.3f} | "
            f"{row['audio_deviation_percentile']:.1f} | {row['priority_for_clip_review']} | "
            f"{row['audio_top_contributors'].replace('|', '/')} |"
        )
    lines += [
        "",
        "## Interpretation",
        "",
        "The useful research object is not a claim that an executive was anxious or deceptive. It is a reproducible, source-linked measure of departure from that executive's own established delivery pattern at two levels: whole-call context and within-call moments. Every high score can be decomposed into observable contributing features and reviewed in the original audio.",
        "",
        "## Important limitations",
        "",
        f"- The archive contains {len(calls)} calls across {max(row['year'] for row in calls) - min(row['year'] for row in calls) + 1} calendar years, but only one executive and company.",
        "- Word timestamps approximate pauses because word end times are unavailable.",
        "- Transcript-based disfluencies may be understated when the provider smooths speech.",
        "- Microphone gain, compression, network delay, and editing can affect acoustic measures. Recording-sensitive features are therefore referenced to the same call's prepared remarks.",
        "- Leave-one-call-out scoring supports descriptive validation, not causal or predictive claims.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("turn_metrics_csv", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--executive-name", default="Tim Cook")
    parser.add_argument("--company-name", default="Apple")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    source_rows = read_rows(args.turn_metrics_csv)
    turns, excluded = prepare_turns(source_rows)
    scored, feature_rows = score_turns(turns)
    call_profiles, call_feature_rows = score_calls(turns)
    call_summaries = summarize_calls(scored, call_profiles)

    _write_csv(args.output_dir / "answer_deviation_scores.csv", scored)
    _write_csv(args.output_dir / "feature_contributions.csv", feature_rows)
    _write_csv(args.output_dir / "call_deviation_summary.csv", call_summaries)
    _write_csv(args.output_dir / "call_feature_contributions.csv", call_feature_rows)
    _write_csv(args.output_dir / "excluded_short_turns.csv", excluded)
    write_report(
        args.output_dir / "behavioral_deviation_report.md",
        scored,
        call_summaries,
        excluded,
        executive_name=args.executive_name,
        company_name=args.company_name,
    )

    summary = {
        "construct": "Behavioral deviation from personal baseline",
        "executive_name": args.executive_name,
        "company_name": args.company_name,
        "interpretation": f"Call-level departure plus within-call answer-level departure from {args.executive_name}'s observable Q&A delivery",
        "reference_design": "Two level: call Q&A medians and within-call answer residuals, both leave one call out",
        "call_count": len(call_summaries),
        "eligible_turn_count": len(scored),
        "excluded_turn_count": len(excluded),
        "high_priority_audio_not_transcript_count": sum(
            row["priority_for_clip_review"] == "High" for row in scored
        ),
        "thresholds": {
            "minimum_words": MIN_WORDS,
            "minimum_duration_s": MIN_DURATION_S,
            "minimum_within_call_turns": MIN_WITHIN_CALL_TURNS,
            "minimum_baseline_calls": MIN_BASELINE_CALLS,
            "audio_outlier_score": 2.0,
            "routine_transcript_score_max": 1.25,
            "robust_z_cap": Z_CAP,
        },
        "audio_interaction_features": [
            feature["key"] for feature in FEATURES if feature["group"] == "audio_interaction"
        ],
        "transcript_visible_features": [
            feature["key"] for feature in FEATURES if feature["group"] == "transcript_visible"
        ],
        "warnings": [
            "Descriptive measurement only; do not infer emotion, uncertainty, intent, truthfulness, or deception.",
            f"The archive covers {len(call_summaries)} calls for one executive and company.",
            "Provider transcripts can omit disfluencies, making transcript-visible comparisons conservative.",
            "Production conditions can affect acoustics; recording-sensitive features are referenced to prepared remarks in the same call.",
        ],
    }
    (args.output_dir / "analysis_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    print(
        f"Scored {len(scored)} eligible Q&A turns across {len(call_summaries)} calls; "
        f"{summary['high_priority_audio_not_transcript_count']} high-priority audio-only deviations."
    )
    print(f"Results: {args.output_dir}")


if __name__ == "__main__":
    main()
