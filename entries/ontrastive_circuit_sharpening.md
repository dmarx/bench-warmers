# contrastive circuit sharpening

## inspiration

* https://twitter.com/pvllss/status/1684975462282342406
* https://epochai.org/blog/trading-off-compute-in-training-and-inference


## analogy 

* to human learning: when we get the answer wrong, it helps a lot to be told what we could've done differently.

# procedure

1. for a given contrastive target, generate multiple samples.
2. rank them and use a continuous transform/approximation of that ranking as a contrastive loss. this should be structured such that only the single best or handful of really good samples are given good scores


