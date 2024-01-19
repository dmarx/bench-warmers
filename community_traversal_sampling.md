# community traversal batch sampling

labels: experimental

## motivation

simulate some of the optimizer characteristics inherent in the open source community in an ML training process

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
