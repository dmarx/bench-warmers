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
  * inspiration -> tropes -> elevator pitch -> who/what/where/when/why/how -> criticize proposal as "facile" -> add complexity to characters motivations -> adjust theme
    * https://chat.openai.com/c/80fdd117-9eb5-40ba-a099-1741d6c1326a  
  * elevator pitch from invested perspective
    * https://chat.openai.com/c/4b0cc047-edb2-4857-b833-2eb21a3f1f39
    * https://chat.openai.com/c/9ab138ff-acfc-4614-989c-70145f44fb34
  * topic -> context -> context from alternative perspectives -> guide towards target perspective -> adjacent topics -> Synthesize -> TOC -> coarse-to-fine
    * https://chat.openai.com/c/310b31ac-7245-4e84-8393-5cddd187fcdb
    * https://chat.openai.com/c/c968e7e8-eae9-422f-bdea-bd4346883460
  * foreach
    * https://chat.openai.com/c/a33581f7-cddc-4e78-9e53-aac5b0c9f4c3
  * more
    * https://chat.openai.com/c/c4b23052-1771-4271-acea-8a59f7b2cecd  
  * topic -> isolate piece of response -> "elaborate" -> ...
    * https://chat.openai.com/c/7b75c12a-b0d5-4691-b227-a3f87e487d89
  * pseudocode
    * https://chat.openai.com/c/ce27f69e-ea9e-459b-831a-ac95d72198a0
    * https://chat.openai.com/c/664d7333-89fe-4bdf-91e0-8d4b8696d654
  * user stories and action items
    * https://chat.openai.com/c/c968e7e8-eae9-422f-bdea-bd4346883460
  * collaborative brainstorming
    * https://chat.openai.com/c/b5c20579-f574-43d0-b31a-6e0b9ce0a3fc
    * https://chat.openai.com/c/deec108c-f45f-46a7-bdcd-3ff3a2b4e444
    * https://chat.openai.com/c/a416562c-acbf-42f3-afe8-58f8236cd06a
    * https://chat.openai.com/c/b925108b-e11f-4f0d-9d6c-82e88347102c
    * https://chat.openai.com/c/2dbb6562-9655-464e-b464-410f27ebd49f
  * adding notes/comments/type-hints/documentation in-line
    * https://chat.openai.com/c/77db5296-a7bc-4c6b-b2f1-b7df89321652
  * PR/FAQ -> user stories -> test suite -> README/core features tutorial -> skeleton codebase -> prioritize development plan -> pros/cons -> flesh out -> reassess plan -> reassess target userbase -> assess competition and differentiators
    * https://chat.openai.com/c/95d3ba5b-f5de-4eb4-8f31-28bd376e3daa
  * "tell me about ___" -> "> ... \n elaborate"
    * https://chat.openai.com/c/a2db9a7d-b554-448e-bc72-edb4c27c3cd7
  * corase-to-fine outline -> please expand on ....
    * https://chat.openai.com/c/40ad3f27-89f4-40ad-b0d1-7d30b4ea5685
  * debate between opposing viewpoints
    * https://chat.openai.com/c/933606f8-fc64-456d-80d3-e306c7b09b96

# Finetune an adapter to interpret specialized context signals

e.g. could recursively utilize a coarse-to-fine strategy to develop multi-resolution outline structures, and use different focused sections of outline as context signal provided to an adaptor module.

this is probably overkill and in-context learning probably accomplishes most of what I want here. but yeah, could finetune a LoRA or something.


# hierarchical document structure

with each chunk and level of depth of a document, associate with it a "scratchpad". this can be a single file, or multiple files. should represent considerata relevant to that "local" context. represent doucment as a nested file tree. each level of the tree contains a "content" directory for the actual content, and a "scratch" directory for context documents. as content gets authored, scratch content in adjacent directories can be updated.

document can be accompanied by a log (git log?) documenting change history, and each scratch space can be accompanied by its own respective "to do" list of action items for work that needs to be developed locally, content to be developed, etc.

# auto-wiki

"you are generating content for ___ textbook in the form of wiki articles. highlight topics and phrases that merit their own articles as hyperlinks, using the following markup syntax: <content>this is an [[inline link]] to another [[article]]</content>. the current article is on the topic: '{article topic}. Begin.<content>"

spider to push out more content
