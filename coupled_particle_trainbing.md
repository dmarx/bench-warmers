# coupled particle training

labels: experimental, statistical-mechanics

chain -> lattice -> fluid constrained to a manifold

coupled particles explroing a space

square lattice of particles exploring a flat basin

one particle finds a promising new direction: we want the mass of the collective to shift towards that particle, such that it has the potential to pull the colelctive along

imagining the lattice structure as a constraint to have roughly fixed distances between particles connected by spring forces, we just need to give the particles mass and make the springs reasonably tensile.

but taking it a step further, we could treat the springs as pipes and imagine that some fraction of the "interconnected pipe volume" of the lattice contains a fluid with some viscosity

we can also anneal training by expanding or contracting the spring force, or rather the effective distance apart the particles "want" to be

associate with each particle a set of model parameters being trained together to parameterize a single model as the collection of parameters

when training progress slows, we can increasing the inter-model repelling force

I think this is effectively adding a higher order gradient?I think the water effectively parameterizes the hessian here.

the way I described thsi would be crazy expensive to implement. at any given step, we apply the "repelling" loss only to a specific (or random?) set of parameters. my intuition is to choose these parameters randomly to apply this loss stochastically across all layers, but it actually might be sufficient to couple the models across a single layer. keep this layer fixed throughout training? bottom layer? top?
