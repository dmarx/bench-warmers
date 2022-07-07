# Automated Video Description for Vision Impaired

## Goals

* assembling the dataset is by itself an opportunity to improve access to existing content
* 'described videos' for the blind are in short supply
* make it so easy for industry to add the feature from models we train 
that it would be offensive of them not to

## Milestones

- near term: help the sight impaired community with larger repertoire of entertainment
- long term: train a model to automate making these descriptions, making it trivial for studios to add this feature
- longer term: make it trivial for people to make their own descriptions to go with videos
- longer term: assistive devices that describe someones surroundings in real time in natural language


## broad development plan

* starting place: scene understanding model
  * active area of research, probably decent pre-trained models we can build off of to prototype the idea

* separate model classifies video segments as meriting description or not
  * talk to <certification agency for people who describe videos> for SME support
  * ? is there something happening
  * ? has it changed from what was already happening
  * ? are there audio cues meriting description
  * ? are there audio cues that 'speak for themselves'
  * ? would a new description starting at t time collide with an ongoing descritption in progress
  * might need to fit this iteratively, gnash equilibrium between description content density and length
  
## Immediate Action Items

* check email or other NTS boards for related ideas
* dig up the name of that non-profit that's all about described video publication
* involve the non-profit (same one?) that certifies people to write/perform video descriptions
  
## Relevant research/code

* https://github.com/happyharrycn/actionformer_release
* https://github.com/mttr2021/MTTR
* https://github.com/google-research/scenic
* https://roeiherz.github.io/ORViT/
* https://github.com/JerryX1110/awesome-rvos
* https://github.com/microsoft/swinbert
 
## TO DO:

- [ ] Research existing/relevant datasets
- [ ] Lit review
  - [ ] relevant models
  - [ ] relevant published datasets
  - [ ] relevant potential datasets
- [ ] rough model blue print
  - [ ] draft target function (problem specification)
  - [ ] draft architecture + optimization scheme
  - [ ] estimated minimum cardinality of dataset 
  - [ ] rough estimate of FLOP cost
- [ ] flesh out proposal (see above)
