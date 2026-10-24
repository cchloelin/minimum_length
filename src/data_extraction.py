import powerbox as pbox
import numpy as np

"""Generate the initial conditions for inflation using the Bunch-Davies Spectrum."""
def bunch_davies(k):
    return np.where(k > 0, 1.0 / (2.0 * k), 0.0)

def initial_conditions():
    b_length = 200.0 # in MPC

    pb = pbox.PowerBox(
        N=256, # per dimension                     
        dim=3,                     
        pk = bunch_davies,
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

#print(initial_conditions())
## Values are too big currently, either scale down by 1e-5 or change units to be Hubble parameter (so smaller than 1)