# Population Convergence Training

label: experimental

population-based training with RNAring/bacteria thing. 

* let M be the population of models m. let k be a threshold percentage.
* initialize the models separately (?)
* each model sees different datum (?)
* at gradient step, top k % of gradients magnitude is shared between models.
  - for each model m, calculate the gradient. find the kth-percentile of the gradient components' magnitudes, and censor everything below this threshold magnitude.
* start k at 0 (no information shared), increasing to 1 (model parallel).

should function similar to summing the noise from multi-condition desnoising
