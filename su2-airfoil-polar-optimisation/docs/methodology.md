# Methodology

## Baseline Study

The first phase is a polar-generation workflow. The target output is a coefficient table across angle of attack:

| AoA | CL | CD | CM | CL/CD |
|---:|---:|---:|---:|---:|

## Verification Checks

- residual convergence for each angle of attack
- coefficient convergence history
- mesh consistency across all cases
- clear statement of Reynolds number and Mach number
- comparison against known airfoil behaviour where available

## Optimisation Extension

After the baseline polar is complete, the optimisation stage can be added.

Potential objectives:

- minimise drag at fixed lift
- maximise CL/CD at cruise condition
- reduce moment coefficient penalty
- improve pressure recovery for intake-style geometry

Potential constraints:

- minimum thickness
- leading-edge radius
- pitching moment
- lift coefficient
- geometry smoothness

## Notes

Do not present unvalidated outputs as final results. Keep the repository honest: state when data is preliminary, template-based or not yet validated.
