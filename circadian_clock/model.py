import numpy as np

def goodwin_model_simplified(y0, t, parameters):
    """
    Defines ODEs of the Goodwin model.
    """
    X, Y, Z, R, S, C, W = y0

    nu1  = parameters['nu1']
    nu2  = parameters['nu2']
    nu3  = parameters['nu3']
    nu4  = parameters['nu4']
    nu5  = parameters['nu5']
    nu6  = parameters['nu6']
    nu7  = parameters['nu7']
    nu8  = parameters['nu8']
    nu9  = parameters['nu9']
    nu10 = parameters['nu10']
    nu11 = parameters['nu11']
    nu12 = parameters['nu12']
    nu13 = parameters['nu13']
    nu14 = parameters['nu14']
    
    K1  = parameters['K1']
    K2  = parameters['K2']
    K3  = parameters['K3']
    K4  = parameters['K4']
    K5  = parameters['K5']
    K6  = parameters['K6']
    K7  = parameters['K7']
    K8  = parameters['K8']
    K9  = parameters['K9']
    K10 = parameters['K10']
    
    hill = parameters['hill']
    hill_S = parameters['hill_S']
    hill_W = parameters['hill_W']
    
    b = parameters['b']
    c = parameters['c']
    d = parameters['d']

    PFL = b + c * X + d * W  # Positive feedback loop (PFL) term

    dXdt = nu1 * ((K1**hill) / (K1**hill + Z**hill + W**hill_W + S**hill_S)) * PFL - nu2 * (X / (K2 + X))  # clk/bmal
    dYdt = nu3 * X * ((K3**hill) / (K3**hill + W**hill_W)) - nu4 * (Y / (K4 + Y))  # per/tr-cry mRNA and protein
    dZdt = nu5 * Y - nu6 * (Z / (K6 + Z))
    dRdt = nu7 * X - nu8 * (R / (K7 + R))  # rev-erb mRNA and protein
    dSdt = nu9 * R - nu10 * (S / (K8 + S))
    dCdt = nu11 * X * ((K5**hill) / (K5**hill + W**hill_W)) - nu12 * (C / (K9 + C))  # cwo mRNA and protein
    dWdt = nu13 * C - nu14 * (W / (K10 + W))
    
    return [dXdt, dYdt, dZdt, dRdt, dSdt, dCdt, dWdt]

def generate_default_parameters():
    """
    Generates a dictionary of default parameters for the model.
    """
    return {
        'nu1': 0.7, 'nu2': 0.5, 'nu3': 0.40, 'nu4': 0.3, 'nu5': 0.70,
        'nu6': 0.35, 'nu7': 0.3, 'nu8': 0.2, 'nu9': 0.1, 'nu10': 0.2,
        'nu11': 0.03, 'nu12': 0.05, 'nu13': 0.3, 'nu14': 0.2, 'K1': 1.00,
        'K2': 1.00, 'K3': 1.00, 'K4': 1.00, 'K5': 0.80, 'K6': 1.00, 
        'K7': 1.00, 'K8': 1.00, 'K9': 1.00, 'K10': 1.00, 'hill': 3,
        'hill_S': 1.00, 'hill_W': 1.00, 'b': 1.0, 'c': 1.0, 'd': 0.3
    }
