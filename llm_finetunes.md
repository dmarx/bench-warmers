# master document for LLM Finetune ideas

labels: training, experimentaiton

feel like maybe I'll be more inspired here if I put the ideas in one place. 

I also like that PR/FAQ thing I saw the other day where someone was writing reviews for SD finetunes they hadn't yet trained or something like that.

anyway, I was inspired to make this now for the following idea:

* document-to-mindmap
  * summarize a document into a graphical summary saved as a text file. graphical summary document GSD.
  * needs to be parameterizable as a text format so we can just use an LLM to generate these.
  * construct a procedure for growing this representation that pushes in "missing" notes 

--

# Sources for codegen finetuning data

## Python

* Django
* FastAPI
* huggingface/transformers
* huggingface/diffusers
* numpy
* scipy
* pandas
* sklearn
* pytorch
* pytorch-lightning

## Go

* Gin
* terraform

## k8s

* kubernetes
* knative
* prometheus
* etcd
* helm
* argoCD
* docker
* singularity
* slurm

# Creative writing (planning) assistant

* TVTropes
* worldbuilding.stackexchange
* subreddits? There must be loads of subreddits that would be good here.
  * /r/askhistorians
* Some sort of public crowd-sourced CliffsNotes? That has to be a thing, right?
* Generated brainstorming dialogues
  * Real Event -> summary -> elevator pitch -> hallucination -> TVTropes -> characters -> TVTropes -> story arcs
    * https://chat.openai.com/c/7c6efd5e-231f-4a3e-9527-0b0f15c387b1
  * elevator pitch from invested perspective
    * https://chat.openai.com/c/4b0cc047-edb2-4857-b833-2eb21a3f1f39
    * https://chat.openai.com/c/9ab138ff-acfc-4614-989c-70145f44fb34
  * topic -> context -> context from alternative perspectives -> guide towards target perspective -> adjacent topics -> Synthesize -> TOC -> coarse-to-fine
    * https://chat.openai.com/c/310b31ac-7245-4e84-8393-5cddd187fcdb
  * foreach
    * https://chat.openai.com/c/a33581f7-cddc-4e78-9e53-aac5b0c9f4c3
  * topic -> isolate piece of response -> "elaborate" -> ...
    * https://chat.openai.com/c/7b75c12a-b0d5-4691-b227-a3f87e487d89
