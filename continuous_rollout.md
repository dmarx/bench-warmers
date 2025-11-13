# Continuous Rollout

labels: experimental

transformer layer where one of the parameters outputs a scalar that governs how many times that layer should be repeated (qua RNN).

Let's call this parameter K, so a given layer is looped max(K,1) times, or multiplied by K if K<1, or the layer is skipped if K<0.

to make this parameter smoothly continuous (for SGD) rather than discrete integer, we interpolate between the `floor(K)` and `ceiling(K)` results, using the
interpolation weight `K - floor(K)`. 

implementation wise: we can just use a while loop and decrement K with each iteration, and then multiply as an interpolation weight when we get to K<1.

Further: use an EM optimization strategy. Fit the non-K parameters first to update the base model, then update the K parameters to update the adaptive depth.

---

what I REALLY want is some kind of adaptive computation strategy that let's the model dynamically select/request/compile circuits to throw at the input.
