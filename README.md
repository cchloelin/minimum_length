# Testing Minimum Length Constraints and Their Impact on the CMB

## Research Question: What is the largest minimum length value that leaves a significant impact (specified later) on the CMB and its power spectra when compared with standard cosmological models? (?)

## Current pipeline:
1. Blur the data using the average of the points within a certain radius (which represents the minimum length) in powerbox.
  * Powerbox is fed an arbitrary power spectrum to generate a specific realization, which is then evolved with the minimum length constraint using a unique script.
  * Real-space data is extracted once inflation ends.
2. Extract this data from powerbox and place it in a table in a separate file.
  * pb.delta_x() --> extracts real space random variable values from each point.
  * pb.x --> extracts spatial coordinates along a speciifc axis in the realization. Because the box is a square (or cube), all points can be found through combinations of the values returned.
  * Four columns: x, y, z, random variable value.
3. Feed the data into the external_Pk module in CLASS to get the desired primordial power spectrum.
4. Configure the CLASS code parameters to use the primordial power spectrum with the minimum length constraints, then run the CMB realization codes and generate required graphs.
5. Data analysis using statistical analysis with MontePython or COBAYA
  * Should extract the largest minimum length constraint which leaves a significant change to the CMB. So, an upper bound for a possible minimum length in the CMB today (?)
  * Leaning towards COBAYA
