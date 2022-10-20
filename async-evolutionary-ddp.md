# random batch + random average for massive asynchronous data-parallel training

![](https://img.shields.io/badge/tag-experimental-lightgrey)
![](https://img.shields.io/badge/tag-foundation-lightgrey)
![](https://img.shields.io/badge/tag-tooling-lightgrey)


chunk up a dataset so each GPU only sees its own chunk. draw a poisson sample at each GPU. call this K. 
Let K denote the number of epochs to run on this GPU before performing a "merge" procedure with a neighboring training process.
After K epochs, training process W1 will draw a sample neighboring process W2 to merge with. 
W2 pauses(/halts?) its current process, updates its weights to be a linear combination of the incoming weights (EMA? scale up EMA term over time?).
W2 unpauses, W1 draws a new sample K.
Monitor norm of updates. Iterate until magnitude of update converges.

provable guarantees? probabaly! But who cares? let's see what happens first and then do the analysis later. 

modifications:

* track validation confidence for each training datum. Pass data around as well.
  * compute some measure of pairwise model similarity (CKA?)
  * models that are less similar exchange higher(?)/lower(?) confidence data
  * data that tracks high confidence across different models gets downsampled to a reserve set that gets sampled less frequently until it effectively is "retired"
  * data that tracks low confidence across different models continuously gets passed around
    * would want to keep track of what models have visited that data
* rather than exchanging individual data points, swap models on GPUs. 
  * can condition sampling strategy on data confidence and how long its been since that checkpoint has seen that data
  * there are probably some good learnable hyperparameters here. 
* I could probably do a really low-scale experiment of this on MNIST using RayTune's fractional GPUs and asyncio.
* add in some notion of worker "communities" that exchange with each other more or less often
  * certain sets of weights might be more suited to merging than others. 
  * should result in an early segmentation of the solution space, slowly converging over time.
  * this feels like a job for agglomerative HClust.
* For computing checkpoint-checkpoint similarity, I could probably construct some sort of random projection matrix for dimensionality reduction
  * build it once, don't even train it
  * it will have an impact on the training process, so the models will implicitly be forced to adapt to its presence since it will impact weight updates (merges)

