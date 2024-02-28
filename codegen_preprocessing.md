# Dataset preprocessing for code-gen finetuning

labels: nlp, experimental

## Metadata header

Concatenate file metadata as a header (comment?) to each file.

Potential information to include:

* project root URL
* article title
* article abstract
* full project file tree
* list of functions/objects/variables defined in the file

## Modified versions of code

* standardized formatting
  * python: `black`
* version of code with all comments and doc strings stripped
* version of code with additional comments/docstrings/typehints completed by LLM (ChatGPT)
