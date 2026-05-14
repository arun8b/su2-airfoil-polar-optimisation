#!/usr/bin/env python3
"""Plot SU2 airfoil polar from CSV.

Expected columns:
AoA_deg,CL,CD,CM,CL_over_CD
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    required = {"AoA_deg", "CL", "CD"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")

    args.output.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 5))
    plt.plot(df["CD"], df["CL"], marker="o")
    plt.xlabel("CD")
    plt.ylabel("CL")
    plt.title("SU2 airfoil drag polar")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(args.output, dpi=180)
    print(f"Saved {args.output}")

    lift_curve = args.output.with_name(args.output.stem + "_lift_curve.png")
    plt.figure(figsize=(8, 5))
    plt.plot(df["AoA_deg"], df["CL"], marker="o")
    plt.xlabel("Angle of attack [deg]")
    plt.ylabel("CL")
    plt.title("SU2 lift curve")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(lift_curve, dpi=180)
    print(f"Saved {lift_curve}")


if __name__ == "__main__":
    main()
