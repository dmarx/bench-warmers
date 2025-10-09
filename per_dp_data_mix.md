# per node data mix

labels: experimental, distributed_training

structure a large cluster's data mix as an LDA process. Treat each dataset as a topic, with the target global data mix as the prior. then sample a per-node (node = data parallel rank) topic vector from the prior to assign a per-node data mix.

for extra fanciness, add a temperature term so we can jointly anneal the cluster towards or away from similarity wrt the prior.
