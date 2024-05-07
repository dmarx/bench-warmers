# contrastive learning of graph/manifold hierarchy

parameterize each level of the hierarchy as a code book. Assume the code book entries map directly to meta-nodes. The meta-graph describes inter-community relationships at some depth of the hierarchy.

the assignment of codebook entries to nodes of the knowledge graph (over the data) is one-to-many. Each node maps to a single meta-node, and meta-nodes can map to many nodes. 

now, run DeLIP or CLIP or whatever contrastive objective over the pairings. so the node -> meta-node assignments can be parameterized as a classifier that is conditioned on some learnable vector, and we learn that vector through tthe CLIP objective on the pairings.
