"""Build a simplified, publication-ready figure for the video pilot."""

from __future__ import annotations

import csv
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Patch, Rectangle


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/derived/repeated_interviewer"
PROFILE_CSV = BASE / "francine_multimodal_deviation_profiles.csv"
MANIFEST_CSV = BASE / "manifest.csv"
PNG = ROOT / "figures/submission_figure_3_repeated_interviewer.png"
PDF = ROOT / "figures/submission_figure_3_repeated_interviewer.pdf"


CHANNELS = [
    ("Transcript", "words"),
    ("Interaction timing", "turn-taking"),
    ("Vocal delivery", "voice"),
    ("Visual: speaking", "facial movement\nwhile speaking"),
    ("Visual: listening", "facial movement\nwhile listening"),
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    profiles = read_csv(PROFILE_CSV)
    manifest = read_csv(MANIFEST_CSV)
    guest_by_id = {row["sample_id"]: row["interviewee"] for row in manifest}

    if len(profiles) != 8:
        raise ValueError(f"Expected eight interview profiles; found {len(profiles)}")

    guests = [guest_by_id[row["sample_id"]] for row in profiles]
    values = np.array(
        [
            [float(row[key]) if row[key] else np.nan for key, _ in CHANNELS]
            for row in profiles
        ],
        dtype=float,
    )

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "axes.labelcolor": "#263746",
            "xtick.color": "#263746",
            "ytick.color": "#263746",
        }
    )

    fig, ax = plt.subplots(figsize=(11.5, 6.2), dpi=220, facecolor="white")
    fig.subplots_adjust(left=0.235, right=0.965, top=0.95, bottom=0.27)

    cmap = LinearSegmentedColormap.from_list(
        "departure",
        ["#F2F5F7", "#F7D8B8", "#E98263", "#96384A"],
    )
    image = ax.imshow(
        np.ma.masked_invalid(values),
        cmap=cmap,
        vmin=0,
        vmax=2.0,
        aspect="auto",
    )

    for row_index in range(values.shape[0]):
        for column_index in range(values.shape[1]):
            value = values[row_index, column_index]
            if math.isnan(value):
                ax.add_patch(
                    Rectangle(
                        (column_index - 0.5, row_index - 0.5),
                        1,
                        1,
                        facecolor="#F4F4F4",
                        edgecolor="#98A5AF",
                        linewidth=0.8,
                        hatch="///",
                        zorder=2,
                    )
                )
            else:
                ax.add_patch(
                    Rectangle(
                        (column_index - 0.5, row_index - 0.5),
                        1,
                        1,
                        fill=False,
                        edgecolor="white",
                        linewidth=1.5,
                        zorder=3,
                    )
                )

    ax.set_xticks(range(len(CHANNELS)), [label for _, label in CHANNELS], fontsize=11.5)
    ax.set_yticks(range(len(guests)), guests, fontsize=12)
    ax.tick_params(axis="x", length=0, pad=10)
    ax.tick_params(axis="y", length=0, pad=8)
    for spine in ax.spines.values():
        spine.set_visible(False)

    cbar = fig.colorbar(
        image,
        ax=ax,
        orientation="horizontal",
        fraction=0.055,
        pad=0.18,
        aspect=35,
    )
    cbar.set_ticks([0, 2])
    cbar.set_ticklabels(["closer to usual", "more distinctive"])
    cbar.ax.tick_params(labelsize=10.5, length=0, pad=4)
    cbar.outline.set_visible(False)

    if np.isnan(values).any():
        fig.legend(
            handles=[
                Patch(
                    facecolor="#F4F4F4",
                    edgecolor="#98A5AF",
                    hatch="///",
                    label="not observable",
                )
            ],
            loc="lower right",
            bbox_to_anchor=(0.965, 0.035),
            frameon=False,
            fontsize=10.5,
        )

    fig.savefig(PNG, dpi=220, facecolor="white", bbox_inches="tight")
    plt.close(fig)
    print(PNG)
    print(PDF)


if __name__ == "__main__":
    main()
