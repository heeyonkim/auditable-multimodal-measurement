#!/usr/bin/env python3
"""Recompute core pilot summaries using only the Python standard library."""

from __future__ import annotations

import argparse
import csv
import json
import statistics
from pathlib import Path


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def values(rows: list[dict[str, str]], field: str) -> list[float]:
    result: list[float] = []
    for row in rows:
        value = row.get(field, "")
        if value not in ("", None):
            result.append(float(value))
    return result


def five_number(items: list[float]) -> dict[str, float]:
    ordered = sorted(items)
    quartiles = statistics.quantiles(ordered, n=4, method="inclusive")
    return {
        "min": min(ordered),
        "p25": quartiles[0],
        "median": statistics.median(ordered),
        "p75": quartiles[2],
        "max": max(ordered),
    }


def is_true(value: str | None) -> bool:
    return str(value or "").strip().lower() in {"true", "1", "yes"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    audio_yield = read_rows(args.data_dir / "expanded_audio_measurement_yield.csv")
    audio_scores = read_rows(args.data_dir / "expanded_audio_answer_scores.csv")
    audio_examples = read_rows(args.data_dir / "expanded_audio_primary_examples_robustness.csv")
    if len(audio_yield) != 12 or len(audio_scores) != 3273 or len(audio_examples) != 177:
        raise SystemExit(
            f"Unexpected audio row counts: yield={len(audio_yield)}, "
            f"scores={len(audio_scores)}, examples={len(audio_examples)}"
        )

    interviews = read_rows(args.data_dir / "interview_measures.csv")
    aligned = read_rows(args.data_dir / "multimodal_frame_turn_alignment.csv")
    manifest = read_rows(args.data_dir / "sample_manifest.csv")
    if len(interviews) != 30 or len(manifest) != 30 or len(aligned) != 360:
        raise SystemExit(
            f"Unexpected row counts: interviews={len(interviews)}, "
            f"manifest={len(manifest)}, aligned={len(aligned)}"
        )

    fields = [
        "speaker_count",
        "turn_count",
        "dominant_speaker_speech_share",
        "median_response_latency_s",
        "all_filler_phrases_per_100_words",
        "multiple_people_frame_rate",
        "raised_hand_person_rate",
        "shot_transition_rate",
    ]
    summary = {
        "earnings_audio": {
            "executives": len(audio_yield),
            "usable_calls": sum(int(row["usable_calls"]) for row in audio_yield),
            "eligible_answers": len(audio_scores),
            "audio_interaction_review_flags": len(audio_examples),
        },
        "interviews": len(interviews),
        "aligned_frame_rows": len(aligned),
        "frames_during_speech": sum(row["speech_active_at_frame"].lower() == "true" for row in aligned),
        "descriptive_variation": {field: five_number(values(interviews, field)) for field in fields},
    }
    shot_path = args.data_dir / "video_shot_dynamics.csv"
    chance_path = args.data_dir / "editorial_responsiveness_chance_adjusted.csv"
    if shot_path.exists() and chance_path.exists():
        shots = read_rows(shot_path)
        chance = read_rows(chance_path)
        if len(shots) != 30 or len(chance) != 30:
            raise SystemExit(f"Unexpected video-measure row counts: shots={len(shots)}, chance={len(chance)}")
        summary["continuous_video_analysis"] = {
            "videos": len(shots),
            "total_shots": sum(int(float(row["shot_count"])) for row in shots),
            "total_speaker_transitions": sum(int(float(row["speaker_transition_count"])) for row in shots),
            "median_shot_changes_per_minute": statistics.median(values(shots, "shot_changes_per_minute")),
            "median_edit_within_2s_rate": statistics.median(values(shots, "edit_within_2s_of_speaker_change_rate")),
            "median_chance_expected_rate": statistics.median(values(chance, "chance_expected_edit_near_transition_rate")),
            "median_chance_adjusted_responsiveness": statistics.median(values(chance, "chance_adjusted_editorial_responsiveness")),
            "positive_chance_adjusted_videos": sum(float(row["chance_adjusted_editorial_responsiveness"]) > 0 for row in chance),
        }
    event_path = args.data_dir / "event_aligned_production_measures.csv"
    if event_path.exists():
        events = read_rows(event_path)
        if len(events) != 120:
            raise SystemExit(f"Unexpected event-aligned row count: events={len(events)}")
        cut_events = [row for row in events if is_true(row["cut_between_pre_and_settled"])]
        no_cut_events = [row for row in events if not is_true(row["cut_between_pre_and_settled"])]
        changed = [row for row in events if is_true(row["composition_change_pre_settled"])]
        summary["event_aligned_video_analysis"] = {
            "videos": len({row["candidate_id"] for row in events}),
            "speaker_transition_events": len(events),
            "event_aligned_frames": len(events) * 3,
            "composition_class_changes": len(changed),
            "composition_class_change_rate": len(changed) / len(events),
            "focus_gain_events": sum(is_true(row["focus_gain_pre_settled"]) for row in events),
            "multiple_to_focused_single_events": sum(
                is_true(row["multi_to_single_pre_settled"]) for row in events
            ),
            "focused_single_to_multiple_events": sum(
                is_true(row["single_to_multi_pre_settled"]) for row in events
            ),
            "exact_window_cut_events": len(cut_events),
            "composition_change_rate_with_cut": sum(
                is_true(row["composition_change_pre_settled"]) for row in cut_events
            ) / len(cut_events),
            "composition_change_rate_without_cut": sum(
                is_true(row["composition_change_pre_settled"]) for row in no_cut_events
            ) / len(no_cut_events),
        }
    args.output.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
