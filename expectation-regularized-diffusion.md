# Expectation regularized diffusion process

For a given predicted $\hat{x_0} | x_t$ given by the reverse process, take $k$ samples of $x_{t-1} | \hat{x_0}$ given 
by the reverse process and take the mean to get an expectation for the noise residual

...this might be no different from established ancestral sampling methods
