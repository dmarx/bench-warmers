# minibatch bootstrapped gradients

![](https://img.shields.io/badge/tag-wip-lightgrey)  
![](https://img.shields.io/badge/tag-training-lightgrey)  
![](https://img.shields.io/badge/tag-experimental-lightgrey)  
![](https://img.shields.io/badge/tag-optimization-lightgrey)


sort of like a data augmentation, but more like a gradient regularization. for some large batch, accumulate gradients over bootstrap resamples from that minibatch.
for n resamples, divide learning rate by n (?)... or not? or multiply? i dunno. to do: investigate hyperparameter scaling in this regime. sheesh.
