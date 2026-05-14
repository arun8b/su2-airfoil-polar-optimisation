#!/usr/bin/env python3
"""Extract final coefficients from SU2 history CSV files.

This script expects SU2 history files with column names containing lift/drag/moment terms.
It is intentionally defensive because SU2 output columns vary by version/configuration.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re

import pandas as pd


def find_column(columns: list[str], patterns: list[str]) -> str:
    for pattern in patterns:
        regex = re.compile(pattern, re.IGNORECASE)
        for col in columns:
            if regex.search(col):
                return col
    raise KeyError(f"No column matched patterns {patterns}. Available columns: {columns}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--history", required=True, type=Path)
    parser.add_argument("--aoa", required=True, type=float)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    df = pd.read_csv(args.history)
    df.columns = [c.strip().strip('"') for c in df.columns]

    cl_col = find_column(df.columns.tolist(), [r"lift", r"cl"])
    cd_col = find_column(df.columns.tolist(), [r"drag", r"cd"])
    cm_col = find_column(df.columns.tolist(), [r"moment", r"cm"])

    final = df.iloc[-1]
    row = pd.DataFrame([{
        "AoA_deg": args.aoa,
        "CL": final[cl_col],
        "CD": final[cd_col],
        "CM": final[cm_col],
        "CL_over_CD": final[cl_col] / final[cd_col] if final[cd_col] != 0 else None,
    }])

    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.output.exists():
        old = pd.read_csv(args.output)
        out = pd.concat([old, row], ignore_index=True)
        out = out.drop_duplicates(subset=["AoA_deg"], keep="last").sort_values("AoA_deg")
    else:
        out = row

    out.to_csv(args.output, index=False)
    print(f"Updated {args.output}")


if __name__ == "__main__":
    main()
