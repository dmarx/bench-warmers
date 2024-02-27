# LoRA as a Topic Model

labels: experimental, nlp, finetuning

Very broadly, a topic model is just a hierarchical model where members are assigned soft responsibilities relative to the global categories. 

the soft responsibility assignments are given by a vector, which represents the member as a linear combination of the parent categories.

hyper-lora functions very similarly, but samples a random linear subspace from which to assign responsibilties.

we can use a LoRA to learn a common subspace, and then modulate per-member with a learned vector assigned to each member.

LoRA can be decomposed into two parts, an up matrix and a down matrix. Call these `U` and `V`. (Initialize `U` and `V` by fitting the whole corpus?)

Let `x` be a document vector. We use a common up matrix `U` for the entire corpus, but each member will have a modulated down matrix, `Vx`

It might be better to flip this, so the up matrix is modulated and the down matrix is global. Not sure, might not make a difference. 

Could also learn a vector of per-module weights, so `x` gets scaled differently per-layer.

Under this interpretation, we could actually let `V` be global and then have a separate matrix `A` for the subspace x gets applied to.

So then the LoRA `UV` becomes `U(V+A*x)` where `U` and `V` are learned globally, `A` is either learned globally or a fixed random subspace, `*` is a hadamard product, and `x` is learned per document, initialized to 0, and L2 regularized.

This way, we encourage the network to represent as much common information in the `UV` subspace as possible, while also leaving some flexibility to learn a per-document `UAx` modulation.

So once we have this... what does it give us?

* `|x|` could be interpreted as an outlier or uniqueness metric
* `cos(x_i, x_j)` very likely gives us a similarity and could be used for document clustering
* Instead of loading whole documents into a RAG context, you could retrieve the per-document modulations for the top K most relevant documents and construct a per-query LoRA that preferentially carries topic-specific information w/o consuming any context tokens
  * under this interpretation, document vectors are functionally knowledge plugins.
    * but if this is accurate, we'd expect to be able to sum over knowledge plugins and get something similar to what we'd have had if we'd just learned a single LoRA
    * this means we want an inductive prior towards the distribution over `x` vectors being multi-uniform
    * I think we get this for free if we set `A` to a fixed random matrix rather than permitting it to be learnable.
      * concretely, this would give us an expectation that summing over `Ax`'s would give us random noise. in the formulation above we'd want summing over them to give us 0
      * an alternative formulation could have per-document learnable terms on both sides of the equation, which I think would then give us an easier inductive prior for `(A*x)(A*y)'`=I` or something like that
      * So then we'd have each document vector actually being two vectors, `x` and `y`, and then we're fitting the LoRA given by `(U+A*x)(V+A*y)` or something like that
      * Part of my original reasoning for only having the per-document component in one of those two matrices though was to ensure we had an inductive prior for learning global information.
      * I'm concerned that having per-document learnable components on both sides of that equation will promote overfitting. Just gotta heavily regularize `x` and `y` I guess.
