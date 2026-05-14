#!/usr/bin/env python3
"""Generate SU2 angle-of-attack case folders from a template config.

Example:
python scripts/generate_aoa_cases.py --template config/base.cfg --aoa -4 0 4 8 12 --out runs
"""

from __future__ import annotations

import argparse
from pathlib import Path


def safe_name(aoa: float) -> str:
    sign = "m" if aoa < 0 else "p"
    value = str(abs(aoa)).replace(".", "p")
    return f"aoa_{sign}{value}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", required=True, type=Path)
    parser.add_argument("--aoa", required=True, nargs="+", type=float)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    template = args.template.read_text(encoding="utf-8")
    args.out.mkdir(parents=True, exist_ok=True)

    for aoa in args.aoa:
        case_dir = args.out / safe_name(aoa)
        case_dir.mkdir(parents=True, exist_ok=True)
        cfg = template.replace("{{AOA}}", f"{aoa:.3f}")
        (case_dir / "case.cfg").write_text(cfg, encoding="utf-8")
        (case_dir / "README.md").write_text(
            f"# SU2 case: AoA {aoa:.3f} deg\n\nRun with:\n\n```bash\nSU2_CFD case.cfg\n```\n",
            encoding="utf-8",
        )
        print(f"Created {case_dir}")


if __name__ == "__main__":
    main()
