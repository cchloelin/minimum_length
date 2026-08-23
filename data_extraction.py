from classy import Class
import powerbox as pbox
from powerbox import get_power
import matplotlib.pyplot as plt
import numpy as np

LambdaCDM = Class()
LambdaCDM.set_baseline('p18lb')
LambdaCDM.compute()

primordial_dictionary = LambdaCDM.get_primordial()
wavenumber = np.array(primordial_dictionary['k [1/Mpc]'])
values = np.array(primordial_dictionary['P_scalar(k)'])

def primordial_callable(array):
    return np.interp(array.flatten(), wavenumber.flatten(), values.flatten())

# what are the units for the real-space realization if the primordial power spectrum is dimensionless??
b_length = 100.0

pb = pbox.PowerBox(
    N=512,                     
    dim=2,                     
    pk = primordial_callable,
    boxlength = b_length,           
)

plt.imshow(pb.delta_x(),extent=(0,b_length, 0, b_length))
plt.colorbar()
plt.show()
