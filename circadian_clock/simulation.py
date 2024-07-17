import numpy as np
from scipy.integrate import odeint

def integrate_model(y0, t, parameters):
    """
    Integrates the ODEs numerically.
    """
    from .model import goodwin_model_simplified
    return odeint(goodwin_model_simplified, y0, t, args=(parameters,))

