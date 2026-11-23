# Defining Minimum Length Scale Thresholds Using Theoretical Simulations
**Research Question:** What is a threshold for minimum length scales that provide a comparable framework with standard cosmological models? (?)
## Motivations
Whether or not the universe is discrete or continuous has been debated since ancient times. In the modern era, the two primary frameworks used to describe the universe, general relativity and quantum mechanics, fail to provide a solution in extreme environments. Under these conditions, general relativity predicts singularities whilst the quantization of gravity under quantum mechanics leads to nonrenormalizable infinities that do not yield any physical predictions, despite each theory being well-tested in their own regimes. The Planck Length (1.6 * 10^-35 m) is the current "minimum length" in which any attempts at measurement or calculation begin to break down, derived from the constants h, G, and c. However, whether or not this length describes an actual discrete universe or if there is just a fundamental gap in our understanding of the universe is still unknown. Paradigms such as String Theory and Loop Quantum Gravity are proposed unifications between general relativity and quantum mechanics which may provide a solution to this question, but none have been particularly favored or proven, leaving the question open.
## Methodology
1. **Establish the initial conditions of the inflaton field** -- We used the Bunch-Davies spectrum in the program powerbox, which generates a Gaussian Random Field based on a given equation. Since the Bunch-Davies spectrum inherently describes the quantum fluctuations experienced by the inflaton field, which are inherently Gaussian, this process works out.
3. **Implement a minimum length scale** -- Minimum lengths can be interpreted as limits on spatial and temporal resolution, making them implementable through blurring. Gaussian blurring was thus used because of how it handles edges and provides a more realistic result compared to other methods of blurring, such as box filters.
4. **Evolve initial conditions through inflation** -- W.I.P
5. **Extract data** -- Powerbox provides a get_power function that can be used to extract the primordial power spectrum values from the real-space simulation with the minimum-length implementation.
6. **Evolve to the modern era** -- In order to compare real-world data from the modern era to our simulated data, our data must be evolved to the modern era, which can be done with CLASS by simply feeding it properly formatted primordial power spectrum values that were just extracted.
## Data Analysis
COBAYA was used for data analysis due to its compatibility with CLASS and its relevance for what this project is testing. 
## Results
W.I.P
