# Expectation regularized diffusion process

Per discussion from 2022-10-01 EAI diffusion reading group re: ODE vs SDE sample quality, sounds like this probably wouldn't work very well because this would blur the noise in a way that isn't reflective of how the training data was distributed, but maybe this could be modified to find a medioid of noise residuals.

on that note... maybe we could finetune the reverse process to predict close to this medioid noise residual? 

---

For a given predicted $\hat{x_0} | x_t$ given by the reverse process, take $k$ samples of $x_{t-1} | \hat{x_0}$ given 
by the reverse process and take the mean to get an expectation for the noise residual

...this might be no different from established ancestral sampling methods


