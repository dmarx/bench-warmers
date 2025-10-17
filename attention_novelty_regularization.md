# Attention Feature reuse via novelty regularization

labels: experimental

parameterize a transformer model as a collection of modules whose features are quantized into two or more code books:
* a strictly local codebook that is costly to invoke.
* a global codebook that the model is incentivized to invoke.
* one or more "neighborhood" codebooks that permit feature overlap in adjacent layers

features in the global codebook can be accessed anywhere in the model and reuse is encouraged. we can make this explicit by adding a multiplicity reward

maybe we could add a mixture/ motility component? use the multiplicity to motivate promoting/demoting features from one codebook to another.

promote feature diversity by regularizing global-local codebook similarity scores (i.e. push local representations away from global counterparts. force local codes to specialize)


## problem: the QKV matrices are projections on the input space, not fixed feature collections.

potential solution: rather than using those projections directly, we map them to their quantized (codebook) nearest neighbors, subject to some proximity threshold.
proposed features (i.e. vectors in the projection) that don't satisfy the threshold can then comprise the costly local codebook, 
and we can penalize proportional to the cardinality of the codebook, i.e. the number of proposed features outside the threshold.

--- 

## relevant research

* Attention reuse - https://www.semanticscholar.org/reader/fb486b63058925d762317992efa65e3cd6f188de
* tokenize the linear projections - https://www.semanticscholar.org/reader/2c48cddf1ce5cc99b257becd508ab929b0888daf
  * https://github.com/Haiyang-W/TokenFormer
  * built upon by https://arxiv.org/pdf/2508.01167 for lifelong learning
* attention parameters as linear combination ofshared "atoms" - https://www.semanticscholar.org/reader/4e07feb4482d061d8c99cde3bc1ea08ea2c2a4a1
