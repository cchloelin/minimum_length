from classy import Class
import powerbox as pbox
import matplotlib.pyplot as plt
import numpy as np

LambdaCDM = Class()
input = {# LambdaCDM parameters (Planck 18 + lensing + BAO bestfit)
        'omega_b':2.255065e-02,
        'omega_cdm':1.193524e-01,
        'H0':6.776953e+01,
        'A_s':2.123257e-09,
        'n_s':9.686025e-01,
        'z_reio':8.227371e+00,
        # other fixed parameters
        'N_ur':2.0328,
        'N_ncdm':1,
        'm_ncdm':0.06,
        'T_ncdm':0.71611,
        # settings for the output quantites
        'output':'mPk, tCl, pCl, lCl',
        'lensing':'yes',
        'P_k_max_h/Mpc':1.0,
        'z_max_pk': 1088.0, # set redshift
        'non_linear':'halofit',
        }
LambdaCDM.set(input)
LambdaCDM.compute()

kk = np.geomspace(1e-4,3.0,num=1000) # k in h/Mpc
h = LambdaCDM.h() # get reduced Hubble for conversions to h/Mpc
# Note that kk*h is the array of k in 1/Mpc
Pk = LambdaCDM.get_pk_all(kk*h,1088.)*h**3

def pk_callable(array):
    return np.interp(array.flatten(), kk.flatten(), Pk.flatten())

b_length = 300

"""Dimension must be 3 because matter exists in 3D space and is not
only described by angles in terms of latitude and longitude."""
pb = pbox.PowerBox(
    N=256,
    dim=3,
    pk = pk_callable,
    boxlength = b_length,
)

"""Powerbox generates a 3D cube, so take a slice of it manually."""
realization = pb.delta_x()
realization_slice = realization[0, :, :] # grabs a specific layer from the cube to show
plt.imshow(realization_slice, extent=(0,b_length,0,b_length))
plt.colorbar()
plt.show()