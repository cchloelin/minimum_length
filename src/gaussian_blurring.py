import numpy as np
import scipy.ndimage as ndimage
from data_extraction import primordial_realization
from powerbox import get_power
from scipy.interpolate import CubicSpline

"""Blur the original data to simulate a minimum length."""
blurring_radius = 0.25
n = 256
raw_data = primordial_realization()[:, -1]

def blurred_data():
    data_4d = raw_data.reshape(n, n, n)
    blurred = ndimage.gaussian_filter(data_4d, sigma=blurring_radius)
    return blurred

b_length = 200.0
altered_data = blurred_data()

"""Get the power spectrum data using the get_power function in powerbox."""
# n-modes describes the number of points in each bin.
dimensionful_values, k_values, _, n_modes = get_power(
    altered_data, 
    b_length, 
    a=1, b=1,
    dimensionless=False,
    log_bins=True,
    bins = 20
    )

"""Derive the power spectrum equation using cubic spline interpolation."""
# Convert the dimensionful values into the dimensionless power spectrum format.
primordial_values = (k_values**3 / (2 * np.pi**2)) * dimensionful_values

# Fit the values to log-log space as convention
log_k = np.log(k_values)
log_p = np.log(primordial_values)

# Use cubic spline interpolation to get the primordial power spectrum equation.
primordial_equation = CubicSpline(log_k, log_p)