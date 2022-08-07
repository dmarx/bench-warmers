# Grimoire: Prompting Toolbox

Set of tools to facilitate prompt design for AI art

## Feature brainstorming

* image manager that associates prompt components with images
* simple data mining tools (e.g. n-grams) for extracting commonly used prompt components
* NLPaugs for constructing variations on prompts
* image captioning tools for identifying prompts associated with one or more images
* mechanisms for organizing, categorizing and composing prompt components and templates
* database of useful prompt chunks (e.g. artist names, materials, templates, vitamins for inducing realism or styles, etc.)
* EDA visualizations for examining embedding space topology, clustering, and distributional features of prompts (inliers, outliers, aethetic scores, etc)
  * https://clip-as-service.jina.ai/playground/embedding/

## UX Brainstorming

* Anticipate that primary users will be non-coder artists and colab users
* Will need to ship with some sort of simple front-end (i.e. a notebook)
* Design for use with notebooks, perhaps include a notebook of pre-designed colab forms or compatible widgets
