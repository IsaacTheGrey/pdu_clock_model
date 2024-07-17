# Circadian Clock Simulation

This repository contains a Python implementation of a circadian clock simulation based on the Goodwin model. It includes functionality for parameter sweep and sensitivity analysis, with results exported to a CSV file.

## Structure

- `circadian_clock/`: Contains the core modules for the simulation.
  - `model.py`: Defines the ODE model.
  - `simulation.py`: Handles the numerical integration of the model.
  - `analysis.py`: Provides functions for normalizing oscillations, computing periodograms, performing parameter sweep, and saving results.
  - `plotting.py`: Contains plotting functions for visualizing results.
- `scripts/`: Contains scripts to run simulations and analyses.
  - `run_simulation.py`: Main script to run the simulation and sensitivity analysis.
- `README.md`: This file.

## Usage

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/circadian_clock_simulation.git
    cd circadian_clock_simulation
    ```

2. Install required packages:

    ```bash
    pip install numpy scipy matplotlib
    ```

### Running the Simulation

To run the simulation and sensitivity analysis, execute the following command:

```bash
python scripts/run_simulation.py
```

```mermaid
graph TD;
    A[Start] --> B[Generate Default Parameters]
    B --> C[Integrate Model]
    C --> D[Remove Transient Behavior]
    D --> E[Compute Periodogram]
    E --> F[Plot Main Results]
    F --> G[Define Parameter Ranges]
    G --> H[Perform Parameter Sweep]
    H --> I[Save Sensitivity Results to CSV]
    I --> J[Plot Sensitivity Results]
    J --> K[End]

    subgraph Simulation
        B --> C
        C --> D
        D --> E
        E --> F
    end

    subgraph Sensitivity Analysis
        G --> H
        H --> I
        I --> J
    end
```


