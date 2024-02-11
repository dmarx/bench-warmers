# ELI5: history of the VAE

labels: education, history, vae, feature_learning, publication

https://discord.com/channels/729741769192767510/730095596861521970/1206121483877752862

let's talk about feature learning
so back in the before times, there was this thing we used to do
we'd sit around the fire, and think about our problems and how to solve them

it was called "feature engineering" and it was a pain in the ass

when i worked as a data scientist, like 70% of the effort of any problem was just making the data workable
"workable" means something very different today
in the now-after times
the founders, in their great wisdom and laziness, dreamed of "end-to-end" solutions to their problems
the computer vision people had been especially bogged down in their feature engineering, and were the first for whom their frustration overcame their laziness
and thus was born a machine that could learn its own features 
let's consider a simple classification problem
you can model classification with logistic regression. nice and simple, old-school statistics
softmax is just multivariate logistic regression
literally
where do we often see softmax these days? last stop on the processing pipeline for a deep neural network
so pop off that last piece and what are we left with?
on the one hand, we have one of the simplest possible classification models
and on the other hand, we ahve everything else
so it's completely valid to interpret that "everything else" as a machine that constructs complex features on-which a simple classifier can operate
this is no big deal now. may even seem obvious
it was not. not for a very long time
one of the common themes in feature engineering back in the early ML days was dimensionality reduction

you see my lovelies, we didn't know about gradient double descent at the time, and misguidedly believed that a consequence of the bias variance decomposition was that it was bad to have overparameterized models
so a common component of feature engineering pipelines used to be dimensionality reduction because it was believed that was a way to avoid overfitting
crystallize the signal out of the data, throw away the noise
as the information density of the representation increases, so then should the generalizability of the model
pack the input down into just its bare essentials. find the latent
this line of thought naturally led people to an hourglass architectured MLP. treat the bottleneck region as the condensed features, and the part after it as a second reconstruction component
turns out, this procedure is essentially a kind of non-linear PCA

the NLP people heard tell of the success the computer vision people had achieved by leaning into their laziness
they began to adopt tips and tricks that had been demonstrated by their CV brethren
yet something was missing
pictures had a natural numeric representation already, but words did not
NLP researchers dealt with this nuisance by counting things
and treating words as counts
in the land where people are counting lots of things, the statistician is king. and so it was with NLP
"counts can be modeled as poisson distributed random variables!" proclaimed the computational linguists. we can use our statistical models to understand language!"
and this worked for a time
it sure beat the hell out of constructing parse trees and part-of-speech tagging and all that shit
but they also hadn't completely escaped that either
fortunately, some mythically lazy NLP researchers had observed the success the computer vision people had achieved
and they wanted in
the computer vision folks had the VAEs, but they didn't understand the value of that yet
they were blinded by their feature engineering machines and ignored the magic of their VAEs, relegating to them to tasks like clustering images

now, our mythically lazy NLP researchers, they were tired of their shitty features and wanted a simple solution to create good features
features for our NLP researchers, as mentioned, were counts. of specific words (or sequences of strings)
which meant if you wanted to use these techniques, you had to pick your words ahead of time and ignore all the other words
wordlists were all the rage
stop word lists
wordnet lemma graph
stemming rules
it was rough
and thus was born: word2vec
word2vec was still a wordlist
but it was an extremely useful wordlist
and it mapped words not to counts but to dense vectors
the lazy researchers realized they could combine the VAE trick with masking to construct a reconstruction loss based on word context, and therefore representations based on word context
the word2vec authors shared their pretrained model with the world
pre-trained embeddings became the hot new thing
___2vec was all you needed to get published

"we're doing deep learning!" proclaimed the NLP researchers proudly slapping themselves on the back
but they were not
they were only doing shallow learning
word2vec, it turned out, was just doing an implicit matrix factorization
https://papers.nips.cc/paper/2014/file/feab05aa91085b7a8012516bc3533958-Paper.pdf
but nobody cared because they finally got to be lazy like their CV friends
in fact, they got to be even lazier
they soon realized they didn't even need the fancy deep learning architectures to achieve most of their goals, as long as they started from a lookup table of pre-trained embeddings
"word2vec + logistic regression? good enough!" said basically everyone 
they had discovered transfer learning, and it was good
the computer vision people had enjoyed their time with the VAE, but had decided they outgrew it
a simple reconstruction loss was not enough, they needed more losses
they moved on from encoder-decoder to generator-discriminator
instead of the latent representation being the bottleneck, it was the input for both models
the computer vision people had discovered the z space, and felt quite fancy there

but their models were getting chonkier and chonkier
am i saying the stylegan architecture was a conspiracy by nvidia to get people to buy more compute? no of course not, but if it was it worked
and then from the z space, came the w space
(by the way, z = normal random variable, w = weights)

the activation space baby
i'm baked, w doesn't equal weights

the GAN folks had been treating the input vector as their main "latent", but there was another dense feature representaiton they'd ignored

they'd fogotten that they could interpret deep networks as feature engineering machines, and discovered they'd been siting on a pile of useful features inside the network
z space, w space, w+ space

mechanistic interpretability was becoming all the rage
the VAE however, was stuck in dimensionality reduction land
beta-VAE, sparse vae, .... that latent had to be as DENSE AS POSSIBLE

one day, some computer vision researchers in germany had an insight
let's use the VAE to learn features for a GAN

the VAE had announced its triumphant return
it would be used to learn a feature dictionary for the GAN
and thus was born the VQGAN
yadda yadda diffusion, yadda yadda stable diffusion

happily ever after
thank you for attending my TED talk
