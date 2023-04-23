# twin mixing bootstrap regularization

![](https://img.shields.io/badge/tag-completed-darkgreen)  
![](https://img.shields.io/badge/tag-experimental-lightgrey)  
![](https://img.shields.io/badge/tag-interpretability-lightgrey)  
![](https://img.shields.io/badge/tag-regularization-lightgrey)


(followup idea from "paired dropout" - constrianing drop out to only sample one index from a pair and pair up all weights)

* have two copies of a model in memory. for each batch of data, split it in half and only let each set of weights see a respective half batch.
* backprop
* randomly exchange weights

once this is done, switch data batches and repeat

should be functionally similar to "paired dropout", but doubling (quadrupling?) data efficiency.

interpretable as a learned per-parameter variance prior

... actually, could probably even just bootstrap over the same sample in memory for a while
