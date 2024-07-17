import numpy as np
from circadian_clock.model import generate_default_parameters
from circadian_clock.simulation import integrate_model
from circadian_clock.analysis import normalize_oscillations, compute_periodogram, parameter_sweep
from circadian_clock.plotting import plot_main_results, plot_sensitivity_results

def main():
    dt = 0.01
    t = np.arange(0.0, 5000, dt)
    y0 = [1, 0, 0, 0, 0, 0, 0]

    # Use default parameters
    base_parameters = generate_default_parameters()

    # Integrate the model
    sol_PFL = integrate_model(y0, t, base_parameters)

    # Remove transient behavior, keep only asymptotic dynamics
    last_osc = 144
    t_asymp = np.arange(0, last_osc, dt)
    sol_PFL_asymp = sol_PFL[-int(last_osc / dt):, :]
    sol_PFL_asymp = normalize_oscillations(sol_PFL_asymp)

    # Compute periodogram
    frequencies, power = compute_periodogram(sol_PFL_asymp, dt)
    periods = 1 / frequencies
    dominant_period_idx = np.argmax(power)
    dominant_period = periods[dominant_period_idx]

    # Plot main results
    plot_main_results(t_asymp, sol_PFL_asymp, periods, power, dominant_period)

    # Define parameter ranges for the sweep
    parameter_ranges = {param: np.linspace(0.5 * base_parameters[param], 1.5 * base_parameters[param], 10)
                        for param in base_parameters.keys()}

    # Perform parameter sweep
    sensitivity_results = parameter_sweep(base_parameters, y0, t, parameter_ranges)

    # Plot sensitivity results in multiple pages
    plot_sensitivity_results(sensitivity_results)

if __name__ == "__main__":
    main()

