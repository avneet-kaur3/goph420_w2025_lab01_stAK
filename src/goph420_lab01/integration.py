import numpy as np
import matplotlib.pyplot as plt


def integrate_newton(x, f, alg):
    '''Approximates the integral of f(x) over a set time period from 0 to 10 seconds by Newton-Cotes rules.
    The function can carry out the integration through the trapezoid rule or the 1/3 Simpson's rule.

    Parameters: 
        x (array_like) : Coordinates of the sample points.
        f (array_like) : Values of the function at the sample points.
        alg (str) : Flag for the algorithm to be used.
    Returns: 
        integral (float) : Provides a floating point value for the integral estimate.
    '''
    #If the value of alg given is not 'trap' or 'simp', a ValueError will be raised.
    if (alg.strip().lower() not in ['trap', 'simp']):
        raise ValueError("The algorithm chosen must be 'trap' or 'simp'.")
    
    #If the x and f arrays are incompatible, respective ValueErrors will be raised.
    if (x.shape[0] != f.shape[0]):
        raise ValueError('Arrays x and f have different lengths.')
    if (x.ndim != 1) or (f.ndim != 1):
        raise ValueError('Arrays x and f must be one-dimensional.')

    dx = 0.01

    if(alg == 'trap'):
        integral = (dx/2) * np.sum(f[1:] + f[:-1])

    elif(alg == 'simp'):
        integral = (dx/3) * (f[0] + f[-1] + (4 * np.sum(f[1:-1:2])) + (2 * np.sum(f[2:-2:2])))

    return integral
