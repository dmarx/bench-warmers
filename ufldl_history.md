# ELI5: history of the VAE

labels: education, history, vae, feature_learning, publication, history_of_science

https://discord.com/channels/729741769192767510/730095596861521970/1206121483877752862

*TODO: Combine this with papers from the [anthology](https://github.com/dmarx/anthology-of-modern-ml/blob/main/README.md) to provide some structure to the "treat this like a textbook" stuff*

#### Historical context

* 1991 - "Nonlinear principal component analysis using autoassociative neural networks" - Mark A. Kramer
* 2006 - "Reducing the Dimensionality of Data with Neural Networks" - Geoff Hinton, R. R. Salakhutdinov
* 2013 - ["Auto-Encoding Variational Bayes"](https://arxiv.org/abs/1312.6114) - Diederik P Kingma, Max Welling

## Feature Engineering

Let's talk about feature learning. Back in the before times, there was this thing we used to do: we'd sit around the fire, and think about our problems and how to solve them. It was called "feature engineering," and it was a pain in the ass.

When I worked as a data scientist, like 70% of the effort of any problem was just making the data workable. "Workable" means something very different today, in the now-after times. The founders, in their great wisdom and laziness, dreamed of "end-to-end" solutions to their problems. The computer vision people had been especially bogged down in their feature engineering and were the first for whom their frustration overcame their laziness. And thus was born a machine that could learn its own features.

#### Historical context

* early interpretability work
  * linear probing
  * visualizing CNN features, distill
  * 2015 - ["Distilling the Knowledge in a Neural Network"](https://arxiv.org/abs/1503.02531) - Geoffrey Hinton, Oriol Vinyals, Jeff Dean
  * hinton's "dark knowledge" (if there was a second paper? the one with the held out mnist digits)

* feature engineering in the wild (CV)
  * 2014 - ["My solution for the Galaxy Zoo challenge"](https://sander.ai/2014/04/05/galaxy-zoo.html) - Sander Dieleman
  * 1991 - ["Face Recognition Using Eigenfaces"](https://www.cin.ufpe.br/~rps/Artigos/Face%20Recognition%20Using%20Eigenfaces.pdf) - Matthew Turk, Alex Pentland
  * canny edge detection
* feature engineering tooling
  * opencv docs
  * 

## Automatic Feature Learning

Let's consider a simple classification problem. You can model classification with logistic regression. Nice and simple, old-school statistics. Softmax is just multivariate logistic regression. Literally. Where do we often see softmax these days? Last stop on the processing pipeline for a deep neural network. So, pop off that last piece and what are we left with? On the one hand, we have one of the simplest possible classification models. And on the other hand, we have everything else. So it's completely valid to interpret that "everything else" as a machine that constructs complex features on which a simple classifier can operate. This is no big deal now. May even seem obvious. It was not. Not for a very long time.

#### Historical context

## Dimensionality Reduction in Early ML

One of the common themes in feature engineering back in the early ML days was dimensionality reduction. You see, my lovelies, we didn't know about gradient double descent at the time, and misguidedly believed that a consequence of the bias-variance decomposition was that it was bad to have overparameterized models. So, a common component of feature engineering pipelines used to be dimensionality reduction because it was believed that was a way to avoid overfitting. Crystallize the signal out of the data, throw away the noise. As the information density of the representation increases, so then should the generalizability of the model. Pack the input down into just its bare essentials. Find the latent. This line of thought naturally led people to an hourglass-architected MLP. Treat the bottleneck region as the condensed features, and the part after it as a second reconstruction component. Turns out, this procedure is essentially a kind of non-linear PCA.

#### Historical context

## Advent of Word Embeddings

*(TODO: segue to InfoNCE to contrastive learning to CLIP )*

The NLP people heard tell of the success the computer vision people had achieved by leaning into their laziness. They began to adopt tips and tricks that had been demonstrated by their CV brethren. Yet something was missing. Pictures had a natural numeric representation already, but words did not. NLP researchers dealt with this nuisance by counting things and treating words as counts. In the land where people are counting lots of things, the statistician is king. And so it was with NLP. "Counts can be modeled as Poisson distributed random variables!" proclaimed the computational linguists. "We can use our statistical models to understand language!" And this worked for a time. It sure beat the hell out of constructing parse trees and part-of-speech tagging and all that shit. But they also hadn't completely escaped that either.

Fortunately, some mythically lazy NLP researchers had observed the success the computer vision people had achieved, and they wanted in. The computer vision folks had the VAEs, but they didn't understand the value of that yet. They were blinded by their feature engineering machines and ignored the magic of their VAEs, relegating them to tasks like clustering images.

Now, our mythically lazy NLP researchers, they were tired of their shitty features and wanted a simple solution to create good features. Features for our NLP researchers, as mentioned, were counts. Of specific words (or sequences of strings), which meant if you wanted to use these techniques, you had to pick your words ahead of time and ignore all the other words. Wordlists were all the rage: stop word lists, WordNet lemma graph, stemming rules. It was rough. And thus was born: Word2Vec.

Word2Vec was still a wordlist, but it was an extremely useful wordlist. And it mapped words not to counts but to dense vectors. The lazy researchers realized they could combine the VAE trick with masking to construct a reconstruction loss based on word context, and therefore representations based on word context. The Word2Vec authors shared their pretrained model with the world. Pre-trained embeddings became the hot new thing. ___2Vec was all you needed to get published.

"We're doing deep learning!" proclaimed the NLP researchers proudly slapping themselves on the back. But they were not. They were only doing shallow learning. Word2Vec, it turned out, was just doing an implicit matrix factorization. But nobody cared because they finally got to be lazy like their CV friends. In fact, they got to be even lazier. They soon realized they didn't even need the fancy deep learning architectures to achieve most of their goals, as long as they started from a lookup table of pre-trained embeddings. "Word2Vec + logistic regression? Good enough!" said basically everyone. They had discovered transfer learning, and it was good.

#### Historical context

## VAEs to GANs

The computer vision people had enjoyed their time with the VAE, but had decided they outgrew it. A simple reconstruction loss was not enough; they needed more losses. They moved on from encoder-decoder to generator-discriminator. Instead of the latent representation being the bottleneck, it was the input for both models. The computer vision people had discovered the z-space, and felt quite fancy there.

But their models were getting chonkier and chonkier. Am I saying the StyleGAN architecture was a conspiracy by NVIDIA to get people to buy more compute? No, of course not, but if it was, it worked. And then from the z-space, came the w-space. The activation space, baby.

The GAN folks had been treating the input vector as their main "latent," but there was another dense feature representation they'd ignored. They'd forgotten that they could interpret deep networks as feature engineering machines, and discovered they'd been sitting on a pile of useful features inside the network. Z-space, w-space, w+ space.

Mechanistic interpretability was becoming all the rage. The VAE, however, was stuck in dimensionality reduction land. Beta-VAE, sparse VAE,... that latent had to be as DENSE AS POSSIBLE.

#### Historical context

## The Return of the ~~King~~ VAE

One day, some computer vision researchers in Germany had an insight. Let's use the VAE to learn features for a GAN. The VAE had announced its triumphant return. It would be used to learn a feature dictionary for the GAN. And thus was born the VQGAN. Yadda yadda diffusion, yadda yadda Stable Diffusion.

Happily ever after. Thank you for attending my TED talk.
