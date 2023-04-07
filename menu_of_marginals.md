# accelerated finetuning with "menu of marginals"

![](https://img.shields.io/badge/tag-experimental-lightgrey)


tldr: front-load a bunch of compute to warmstart the process

...the more I think about it, the more this feels like a "that would probably work, but would cost more money than it would save"

---

1. compute a clustering of your training data in representation space
2. finetune a model to each cluster

we can treat each model as the marginalized distribution for that cluster.

1. now, take any incoming finetuning task, and project it into cluster space.
2. use this projection to compute cluster responsibilities.
3. use cluster responsibilities as weights for a model merge as a linear combination of the menu of marginals.
