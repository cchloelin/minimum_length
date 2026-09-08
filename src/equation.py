import numpy as np
from blurring_script import blurring
from powerbox.dft import fft

n = 10
b_length = 1000.0
data = blurring()
random_values = []

"""Extract only the random variable values from the real-space data."""
for point in data:
    random_values.append(point[-1])

# Specify that the field is 3D by shaping it accordingly; N is the N used when first generating a powerbox instance.
shaped_values = np.asarray(random_values).reshape(n, n, n)

"""Perform the Fourier transform."""
fourier_space = fft(shaped_values, b_length, ret_cubegrid=False)

# Returns 4 arrays:
## Fourier space values -> j means imaginary
## x coordinates
## y coordinates
## z coordinates
print(fourier_space)