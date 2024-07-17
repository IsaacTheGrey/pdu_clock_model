# Circadian Clock Simulation

This repository contains a Python implementation of a circadian clock simulation based on the Goodwin model.

## Structure

- `circadian_clock/`: Contains the core modules for the simulation.
  - `model.py`: Defines the ODE model.
  - `simulation.py`: Handles the numerical integration of the model.
  - `analysis.py`: Provides functions for normalizing oscillations, computing periodograms, and analyzing parameter sensitivity.
  - `plotting.py`: Contains plotting functions for visualizing results.
- `scripts/`: Contains scripts to run simulations and analyses.
  - `run_simulation.py`: Main script to run the simulation and sensitivity analysis.

## Usage

To run the simulation and sensitivity analysis, execute the following command:

```bash
python scripts/run_simulation.py
