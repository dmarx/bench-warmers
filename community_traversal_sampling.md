# community traversal batch sampling

labels: experimental

## motivation

simulate some of the optimizer characteristics inherent in the open source community in an ML training process

### discussion

one of the reasons that open source development is so effective is that it creates opportunity for different people to contribute who respectively are more or less concerned with different problem domains. let's model a developer as a distribution over the problem domains that interest them, analogous to modeling a document as a distribution over topics (LDA). dual to the developers, we model projects as distributions over problem domains. we can therefore characterize a problem domain by the projects and/or the developers associated with it. when some developer D contributes to some project P, they are informing that project with the priorities they learned from the problem domains that are their focus, a neghiborhood around D in the problem domain manifold. projects spread through developer communities, so the next person to contribute is likely to have interests similar to the person who introduced them to the project. we simulate this "development homophilly" effect by traversing the neighborhood.

## basic idea

**graph construction**

1. cluster the data
2. treat clusters as nodes
3. construct edges using (?) process. for now, let's assume erdos-renyi random graph
4. pick some node `ROOT` at random to start the process.

**local sampling**

5. sample `k` nodes from the neighborhood of `ROOT`. call the union of data objects in this set of k+1 nodes our "batch community".
6. sample a training batch of size `n` from the batch community.

**graph traversal**

7. sample a neighbor from ROOT and use this as the new ROOT

## replace the graph with a learned manifold

create opportunity for a mechanism which lets the learning process structure the data space and explore it however it likes, so it can e.g. spend more time learning 'x' thing, or associate related exemplars for some feature it is close to learning.)

1. associate each datum with a learnable vector.
2. use neighborhoods in the vector space of a given `ROOT` datum/batch as "batch communities".
3. compute an outter gradient to update the learnable vector
