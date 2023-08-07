# parallel diffusion

![](https://img.shields.io/badge/tag-experimental-lightgrey)


this has to be a thing, right?

let's say we're using 20 steps of some stochastic sampling process.
now imagine we repeat this 8 times from the same init, so 200 steps total to generate 8 (identical?) images.

<< sidebar: i bet there are ways of writing prompts that are better or worse for learning from. >>
<< i wonder who's investigating what linguistic properties are easier or harder to learn? >>

ok back to parallel diffusion

so let's say we do a reduce operation after each parallel step. if there's a little stochasticity between each job, the result won't
be 8 identical images but 8 extremely similar images. the mean of that will probably be a great regularizer for estimating the expectation for sampling at that diffusion step.
BECAUSE OF THE REGULARIZATION, THE SAMPLING PROCESS MAY BETTER TOLERATE TAKING A LARGER STEP.
there's almost certainly an analytic tradeoff between \delta step_size and \delta var(E[X]) (for predicted noise X).
anyway, i'm calling this parallel diffusion because the end game is to run each job on its own GPU, so steps could be performed in parallel.
this will add a little overhead from map-reducing
