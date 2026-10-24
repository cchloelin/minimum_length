import scipy.ndimage as ndimage
from data_extraction import initial_conditions

"""Blur the original data to simulate a minimum length."""
blurring_radius = 0.25
n = 256
raw_data = initial_conditions()[:, -1]

def blurred_data():
    data_4d = raw_data.reshape(n, n, n)
    blurred = ndimage.gaussian_filter(data_4d, sigma=blurring_radius)
    return blurred