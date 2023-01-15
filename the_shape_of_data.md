# The Shape Of Data

![](https://img.shields.io/badge/tag-publication-lightgrey)

(originally via self-email, 2021-07-05)

Popular science book describing for normal people geometric stuff in ML (e.g. embeddings, gaussian annulus, cosine similarity, manifold hypothesis)

yo let's just make this a "dave's greatest hits" and aggregate, organize, and expand on stuff i've already ranted about online? e.g. reddit comments, CrossValidated, twitter, etc. hell, i can just grow keep growing this whenever I make a high effort comment somewhere.

maybe "greatest hits" should even be its own repo with its own specialized CI thing?

## Misc topic ideas

* intro (+misc)
  * stats is not maths - https://stats.stackexchange.com/questions/78579/stats-is-not-maths/78732#78732
  *  https://stats.stackexchange.com/questions/76406/explaining-a-boxplot-and-providing-a-reference-in-a-technical-paper/76407#76407
    *  "You will rarely be criticized for being too explicit, but it's easy to criticize for being too ambiguous. As a rule of thumb, make as few assumptions about your readers as possible."
  * sourcing myself
    * https://stats.stackexchange.com/users/8451/david-marx?tab=answers&sort=votes  
  * external
    * whuber - pdfs - https://stats.stackexchange.com/questions/4220/can-a-probability-distribution-value-exceeding-1-be-ok/4223#4223 
  * area and integrals - https://stats.stackexchange.com/questions/73972/what-situations-models-require-calculating-the-area-under-a-curve/73973#73973  
  * philosophy of hypothesis testing - https://stats.stackexchange.com/questions/125841/is-h-0-being-a-closed-set-a-convention-in-hypothesis-testing/125881#125881
  * statistical significance - https://stats.stackexchange.com/questions/86162/what-does-it-mean-for-a-variable-to-be-statistically-significant/86167#86167
  * memorylessness - https://stats.stackexchange.com/questions/320854/example-of-memorylessness-of-a-poisson-process/320859#320859
  * holdout reuse - https://datascience.stackexchange.com/questions/26894/to-be-useful-doesnt-a-test-set-often-become-a-second-dev-set/26897#26897
* distances and similarity
  * bag of words
  * tf-idf
  * word2vec - https://datascience.stackexchange.com/questions/26683/does-it-make-sense-to-combine-pca-with-an-artificial-neural-network/26685#26685
  * manhattan distance vs. euclidean distance vs. cosine sim
  * trees and "trees" - https://stats.stackexchange.com/questions/94511/difference-between-bayes-network-neural-network-decision-tree-and-petri-nets/94518#94518
  * growing trees - https://datascience.stackexchange.com/questions/26699/decision-trees-leaf-wise-best-first-and-level-wise-tree-traverse/26950#26950
  * curse of dimensionality - https://stats.stackexchange.com/questions/61390/is-there-unsupervised-regression/65426#65426
  * numerical stability, matrix conditioning and inversion - https://stats.stackexchange.com/questions/88228/how-do-you-calculate-the-ordinary-least-squares-estimated-coefficients-in-a-mult/88229#88229
  * clustering
  * kmeans is spherical, GMM is elipsoid - https://stats.stackexchange.com/questions/80601/why-only-the-mean-value-is-used-in-k-means-clustering-method/80603#80603
  * ranking - https://stats.stackexchange.com/questions/62526/how-to-interpret-the-capped-binomial-deviance-as-rating-model-fit-in-two-player/76878#76878
  * matrices as input-output operators - https://datascience.stackexchange.com/questions/27945/what-is-the-use-of-additional-column-of-1s-in-normal-equation/27946#27946
* data as manifold 
  * separation planes: logistic regression vs SVM - https://stats.stackexchange.com/questions/95340/comparing-svm-and-logistic-regression/95348#95348 
  * consequences of linearity, span - https://stats.stackexchange.com/questions/76488/error-system-is-computationally-singular-when-running-a-glm/76494#76494
  * basis functions - https://datascience.stackexchange.com/questions/26899/are-linear-regression-models-with-non-linear-basis-functions-used-in-practice/26901#26901
  * splines
  * spread - https://stats.stackexchange.com/questions/88348/is-variation-the-same-as-variance/88351#88351
  * sparsity
  * hierarchical manifolds - https://stats.stackexchange.com/questions/63621/what-is-the-difference-between-a-hierarchical-linear-regression-and-an-ordinary/66788#66788
    * LDA - https://stats.stackexchange.com/questions/88206/understanding-latent-dirichlet-allocation-inference/88234#88234
  * class imbalance - https://stats.stackexchange.com/questions/63635/named-entity-recognition-and-class-imbalance/64471#64471
  * statistical bias - https://stats.stackexchange.com/questions/353190/is-it-bad-to-add-bias-to-features/353198#353198
  * bias in RFs - https://stats.stackexchange.com/questions/63776/calibrating-random-forest-regression/63783#63783
  * anomalies
  * nearest neighbor graphs, neighborhood density - https://datascience.stackexchange.com/questions/26781/detect-constant-zero-slope-sections-in-a-noisy-step-function/26804#26804
  * outliers and leverage - https://stats.stackexchange.com/questions/78063/replacing-outliers-with-mean/78064#78064
  * conjugacy - https://stats.stackexchange.com/questions/80085/conditional-distribution-of-a-discrete-random-variable-given-a-continuous-one/80088#80088
  * brownian motion, and the shape of noise - https://stats.stackexchange.com/questions/76263/is-it-possible-that-grid-search-would-fail-in-two-dimensional-feature-space/76264#76264
  * proportions and simplices - https://pages.stat.wisc.edu/~st571-1/04-proportions-4.pdf
* model as manifold, + misc bayesian
  * distributions over distributions - https://stats.stackexchange.com/questions/73268/can-the-t-distribution-be-defined-as-the-distribution-on-the-true-mean-of-a-samp/73273#73273
  * frequentist CIs are confusing
    *  https://stats.stackexchange.com/questions/78795/interpreting-a-confidence-interval/78796#78796
    *  https://stats.stackexchange.com/questions/67782/how-to-compare-two-groups-when-one-only-has-one-data-point/67798#67798
  * change of variables
  * prior beliefs - https://stats.stackexchange.com/questions/77112/how-do-i-correctly-produce-a-prior-posterior-plot-from-mcmc-chains-in-bayesian-h/77122#77122
  * posterior and conditional probability - https://stats.stackexchange.com/questions/76950/posterior-distribution-as-a-distribution-for-a-new-random-variable/76951#76951
  * prior belief as an "anchor" - https://datascience.stackexchange.com/questions/26016/find-optimal-pxy-given-i-have-a-model-that-has-good-performance-when-trained/26136#26136
  * xor - https://datascience.stackexchange.com/questions/29051/is-correlation-needed-when-building-a-model/29061#29061
  * regret minimization - https://stats.stackexchange.com/questions/76401/obtaining-single-connected-component-through-uniform-sampling-in-a-circle/76402#76402
  * secretary problem
  * bayesian probability, probability and continuity - https://stats.stackexchange.com/questions/66315/gentler-approach-to-bayesian-statistics/66377#66377
  * bayesian parameters - https://stats.stackexchange.com/questions/64308/statistical-error-in-bayesian-framework/64310#64310
  * the shape of belief/surprise/confidence - https://stats.stackexchange.com/questions/64852/how-do-i-choose-parameters-for-my-beta-prior/64860#64860
  * the notion of a 'policy' - https://datascience.stackexchange.com/questions/27016/what-is-a-policy-in-machine-learning/27020#27020
  * prediction interval vs confidence interval - https://stats.stackexchange.com/questions/75022/why-do-we-estimate-the-mean-response-in-confidence-interval-but-predict-individu/76085#76085
  * credible interval vs confidence interval
  * reddit ranking - https://stats.stackexchange.com/questions/320858/ranking-k-coins/320860#320860
  * "uninformative" prior - what does "informative" even mean?
    * https://stats.stackexchange.com/questions/73490/what-exactly-is-weakly-informative-prior/73495#73495
  * distributions over solutions = distributions over models - https://stats.stackexchange.com/questions/66500/constructing-confidence-intervals-for-predictive-model/66503#66503
  * bootstrapped CIs - https://stats.stackexchange.com/questions/319030/derivation-of-confidence-and-prediction-intervals-of-predictions-for-probit-and/328777#328777
    * https://stats.stackexchange.com/questions/79937/confidence-limits-for-a-nonlinear-regression/113770#113770 
  * cross validation = validating your procedure - https://stats.stackexchange.com/questions/328717/nested-cross-validation-in-r/328779#328779
  * cross validation and data shape - https://stats.stackexchange.com/questions/320828/svm-cross-validation-parameter-search-returns-constant-accuracies/320850#320850
  * ensembles, boosting, bagging - https://stats.stackexchange.com/questions/77018/is-random-forest-a-boosting-algorithm/77145#77145
  * fitting residuals - https://stats.stackexchange.com/questions/77557/how-are-partial-regression-slopes-calculated-in-multiple-regression/77578#77578
  * conditional probability - https://stats.stackexchange.com/questions/76191/why-do-we-use-conditional-expectation-vs-regular-expectation-in-regression/76193#76193
  * overfitting and degrees of freedom - https://stats.stackexchange.com/questions/78475/does-more-variables-mean-tighter-confidence-intervals/78477#78477
  * double descent
  * model averaging - https://stats.stackexchange.com/questions/65424/how-can-i-validate-a-logistic-regression-model-using-averaged-parameter-estimate/65435#65435
  * model merging a la SD
* embeddings and "features"
  * dense vectors = continuous latent manifolds - https://www.reddit.com/r/aiwars/comments/10cq8wr/on_the_nature_of_sampling_proai_conceptual_art_to/j4hrhtg/?context=3
* sparsity, bottlenecks, and decompositions
  * PCA - https://stats.stackexchange.com/questions/76906/how-can-i-interpret-what-i-get-out-of-pca/76911#76911
    * https://datascience.stackexchange.com/questions/26714/is-pca-considered-a-machine-learning-algorithm/26731#26731
    * orthogonality - https://stats.stackexchange.com/questions/77087/symmetry-of-linear-regression/77111#77111 
    * as a rotation - https://stats.stackexchange.com/questions/66518/interpreting-plot-of-pca-results-from-3-to-2-dimensions/66525#66525
    * variable significance - https://stats.stackexchange.com/questions/65709/negative-binomial-glm-the-most-complex-model-always-has-lowest-aic-all-interac/65717#65717
    * https://stats.stackexchange.com/questions/76483/regression-through-pca/76489#76489
  * fourier
  * taylor series
  * big O and little o notation
* latent space
* autoencoders and denoisers
* weirdness of high dimensions
  * vector components -> rank -> dimensions -> span
  * gaussian annulus, expectations, zero-point energy, and the optimal fighter jet seat configuration
    * https://www.thestar.com/news/insight/2016/01/16/when-us-air-force-discovered-the-flaw-of-averages.html
  * spherical traversals
  * sphere packing paradox
* loss landscapes
  * logistic regression - https://stats.stackexchange.com/questions/66850/prediction-of-a-binary-variable/66854#66854
  * MCMC burn-in https://stats.stackexchange.com/questions/88421/metropolis-algorithm/88422#88422
  * L1 vs L2 regularization https://stats.stackexchange.com/questions/66566/statistically-evaluating-performance-of-algorithms/66577#66577
* regularization and data augmentation
  * https://stats.stackexchange.com/questions/68431/interpretting-lasso-variable-trace-plots/68435#68435
* GAN spaces
* CLIP space
* denoising and diffusion
* composition of representational spaces in LDM
* curse of dimensionality
* saddles, minimia, curvature, flatness
* connectedness of solutions
* power laws and 1-9-90 phenomena
* graph structures, robustness, communication
  * cycles - https://stackoverflow.com/questions/17554805/cycles-in-an-undirected-graph-in-r#63798
  * cliques
  * distributions over graphs - https://stats.stackexchange.com/questions/76401/obtaining-single-connected-component-through-uniform-sampling-in-a-circle/76402#76402
    * 100 prisoners
    * birthday problem
  * small world vs power law
  * force directed layouts
  * pagerank, centrality, random walks, stable distributions, eigendecomposition
    * https://stats.stackexchange.com/questions/88429/markov-chains-2/88754#88754
* iterative systems, chaos, attractors, cycles
* learning dynamics
  * metropolis hastings - https://stats.stackexchange.com/questions/64293/understanding-metropolis-hastings-with-asymmetric-proposal-distribution/64402#64402
  * MCMC and unnormalized distributions - https://stats.stackexchange.com/questions/86909/how-to-generate-random-variables-from-a-defined-density-via-r/86913#86913
  * learning rate magnitude - https://stats.stackexchange.com/questions/87188/optimization-of-the-regularized-least-squares-with-gradient-descent/87196#87196
  * convexity
  * iterated algorithms
  * fixed point solutions
  * training convergence - https://stats.stackexchange.com/questions/66876/how-can-i-assign-a-quality-to-a-regression-based-on-the-number-of-data-points/66881#66881
* double descent
* network capacity / VC dimension
* receptive field of a neuron
* hyperbolic spaces and hierarchical representations
* equivariance
* convolutions and weight sharing - https://datascience.stackexchange.com/questions/26755/cnn-how-does-backpropagation-with-weight-sharing-work-exactly/26761#26761

---

Some additional ideas brainstorming with ChatGPT:

* Receptive field: The receptive field of a neuron in a neural network is the region of the input data that the neuron is sensitive to. It determines what information the neuron is able to "see" and use to make predictions. The geometry and topology of the receptive field can affect the performance of the model.
* Attention mechanisms: Attention mechanisms are techniques used in neural networks to allow the model to "pay attention" to specific parts of the input data when making predictions. They can be thought of as "focus" mechanisms that allow the model to selectively focus on relevant information and ignore irrelevant information. The geometry and topology of the attention mechanisms can affect the interpretability and effectiveness of the model.
* Geometry of optimization: The geometry of the optimization landscape (i.e. the space of all possible model parameters) can affect the performance of optimization algorithms such as gradient descent. For example, the presence of local minima or saddle points can make it difficult for the algorithm to find a good solution. Understanding the geometry of the optimization landscape can help us design better optimization algorithms and improve the performance of machine learning models.
* Topology of solutions: The topology of the space of solutions (i.e. the space of all possible models) can affect the performance and generalization of machine learning algorithms. For example, if the space of solutions is highly connected (i.e. there are many paths between any two solutions), then it may be easier for the algorithm to find a good solution. On the other hand, if the space of solutions is highly fragmented, it may be more difficult for the algorithm to find a good solution.
* Topological data analysis: Topological data analysis (TDA) is a field that uses techniques from topology (the study of the global structure of spaces) to analyze data. TDA can be used to identify patterns and relationships in data that are not easily visible using traditional techniques. The geometry and topology of the data can affect the performance of TDA algorithms and the insights that they can provide.
* Manifold learning: Manifold learning is a set of techniques used to identify and model the underlying structure of data that lies on a low-dimensional manifold embedded in a high-dimensional space. Manifold learning algorithms can be used to visualize and analyze data, and can be particularly useful for tasks such as anomaly detection or clustering. The geometry and topology of the manifold can affect the performance of manifold learning algorithms.
* Differentiable programming: Differentiable programming is a programming paradigm that allows us to define machine learning models using ordinary programming languages and to optimize them using gradient-based optimization algorithms. Differentiable programming allows us to design machine learning models that are more flexible and expressive than traditional models, and to take advantage of the geometry and topology of the optimization landscape to improve the performance of the model.
* Geometric deep learning: Geometric deep learning is a subfield of machine learning that focuses on designing machine learning models that are able to process data with geometric or topological structure, such as graphs or manifolds. These models can be thought of as "shape-aware" models that can learn to recognize patterns in the data that are specific to the shape of the data. The geometry and topology of the data can affect the performance of geometric deep learning models.
* Geometry of generalization: The geometry of the space of solutions (i.e. the space of all possible models) can affect the generalization performance of machine learning algorithms. For example, if the space of solutions is highly connected (i.e. there are many paths between any two solutions), then it may be easier for the algorithm to generalize to new data. On the other hand, if the space of solutions is highly fragmented, it may be more difficult for the algorithm to generalize. Understanding the geometry of the space of solutions can help us design better machine learning algorithms and improve the generalization performance of models.
* Geometry of neural networks: The geometry of neural networks (i.e. the arrangement of the neurons and connections in the network) can affect the performance and generalization of the model. For example, the number and arrangement of layers in the network, the connectivity patterns between neurons, and the type of activation functions used can all affect the geometry of the model and how it processes the data. Understanding the geometry of neural networks can help us design better models and improve their performance.
* Manifold generalization: Manifold generalization is the ability of a machine learning model to generalize to new data that lies on the same manifold as the training data. This can be particularly important when the training data is limited and the model needs to generalize to new examples that are similar to the training data but not identical. The geometry and topology of the manifold can affect the generalization performance of the model, and understanding these properties can help us design better models that are able to generalize well to new data.
* Geometry of generalization error: The geometry of the generalization error (i.e. the difference between the model's performance on the training data and the test data) can provide insights into the underlying structure of the data and the model's ability to generalize. For example, if the generalization error is low for a wide range of model architectures and hyperparameters, this may indicate that the data lies on a simple manifold that is easy for the model to learn. On the other hand, if the generalization error is high for a wide range of model architectures and hyperparameters, this may indicate that the data lies on a more complex manifold that is difficult for the model to learn.
* Manifold regularization: Manifold regularization is a technique used to improve the generalization performance of a machine learning model by constraining the model to lie on a particular manifold. This can be achieved by adding a regularization term to the model's objective function that penalizes deviations from the manifold. Manifold regularization can be particularly useful when the training data is limited and the model needs to generalize to new examples that are similar to the training data but not identical.
* Manifold interpolation: Manifold interpolation is the process of generating new examples that lie on the same manifold as the training data by interpolating between existing examples. This can be useful for tasks such as data augmentation or for generating synthetic data for model training. The geometry and topology of the manifold can affect the performance of manifold interpolation algorithms, and understanding these properties can help us design better algorithms that are able to generate high-quality synthetic data.
* Manifold adversarial networks: Manifold adversarial networks (MANs) are a type of neural network that are designed to learn a compact and meaningful representation of the data that lies on a low-dimensional manifold. They are trained using an adversarial training process, where a generator network generates new examples and a discriminator network tries to distinguish real examples

