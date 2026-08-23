from classy import Class
import powerbox as pbox
import matplotlib.pyplot as plt
import numpy as np

LambdaCDM = Class()
LambdaCDM.set_baseline('p18lb')
LambdaCDM.compute()

# lensed power spectrum up to multipole 2500
cls = LambdaCDM.lensed_cl(2500)
# multipoles l
ll = cls['ell'][2:]
# get CMB ee spectrum C_l^EE
clEE = cls['ee'][2:]

"""Need to make the power spectrum a callable function."""
def clee_callable(array):
    return np.interp(array.flatten(), ll.flatten(), clEE.flatten())

"""Box length should be in terms of radians."""
b_length = np.radians(10)
pb = pbox.PowerBox(
    N=512,
    dim=2,
    pk = clee_callable,
    boxlength= b_length,
    ensure_physical=True
)

plt.imshow(pb.delta_x(), extent=(0, b_length, 0, b_length))
plt.colorbar()
plt.show()
