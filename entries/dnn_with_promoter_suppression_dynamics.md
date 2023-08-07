# simulating regional neuronal promotion/suppression in ANN activations

labels: experimental

assign each node a "color" or some other discrete class assignment amenable to state machine rule construction

during an inference pass, sample a "signal arrival index" `idx~U(0,1)` for each weight

construct some simple rules for how proximity between different classes of weights creates interactions to simulate how neurons can make their neighbors more or less prone to firing

e.g. let's say neurons of the same color is a promoting effect, neurons of different colors is a suppressive effect. application of effect is decided based on arrival order.

this feels like it would be hard to compute, might make sense to perform this operation over tiles of weights rather than the whole matrix.
