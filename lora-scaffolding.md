# LoRA as Training Scaffolding

labels: experimental, learning-theory, training-dynamics

start training with model parameterized as a LoRA, to (at least? (early?)) convergence. zero-init full model, anneal-in the free weights,
while annealing down the LoRA's contribution to the training objective. inductive bias for structure aligned with LoRA.

can maybe use the original scaffolding to init new LoRA's?
