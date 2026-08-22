# Testing Minimum Length Constraints and Their Impact on the CMB

## Research Question: What is the largest minimum length value that leaves a significant impact (specified later) on the CMB and its power spectra when compared with standard cosmological models?

## Current pipeline:
1. Blur the data using the average of the points within a certain radius (which represents the minimum length) in powerbox.
  * The power spectrum fed into powerbox should be the regular primordial power spectrum, with no minimum length constraint.
  * Blurring of data is probably done using a unique script?
2. Extract this data from powerbox and place it in a table in a separate file.
  * Use the function get_power(real_space_values, boxlength)
3. Feed the data into the external_Pk module in CLASS to get the desired primordial power spectrum.
4. Configure the CLASS code parameters to use the primordial power spectrum with the minimum length constraints, then run the CMB realization codes and generate required graphs.
5. Data analysis using statistical analysis with your own code or other modules (to come..)
  * Should extract the largest minimum length constraint which leaves a significant change to the CMB. So, an upper bound for a possible minimum length in the CMB today.
