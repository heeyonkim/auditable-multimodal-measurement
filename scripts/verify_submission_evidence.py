#!/usr/bin/env python3
"""Reconstruct submission profiles and verify reported counts from released data."""
import csv
import math
from collections import defaultdict
from pathlib import Path
from statistics import mean, stdev

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data/derived'
VIDEO = DATA / 'repeated_interviewer'
DOMAINS = {
    'Transcript': ['median_words_per_turn', 'turn_word_count_cv', 'mattr_50'],
    'Interaction timing': ['median_turn_duration_s', 'median_response_latency_s', 'interviewer_speech_share', 'silent_pauses_per_minute'],
    'Vocal delivery': ['median_speaking_rate_wpm', 'median_f0_cv', 'median_intensity_sd_db', 'fillers_per_100_words'],
}


def rows(path):
    with path.open(encoding='utf-8', newline='') as stream:
        return list(csv.DictReader(stream))


def check():
    manifest = rows(VIDEO / 'manifest.csv')
    assert len(manifest) == 8
    broad_ids = {r['video_id'] for r in rows(DATA / 'sample_manifest.csv')}
    assert not broad_ids & {r['video_id'] for r in manifest}, 'Video samples overlap'
    released = {r['sample_id']: r for r in rows(VIDEO / 'francine_multimodal_deviation_profiles.csv')}
    inputs = rows(VIDEO / 'francine_audio_transcript_profiles.csv')
    for episode in inputs:
        for domain, features in DOMAINS.items():
            vector = []
            for feature in features:
                scale = stdev(float(r[feature]) for r in inputs)
                reference = mean(float(r[feature]) for r in inputs if r['sample_id'] != episode['sample_id'])
                vector.append((float(episode[feature]) - reference) / scale)
            score = math.sqrt(mean(v*v for v in vector))
            assert math.isclose(score, float(released[episode['sample_id']][domain]), rel_tol=1e-8, abs_tol=1e-8)
    calibration = rows(VIDEO / 'visual_feature_calibration.csv')
    vectors = defaultdict(list)
    for row in calibration:
        other = [float(r['adjusted_episode_mean']) for r in calibration if r['conversation_state'] == row['conversation_state'] and r['feature'] == row['feature'] and r['sample_id'] != row['sample_id']]
        assert len(other) == int(row['comparison_interviews'])
        value = (float(row['adjusted_episode_mean']) - mean(other)) / float(row['pooled_frame_sd'])
        vectors[row['sample_id'], row['conversation_state']].append(value)
    for (sample, state), vector in vectors.items():
        score = math.sqrt(mean(v*v for v in vector))
        assert math.isclose(score, float(released[sample]['Visual: '+state]), rel_tol=1e-8, abs_tol=1e-8)
    assert sum(state == 'speaking' for _, state in vectors) == 8
    assert sum(state == 'listening' for _, state in vectors) == 6
    answers = rows(DATA / 'expanded_audio_answer_scores.csv')
    paired = [r for r in answers if r['audio_interaction_deviation'] and r['transcript_visible_deviation']]
    assert (len(answers), len(paired)) == (3273, 3233)
    audio = [r for r in paired if float(r['audio_interaction_deviation']) >= 2]
    text = [r for r in paired if float(r['transcript_visible_deviation']) >= 2]
    assert (len(audio), len(text)) == (325, 321)
    assert sum(float(r['transcript_visible_deviation']) >= 2 for r in audio) == 66
    highlighted = [r for r in audio if float(r['transcript_visible_deviation']) <= 1.25]
    assert len(highlighted) == 177
    assert sum(int(r['family_exclusion_support_count']) >= 2 for r in highlighted) == 172
    missing = [r for r in answers if not r['audio_interaction_deviation']]
    assert len({r['call_id'] for r in missing}) == 12
    ledger = rows(DATA / 'earnings_call_screening_ledger.csv')
    assert len(ledger) == 300
    assert sum(r['retained_in_286'] == 'True' for r in ledger) == 286
    assert sum(r['screening_status'] == 'Excluded' for r in ledger) == 14
    outcomes = rows(DATA / 'earnings_call_market_outcomes.csv')
    assert len(outcomes) == 286
    eligible = [r for r in outcomes if r['answer_audio_median'] and r['answer_text_median']]
    assert len(eligible) == 274
    assert {r['call_id'] for r in missing} == {r['call_id'] for r in outcomes if not r['answer_audio_median']}
    assert all(int(r['eligible_q_and_a_turns']) < 5 for r in outcomes if not r['answer_audio_median'])
    specs = rows(VIDEO / 'video_episode_comparison.csv')
    a = {r['sample_id']: float(r['composite_deviation']) for r in specs if r['specification'] == 'naive_zero_fill_full_grid'}
    b = {r['sample_id']: float(r['composite_deviation']) for r in specs if r['specification'] == 'production_adjusted_targeted'}
    common = set(a) & set(b)
    assert len(common) == 6
    rank_a = sorted(common, key=lambda k: a[k], reverse=True).index('F002') + 1
    rank_b = sorted(common, key=lambda k: b[k], reverse=True).index('F002') + 1
    assert (rank_a, rank_b) == (5, 1)
    print('PASS: disjoint video samples; reconstructed all 24 nonvisual and 14 visual composites; answer counts, exclusions, robustness, and common-sample ranks match.')


if __name__ == '__main__':
    check()
