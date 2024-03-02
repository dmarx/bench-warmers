# memorization scaling law

labels: experimentation, scaling, learning_theory

1. for any given model architecture and input representation, we can fit a distribution over the number of steps required to memorize that datum to within some fixed tolerance
2. rinse and repeat, increasing the number of inputs to be memorized. we now have a likelihood over ht e number of steps required to memorize some fixed dataset size
3. extrapolate up to give an information-theoretic distribution over the upper bound for time required to fit that dataset
4. correlate to empirical results to estimate some measure of the "information density" of representations from a given dataset as a ratio relative to whatever the "naive" density was.
