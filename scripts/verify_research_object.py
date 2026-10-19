#!/usr/bin/env python3
"""Build or verify the machine-readable manifest for the released research object.

This script intentionally uses only the Python standard library. It inventories the
shareable repository, records lightweight structural metadata, checks for common
privacy/credential leaks, and verifies that released files have not silently changed.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path


RELEASE_VERSION = "0.4.0-event-aligned-video"
RELEASE_DATE = "2026-09-28"
MANIFEST_NAME = "research_object_manifest.json"
EXCLUDED_NAMES = {MANIFEST_NAME, ".DS_Store"}
EXCLUDED_SUFFIXES = {".pyc", ".zip", ".tar", ".gz"}
TEXT_SUFFIXES = {".csv", ".html", ".json", ".md", ".py", ".txt", ".toml"}

LEAK_PATTERNS = {
    # Join the prefix so the scanner does not flag its own source code.
    "absolute macOS user path": re.compile("/" + r"Users/[^/\s]+/"),
    "Hugging Face token": re.compile(r"\bhf_[A-Za-z0-9]{20,}\b"),
    "Google API key": re.compile(r"\bAIza[A-Za-z0-9_-]{25,}\b"),
    "OpenAI-style secret": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "private key block": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def csv_metadata(path: Path) -> dict:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        try:
            columns = next(reader)
        except StopIteration:
            columns = []
            rows = 0
        else:
            rows = sum(1 for _ in reader)
    return {"rows": rows, "column_count": len(columns), "columns": columns}


def json_metadata(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    result = {"top_level_type": type(payload).__name__}
    if isinstance(payload, dict):
        result["top_level_keys"] = sorted(payload)
    elif isinstance(payload, list):
        result["items"] = len(payload)
    return result


def html_metadata(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"<title[^>]*>(.*?)</title>", text, flags=re.I | re.S)
    title = re.sub(r"\s+", " ", match.group(1)).strip() if match else None
    return {"title": title}


def leak_findings(path: Path, relative_path: str) -> list[dict]:
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return []
    text = path.read_text(encoding="utf-8", errors="replace")
    findings = []
    for label, pattern in LEAK_PATTERNS.items():
        for match in pattern.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            findings.append({"file": relative_path, "line": line, "type": label})
    return findings


def released_files(root: Path) -> list[Path]:
    files = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if path.name in EXCLUDED_NAMES or path.suffix.lower() in EXCLUDED_SUFFIXES:
            continue
        if any(part in {".git", "__pycache__"} for part in rel.parts):
            continue
        files.append(path)
    return sorted(files, key=lambda item: item.relative_to(root).as_posix())


def build_manifest(root: Path) -> dict:
    records = []
    leaks = []
    for path in released_files(root):
        rel = path.relative_to(root).as_posix()
        record = {
            "path": rel,
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        if path.suffix.lower() == ".csv":
            record["structure"] = csv_metadata(path)
        elif path.suffix.lower() == ".json":
            record["structure"] = json_metadata(path)
        elif path.suffix.lower() == ".html":
            record["structure"] = html_metadata(path)
        records.append(record)
        leaks.extend(leak_findings(path, rel))

    return {
        "schema": "auditable-multimodal-research-object/1.0",
        "release": {
            "name": "Making Organizational Behavior Observable proposal prototype",
            "version": RELEASE_VERSION,
            "date": RELEASE_DATE,
            "status": "proposal-stage derived-data research object",
        },
        "corpora": {
            "earnings_calls": {
                "calls": 286,
                "executives": 12,
                "eligible_answers": 3273,
                "content_released": "derived measures only",
            },
            "bloomberg_interviews": {
                "interviews": 30,
                "source_hours": 8.6,
                "speaker_transitions": 1178,
                "sampled_frames": 360,
                "event_aligned_transitions": 120,
                "event_aligned_frames": 360,
                "eligible_question_answer_pairs": 304,
                "content_released": "source URLs and derived measures; no media or transcripts",
            },
        },
        "pipeline_stages": [
            {"stage": "source selection", "status": "documented in released manifest"},
            {"stage": "audio extraction", "status": "run; source media excluded"},
            {"stage": "transcription and diarization", "status": "run; exact model versions not recorded in sanitized snapshot"},
            {"stage": "acoustic and interaction measurement", "status": "derived tables released"},
            {"stage": "sampled-frame observation", "status": "derived tables released"},
            {"stage": "shot detection and temporal alignment", "status": "derived tables and sensitivity checks released"},
            {"stage": "event-aligned composition measurement", "status": "frozen specification, derived tables, and uncertainty audit released"},
            {"stage": "construct specification", "status": "working Measurement Recipe Studio released"},
        ],
        "model_registry": [
            {
                "task": "structured sampled-frame observation",
                "model": "gemini-3.8-flash",
                "provenance_status": "captured in pilot run metadata",
                "claim_boundary": "frame-level observable coding; not psychological ground truth",
            },
            {
                "task": "speech transcription",
                "model": "not recorded in this sanitized snapshot",
                "provenance_status": "must be pinned before archival release",
                "claim_boundary": "automatic transcript may omit or normalize disfluencies",
            },
            {
                "task": "speaker diarization",
                "model": "not recorded in this sanitized snapshot",
                "provenance_status": "must be pinned before archival release",
                "claim_boundary": "exclusive diarization does not reliably measure overlap or interruption duration",
            },
        ],
        "known_limitations": [
            "The release supports derived-data verification, not a credential-free full media rerun.",
            "The repeated-speaker panel was selected for longitudinal coverage and setting variation, not population representativeness.",
            "Automatic transcripts may omit or normalize disfluencies.",
            "Exclusive diarization does not support reliable overlap or interruption-duration claims.",
            "Pitch and intensity are partly functions of recording and production systems.",
            "Time-spread frames and short event-aligned windows are not continuous visual tracking.",
            "Camera cuts and framing characterize the produced interview, not only the focal person.",
            "Exploratory associations are descriptive and do not identify causal effects.",
        ],
        "prohibited_claims": [
            "deception or lying",
            "emotion",
            "confidence",
            "intent",
            "personality",
            "cultural typicality",
            "editorial intention",
            "causal effects from descriptive temporal coupling",
        ],
        "integrity": {
            "algorithm": "SHA-256",
            "file_count": len(records),
            "privacy_or_credential_findings": leaks,
            "passes_release_scan": not leaks,
        },
        "files": records,
    }


def compare(expected: dict, current: dict) -> list[str]:
    problems = []
    if expected.get("schema") != current.get("schema"):
        problems.append("manifest schema differs")
    expected_files = {item["path"]: item for item in expected.get("files", [])}
    current_files = {item["path"]: item for item in current.get("files", [])}
    for missing in sorted(expected_files.keys() - current_files.keys()):
        problems.append(f"missing file: {missing}")
    for added in sorted(current_files.keys() - expected_files.keys()):
        problems.append(f"unmanifested file: {added}")
    for path in sorted(expected_files.keys() & current_files.keys()):
        for key in ("bytes", "sha256", "structure"):
            if expected_files[path].get(key) != current_files[path].get(key):
                problems.append(f"changed {key}: {path}")
    if current["integrity"]["privacy_or_credential_findings"]:
        for item in current["integrity"]["privacy_or_credential_findings"]:
            problems.append(f"release scan: {item['type']} in {item['file']}:{item['line']}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true", help="verify files against the saved manifest")
    args = parser.parse_args()
    root = args.root.resolve()
    manifest_path = root / MANIFEST_NAME
    current = build_manifest(root)

    if args.check:
        if not manifest_path.exists():
            print(f"FAIL: {MANIFEST_NAME} does not exist", file=sys.stderr)
            return 1
        expected = json.loads(manifest_path.read_text(encoding="utf-8"))
        problems = compare(expected, current)
        if problems:
            print("FAIL: research object verification found problems:", file=sys.stderr)
            for problem in problems:
                print(f"- {problem}", file=sys.stderr)
            return 1
        print(f"PASS: {len(current['files'])} files match the manifest; release scan found no leaks.")
        return 0

    manifest_path.write_text(json.dumps(current, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if current["integrity"]["privacy_or_credential_findings"]:
        print(f"WROTE {manifest_path}, but the release scan found possible leaks.", file=sys.stderr)
        return 2
    print(f"WROTE {manifest_path} with {len(current['files'])} files; release scan passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
