# sandbox to probe scaling laws for representation learning

labels: experimental


inspired by "generative wiki rabbit hole"

early graph assumes homogeneity of node and edge types.

certain nodes actually designate community membership. treating community nodes as conventional results in extremely dense graph, eliminating a lot of the desired structure.

structure can be recovered by pojecting membership nodes up into an orthogonal dimension, i.e. layering on a hypernetwork channel for each community...

mmm... i dunno. what i want is for this to be a multi-partite projection

...

anyway, underlying mechanisms aside, my thinking is that i could construct toy graphs and see under what conditions a transformer learns the multi-partite topology. 

use a "next token prediction" objective, where sequences are random paths through the graph, and tokens are nodes

should be able model learning dynamics of NLU under this simplification?

---

track curvature at each node throughout process. Use Fisher Information Matrix as an approximation for the local curvature

- We have the FIM for the *parameter space*, not for the representaton space. for this, we'd need a way to assign a likelihood to each observation.
