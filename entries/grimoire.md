# Grimoire: Prompting Toolbox

![](https://img.shields.io/badge/tag-prompting-lightgrey)
![](https://img.shields.io/badge/tag-tooling-lightgrey)

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
  * https://rom1504.github.io/clip-retrieval/

## UX Brainstorming

* Anticipate that primary users will be non-coder artists and colab users
* Will need to ship with some sort of simple front-end (i.e. a notebook)
* Design for use with notebooks, perhaps include a notebook of pre-designed colab forms or compatible widgets

Some tinkering with the simulacrabot dataset: https://colab.research.google.com/drive/1DDGxDIEuxFCJskP2Mo1DN0wNHqS-QCD7#scrollTo=gOO8cXtr47MY
