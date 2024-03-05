# Predict learning trajectories conditioned on model embeddings

labels: experimental, contrastive_learning, llm, code_gen, public_good, open_source, open_ai

* ContrastiveLoss(TEXT(model_config), TEXT(model_code)) -> ModelEmbedding space
* wandb dataset: conditioning on ModelEmbedding and some text representation of the early training history, predict the training history out to some horizon into the future

pilot study:

* some trivial model family paired with a problem we can train quickly and easily, like MNIST
  * generate configs representing a hyperparameter sweep
  * wait... wandb has a sweep feature built in, right? let's just use that.
  * generate some dense region of hyperparameter space to train on
  * goal: does this strategy at least work for a trivial problem?
  * if yes, use some more sophisticated models and see what happens
  * use (LoRA? on) a 7B codegen base model to parameterize the contrastively-learned ModelEmbedding space
