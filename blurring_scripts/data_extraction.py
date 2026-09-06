import powerbox as pbox
import numpy as np

"""Generate a realization of the primordial power spectrum"""
def dimensionless_primordial(k, As=2.123257e-09, ns=9.686025e-01, k_pivot=0.05):
    return As * (k/k_pivot) ** (ns-1)

def dimensionful_primordial(k):
    return (2*np.pi**2)/k**3 * dimensionless_primordial(k)

def primordial_realization():
    b_length = 1000.0

    pb = pbox.PowerBox(
        N=10, # per dimension                     
        dim=3,                     
        pk = dimensionful_primordial,
        boxlength = b_length,
        seed=1010           
    )

    """Extract real-space values"""
    # Random-variable values
    random_values = pb.delta_x()

    # Coordinates
    x_coords, y_coords, z_coords = np.meshgrid(pb.x, pb.x, pb.x, indexing='ij')

    # X, Y, Z coordinates and corresponding random variable.
    points_values = np.column_stack(
        (x_coords.ravel(),
        y_coords.ravel(), 
        z_coords.ravel(), 
        random_values.ravel())
        )

    # points_values is in the form of a numpy array, which is not the same as a nested python list.
    return points_values

print(primordial_realization())