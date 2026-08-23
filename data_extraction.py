import powerbox as pbox
from powerbox import get_power
import matplotlib.pyplot as plt
import numpy as np

def dimensionless_primordial(k, As=2.123257e-09, ns=9.686025e-01, k_pivot=0.05):
    return As * (k/k_pivot) ** (ns-1)

def dimensionful_primordial(k):
    return (2*np.pi**2)/k**3 * dimensionless_primordial(k)

b_length = 1000.0

pb = pbox.PowerBox(
    N=256,                     
    dim=3,                     
    pk = dimensionful_primordial,
    boxlength = b_length,           
)

realization = pb.delta_x()

values, wavenumber, *extra = get_power(realization, pb.boxlength)
print(wavenumber, values)

realization_slice = realization[0, :, :]
plt.imshow(realization_slice, extent=(0,b_length,0,b_length))
plt.colorbar()
plt.show()
