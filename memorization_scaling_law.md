# memorization scaling law

labels: experimentation, scaling, learning_theory

1. for any given model architecture and input representation, we can fit a distribution over the number of steps required to memorize that datum to within some fixed tolerance
2. rinse and repeat, increasing the number of inputs to be memorized. we now have a likelihood over ht e number of steps required to memorize some fixed dataset size
3. extrapolate up to give an information-theoretic distribution over the upper bound for time required to fit that dataset
4. correlate to empirical results to estimate some measure of the "information density" of representations from a given dataset as a ratio relative to whatever the "naive" density was.

this "information density" idea is interesting.  I guess I could use some kind of simple toy dataset 

ok ohere how about this

we don't sample a dataset, we sample *a network*, so we're also parameterizing this experiment relative to a particular feasible space. imposing simple constraints on the feasible space might help in various ways.

but ok, let's say theta is some latent for the space of models. we sample a set of weights W1 and use this as our target model. it is frozen and will be used to generate the objective. draw another sample W2, call this the ... ok, W1 is the teacher, and W2 is the student. this is just student teacher learning. so the question is: how long does it take to fit the student, given we constrain ourselves to a dataset of some fixed size.

now from this teacher-student model, we can infer properties over the limits for the efficiency of learning a distribution parameters some given way (the weights) given a dataset of fixed size and an error tolerance.
