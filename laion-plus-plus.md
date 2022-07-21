# LAION++ Enriched Dataset

use pre-trained models to automate adding a ton of additional labels to laion aesthetic and/or 400m
- semantic segmentation
- instance segmentation and classification
- depth
- imagenet class
- common and/or multilingual text embeddings
  - https://github.com/facebookresearch/LASER
- common image embeddings (how big are the pre-computed CLIP embeddings?)

be sure to version dataset within its name, so maybe LAIONpp_2022v1 or something like that.
- anticipate that we would update low confidence labels and/or apply better estimation models in the future

# To Do
* chose a handful of enrichments to start with
  * pick some models
  * benchmark models for latency/batch rough estimation
* form an estimate of how much compute/time this would require to run. probably not much.
* estimate data requirement. this will be non trivial. maybe coordinate with TheEye for hosting?
