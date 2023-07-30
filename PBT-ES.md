# Population-based training + evolutionary strategies via locally correlated constraint

there was a paper recently (the one iwas talking about with peter and nick) that discussed a method for regularizing networks to produce regionally correlated activations. let's call this RCA, probably not what it was actually called.

If you use RCA while also running PBT, this will give you a population with regionally-meaningful diversity. with this in place, we could apply "crossover" mutation strategies, sharing semantically meaningful weight subspaces instead of just random weights.
