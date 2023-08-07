# Notes on differentiable permutations

labels: experimental, interpretability, regularization, differentiable_permutation

since this is apparently something I've been thinking about on and off in the context of learning functional regions for interpretability and evolutionary strategies

* [Learning Representations of Sets through Optimized Permutations ](https://openreview.net/pdf?id=HJMCcjAcYX) - Has a cost function for scoring permutations matrices
  * https://github.com/Cyanogenoid/perm-optim/blob/master/permutation.py
* [Learning Permutations with Sinkhorn Policy Gradient](https://paperswithcode.com/paper/learning-permutations-with-sinkhorn-policy) - "Sinkhorn layer produces continuous relaxations of permutation matrices"
* https://paperswithcode.com/paper/git-re-basin-merging-models-modulo
* [Learning Latent Permutations with Gumbel-Sinkhorn Networks](https://arxiv.org/abs/1802.08665)

----

1. assign a learnable parameter that will serve as a permutation matrix
2. segment weights into (non overlapping?) tiles, post-permutation
3. compute per-tile activation variances (sampled tiles?)
4. define the permutation score as a statistic over the per-tile variances (e.g. sum, mean, p90...)
5. learn the permutation matrix which minimizes the permutation score
