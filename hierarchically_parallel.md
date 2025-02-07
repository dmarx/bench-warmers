# Hierarchically parallel langevin training

labels: experimentation

* hierarchically nested gradient accumulation/parameter updates 
* each level of the hierarchy updates at a fraction of the cadence of the level below it
* include a (parameter interpolation) term that interpolates to the root (highest level set of parameters that accumulates over all models) -> global control over spread
* include a parameter that interpolates to the level above: local spread/gravity


## relevant work

* diffusion as evolution
* that recent federated learning thing? kerras might've been involved?
