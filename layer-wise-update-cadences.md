# layer-wise update cadences

![](https://img.shields.io/badge/tag-wip-lightgrey)


use gradient accumulation where each layer has its own respective accumulation cadence

i.e. different layers see different sized batches

which also has the consequence that certain layers will update more slowly, which forces us to be more sure about each step

my suspicion is that one of these configurations is best, but i don't have a good intuition for which one that would be:

- output layer has the fastest cadence and updates more frequently with higher variatiance. this will hopefully "pull" the slower gradients into interesting regions to explore
- the lower level features are more fixed. the GAS cadence is proportionate to our "confidence" in that layer's representation, and we'd expect these lower layers to learn first
- because we need the lower layers to be confident for the above scheme to work, maybe this only works for a particular phase of training, like late phase

this is a separate idea now

what if we used network compression/pruning methods mid-training?

this is reminisscent of the "electroshock" training idea, but maybe less random or less often? like, at the end of each epoch or each k batches

another new one...

what if we use CKConv to expand the filters ... or more generally, what if we somehow attach additional capacity to a network?
concatenate in some additional capacity where all the outgoing weights towards already-trained parameters are down-weighted by a scalar alpha that is
common across the whole new component, so we can "phase in" the new capacity by scaling up alpha.

oh shit what if we did channel-wise gradient updates? or really any scheme that would divide the gradient updates "vertically" in addition to the horizontal
gradient updates of back prop. literally: orthogonal updates.

we could even apply the GAS cadence idea here. divide each layer into quadrants, and assign each quadrant its own cadence. so each layer has a regions that learn
slowly, and regions that learn faster

... I think I may just be re-inventing ADAM here. I should go re-read that paper. and play with these weird training method ideas
