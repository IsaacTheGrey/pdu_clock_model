import numpy as np
from scipy.signal import periodogram
from multiprocessing import Pool

def normalize_oscillations(solution):
    return solution / solution.mean(axis=0)

def compute_periodogram(solution, dt):
    frequencies, power = periodogram(solution[:, 0], 1 / dt)
    nonzero_indices = frequencies != 0
    return frequencies[nonzero_indices], power[nonzero_indices]

def analyze_sensitivity_parallel(param):
    parameter_name, value, base_parameters, y0, t = param
    parameters = base_parameters.copy()
    parameters[parameter_name] = value
    from .simulation import integrate_model
    sol_PFL = integrate_model(y0, t, parameters)
    last_osc = 144
    sol_PFL_asymp = sol_PFL[-int(last_osc / t[1]):, :]
    sol_PFL_asymp = normalize_oscillations(sol_PFL_asymp)
    frequencies, power = compute_periodogram(sol_PFL_asymp, t[1])
    periods = 1 / frequencies
    dominant_period_idx = np.argmax(power)
    dominant_period = periods[dominant_period_idx]
    return value, dominant_period

def analyze_sensitivity(parameter_name, parameter_range, base_parameters, y0, t):
    params = [(parameter_name, value, base_parameters, y0, t) for value in parameter_range]
    with Pool() as pool:
        results = pool.map(analyze_sensitivity_parallel, params)
    results.sort()  # Ensure the results are sorted by parameter values
    dominant_periods = [result[1] for result in results]
    return dominant_periods

def parameter_sweep(base_parameters, y0, t, parameter_ranges):
    """
    Performs a parameter sweep for multiple parameters.
    
    :param base_parameters: Dictionary of base parameter values.
    :param y0: Initial conditions.
    :param t: Time points for the integration.
    :param parameter_ranges: Dictionary of parameter ranges to sweep.
    :return: Dictionary of results for each parameter.
    """
    sensitivity_results = {}
    for param, param_range in parameter_ranges.items():
        dominant_periods = analyze_sensitivity(param, param_range, base_parameters, y0, t)
        sensitivity_results[param] = (param_range, dominant_periods)
    return sensitivity_results

