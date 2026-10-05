import numpy as np
from blurring_script import blurring
from gaussian_blurring import blurred_data
from powerbox import get_power
from scipy.interpolate import CubicSpline

n = 10
b_length = 200.0
data = blurring()

"""Extract only the random variable values from the real-space data."""
random_values = [point[-1] for point in data]
shaped_values = np.asarray(random_values).reshape(n, n, n)

"""Get the power spectrum data using the get_power function in powerbox."""
# n-modes describes the number of points in each bin.
dimensionful_values, k_values, _, n_modes = get_power(
    shaped_values, 
    b_length, 
    a=1, b=1,
    dimensionless=False,
    log_bins=True,
    )

"""Derive the power spectrum equation using cubic spline interpolation."""
# Convert the dimensionful values into the dimensionless power spectrum format.
primordial_values = (k_values**3 / (2 * np.pi**2)) * dimensionful_values

# Fit the values to log-log space as convention
log_k = np.log(k_values)
log_p = np.log(primordial_values)

# Use cubic spline interpolation to get the primordial power spectrum equation.
primordial_equation = CubicSpline(log_k, log_p)