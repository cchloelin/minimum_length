import scipy.ndimage as ndimage
from data_extraction import primordial_realization
import numpy as np

# blurring_radius has to be in terms of pixels because of how scipy functions.
# radius is sigma^3, so 2^3 is 6 pixels.
# because each pixel in this case is 200 mpc / 10 pixels = 20 mpc, 20*6=120 mpc which is equal to before.
blurring_radius = 2.0
n = 10
data = primordial_realization()[:, -1]

def blurred_data():
    data_4d = data.reshape(n, n, n)
    blurred = ndimage.gaussian_filter(data_4d, sigma=blurring_radius)
    return blurred

print(blurred_data())