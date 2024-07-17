import matplotlib.pyplot as plt
import numpy as np

def plot_main_results(t_asymp, solution, periods, power, dominant_period):
    """
    Plots time series, phase plot, and periodogram.
    """
    fig, axs = plt.subplots(1, 3, figsize=(24, 8))  # Main results in one row

    # Time series
    axs[0].plot(t_asymp, solution[:, 0], label='$bmal$')
    axs[0].plot(t_asymp, solution[:, 2], label='PER')
    axs[0].plot(t_asymp, solution[:, 4], label='REV-ERB')
    axs[0].plot(t_asymp, solution[:, 5], label='$cwo$')
    axs[0].plot(t_asymp, solution[:, 6], label='CWO')
    axs[0].legend(fontsize=12, loc='upper right')
    axs[0].set_xlabel('Time [h]', fontsize=14)
    axs[0].set_ylabel('Concentration [a.u.]', fontsize=14)
    axs[0].set_xticks(np.arange(0, t_asymp[-1], step=24))
    axs[0].tick_params(axis='both', which='major', labelsize=12)
    axs[0].set_title('Time Series of Oscillations')

    # Phase plot
    axs[1].plot(solution[:, 0], solution[:, 2], color='grey')
    axs[1].set_xlabel('CLK/BMAL Concentration [a.u.]', fontsize=14)
    axs[1].set_ylabel('PER/tr-CRY Concentration [a.u.]', fontsize=14)
    axs[1].tick_params(axis='both', which='major', labelsize=12)
    axs[1].set_title('Phase Plot')

    # Periodogram
    axs[2].plot(periods, power)
    axs[2].set_xlim(0, 36)
    axs[2].set_xlabel('Period [h]', fontsize=14)
    axs[2].set_ylabel('Power', fontsize=14)
    axs[2].tick_params(axis='both', which='major', labelsize=12)
    axs[2].set_xticks(np.arange(0, 36, step=4))
    axs[2].set_title('Periodogram')

    plt.tight_layout()
    plt.show()

    print(f"The dominant period is approximately {dominant_period:.2f} hours.")

def plot_sensitivity_results(sensitivity_results):
    """
    Plots sensitivity analysis results in multiple pages.
    """
    params_per_page = 2  # Number of parameters to plot per page
    num_params = len(sensitivity_results)
    num_pages = (num_params + params_per_page - 1) // params_per_page

    for page in range(num_pages):
        fig, axs = plt.subplots(1, params_per_page, figsize=(24, 8))
        
        for i in range(params_per_page):
            param_idx = page * params_per_page + i
            if param_idx >= num_params:
                break
            param_name = list(sensitivity_results.keys())[param_idx]
            param_range, dom_periods = sensitivity_results[param_name]
            ax = axs[i]
            ax.plot(param_range, dom_periods, marker='o')
            ax.axhline(y=24, color='r', linestyle='--', label='24-hour period')
            ax.set_xlabel(f'{param_name}', fontsize=14)
            ax.set_ylabel('Dominant Period [h]', fontsize=14)
            ax.set_title(f'Sensitivity to {param_name}', fontsize=16)
            ax.legend()
            ax.grid(True)

        plt.tight_layout()
        plt.show()

