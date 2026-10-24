import numpy as np
from gaussian_blurring import blurred_data
from powerbox import get_power

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

"""Format the power spectrum data to convention for COBAYA / CLASS."""
# Convert the dimensionful values into the dimensionless power spectrum format.
primordial_values = (k_values**3 / (2 * np.pi**2)) * dimensionful_values

# Fit the values to log-log space as convention
log_k = np.log(k_values)
log_p = np.log(primordial_values)