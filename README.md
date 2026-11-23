# Defining Minimum Length Scale Thresholds Using Theoretical Simulations
Research Question: What is a threshold for minimum length scales that provide a comparable framework with standard cosmological models? (?)
## Motivations
Whether or not the universe is discrete or continuous has been debated since ancient times. In the modern era, the two primary frameworks used to describe the universe, general relativity and quantum mechanics, fail to provide a solution in extreme environments. Under these conditions, the math begins to result in nonsensical infinities which cannot yield any physical predictions. The Planck Length (1.6 * 10^-35 m) is the current "minimum length" in which any attempts at measurement or calculation begin to break down. However, whether or not this length describes an actual discrete universe or if there is just a fundamental gap in our understanding of the universe is still unknown.
## Methodology
1. _Establish the initial conditions of the inflaton field_ -- We used the Bunch-Davies spectrum in the program powerbox, which generates a Gaussian Random Field based on a given equation. Since the Bunch-Davies spectrum inherently describes the quantum fluctuations experienced by the inflaton field, which are inherently Gaussian, this process works out.
3. _Implement a minimum length scale_ -- Minimum lengths can be interpreted as limits on spatial and temporal resolution, making them implementable through blurring. Gaussian blurring was thus used because of how it handles edges and provides a more realistic result compared to other methods of blurring, such as box filters.
4. _Evolve initial conditions through inflation_ -- W.I.P
5. _Extract data_ -- Powerbox provides a get_power function that can be used to extract the primordial power spectrum values from the real-space simulation with the minimum-length implementation.
6. _Evolve to the modern era_ -- In order to compare real-world data from the modern era to our simulated data, our data must be evolved to the modern era, which can be done with CLASS by simply feeding it properly formatted primordial power spectrum values that were just extracted.
## Data Analysis
COBAYA was used for data analysis due to its compatibility with CLASS and its relevance for what this project is testing. 
## Results
W.I.P
