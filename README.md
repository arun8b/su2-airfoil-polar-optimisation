# SU2 Airfoil Polar and Optimisation Workflow

A CFD automation project using **SU2** to generate airfoil aerodynamic polars, extract lift/drag coefficients and build a structured route toward aerodynamic optimisation.

This repository is designed as a professional aerospace CFD portfolio project. It demonstrates not only solver usage, but also the full workflow expected in aerodynamic analysis: case setup, configuration control, angle-of-attack sweeps, coefficient extraction, post-processing, verification checks and engineering interpretation.

---

## Project Objective

The objective of this project is to build a reproducible SU2 workflow for 2D airfoil aerodynamic analysis.

The project focuses on:

- Airfoil CFD case setup
- Angle-of-attack sweep automation
- Lift, drag and moment coefficient extraction
- Drag polar generation
- Lift-curve analysis
- Baseline aerodynamic performance assessment
- Preparation for adjoint-based or parametric optimisation

The emphasis is on creating a repeatable CFD workflow rather than running isolated cases manually.

---

## Why SU2?

SU2 is an open-source multiphysics simulation and design optimisation suite widely used in academic and research-focused aerodynamic studies.

It is suitable for this project because it supports:

- compressible and incompressible CFD workflows
- RANS simulations
- automated configuration files
- aerodynamic coefficient monitoring
- Python-driven case management
- adjoint-based optimisation workflows
- design-space exploration

This makes it a strong tool for demonstrating aerospace CFD, aerodynamic design and optimisation capability.

---

## Engineering Aim

The aim is to analyse an airfoil across a range of angles of attack and generate aerodynamic performance data such as:

- lift coefficient, `CL`
- drag coefficient, `CD`
- pitching moment coefficient, `CM`
- lift-to-drag ratio, `CL/CD`
- lift curve, `CL` vs angle of attack
- drag polar, `CL` vs `CD`

The final output should show how aerodynamic performance changes with angle of attack and how the workflow could be extended into optimisation.

---

## Repository Structure

```text
su2-airfoil-polar-optimisation/
├── config/
│   └── base.cfg
├── geometry/
│   └── README.md
├── scripts/
│   ├── generate_aoa_cases.py
│   ├── extract_su2_history.py
│   └── plot_polar.py
├── results/
│   └── polar_template.csv
├── figures/
├── docs/
│   └── methodology.md
├── project_summary.json
├── LICENSE
└── README.md
