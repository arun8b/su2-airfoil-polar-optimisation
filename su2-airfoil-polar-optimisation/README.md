# SU2 Airfoil Polar and Optimisation Workflow

A CFD automation repository for aerodynamic polar generation and design exploration using SU2.

This project is designed to show aerospace CFD capability in a clean, recruiter-readable format: automated case creation, angle-of-attack sweeps, coefficient extraction, polar plotting and a path toward adjoint-based aerodynamic optimisation.

## Engineering Objective

Build a reproducible SU2 workflow to:

- define a baseline airfoil or intake-style 2D geometry
- run aerodynamic cases across multiple angles of attack
- extract lift, drag and moment coefficients
- generate a drag polar and lift-curve slope
- compare baseline and modified configurations
- document optimisation logic and limitations

## Why This Project Matters

SU2 is widely used for research-style CFD and aerodynamic design because it supports automated configuration control, multiphysics workflows and optimisation-oriented studies. This repository demonstrates that the user can structure CFD work as an engineering pipeline, not just isolated solver runs.

## Repository Structure

```text
.
├── config/               # SU2 configuration templates
├── geometry/             # Airfoil coordinate files or mesh notes
├── scripts/              # Python automation and plotting
├── results/              # CSV outputs from completed runs
├── figures/              # Generated polar and convergence plots
└── docs/                 # Methodology and optimisation notes
```

## Planned Workflow

1. Prepare baseline mesh for a NACA 0012 or selected airfoil.
2. Define a reusable SU2 configuration template.
3. Sweep angle of attack using `scripts/generate_aoa_cases.py`.
4. Run SU2 for each case.
5. Extract aerodynamic coefficients into a CSV.
6. Plot lift curve, drag polar and efficiency trends.
7. Compare baseline and modified geometry or setup.
8. Add adjoint/optimisation stage after baseline verification.

## Example Commands

Generate angle-of-attack case folders:

```bash
python scripts/generate_aoa_cases.py --template config/base.cfg --aoa -4 0 4 8 12 --out runs
```

Plot a completed polar CSV:

```bash
python scripts/plot_polar.py --input results/polar_template.csv --output figures/su2_polar.png
```

## Evidence To Add Before Pinning This Repo

- SU2 version and solver notes
- mesh screenshots
- baseline residual convergence
- lift curve and drag polar
- coefficient table
- interpretation of stall/linear range limits if applicable
- optimisation objective and constraints

## Recruiter-Facing Summary

Created a Python-automated SU2 CFD workflow for airfoil aerodynamic analysis, including angle-of-attack sweeps, coefficient extraction, polar plotting and a structured route toward adjoint-based design optimisation.
