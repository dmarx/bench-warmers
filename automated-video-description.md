# Automated Video Description for Vision Impaired

![](https://img.shields.io/badge/tag-publicgood-lightgrey)
![](https://img.shields.io/badge/tag-dataset-lightgrey)
![](https://img.shields.io/badge/tag-foundation-lightgrey)
![](https://img.shields.io/badge/tag-accessibility-lightgrey)

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
  
## Misc thoughts
 
the reason I think this is probably different from normal image captioning is:
 
* there are moments that probably don't need to be described. the audio is self-explanatory
* there will be other moments that will need to be described
* there will probably be a tradeoff between a decision to provide a description at a particular moment vs. not wanting to override the audio of the scene. this tradeoff probably also impacts the pace and length of the description
* so in addition to image captioning (really, "scene understanding," but same basic idea), there needs to be some sort of classifier to flag regions of content that merit description, and some sort of budget assignment constraining how long those descriptions can be
 

## Immediate Action Items

* check email or other NTS boards for related ideas
* dig up the name of that non-profit that's all about described video publication
* involve the non-profit (same one?) that certifies people to write/perform video descriptions
  
## Relevant models/research

* https://github.com/YoadTew/zero-shot-video-to-text
* https://github.com/happyharrycn/actionformer_release
* https://github.com/mttr2021/MTTR
* https://github.com/google-research/scenic
* https://roeiherz.github.io/ORViT/
* https://github.com/JerryX1110/awesome-rvos
* https://github.com/microsoft/swinbert
* https://github.com/alibaba-mmai-research/TAdaConv
* https://github.com/MIT-HAN-LAB/temporal-shift-module
* https://paperswithcode.com/task/video-description/latest
* https://github.com/L-YeZhu/Video-Description-via-Dialog-Agents-ECCV2020
* https://arxiv.org/pdf/1802.10250.pdf
* https://netflixproject.wordpress.com/audio-description-on-demand/
* https://github.com/facebookresearch/lavila
 
## Subject Matter Experts

* https://describedvideocanada.com/
* https://www.3playmedia.com/
* https://www.ami.ca/sites/default/files/2019-06/Integrated-Described-Video-Best-Practices.pdf
* https://www.ami.ca/
* https://www.fcc.gov/audio-description
* https://fcc.gov/file/19830/download
* https://adp.acb.org/
* https://dcmp.org/
* http://moviesfortheblind.com/
* http://narrativetv.com/programming.html
* https://adp.acb.org/articles/TheVisualMadeVerbal.html

## Readily available data

* http://audiovault.net/ - audio for described videos (audio only)
* https://eval.ai/web/challenges/challenge-page/1626/overview - EGo4D - Video action classification dataset
* https://kgavrilyuk.github.io/publication/actor_action/ - A2D-sentences: Actor and action video segmentation from a sentence + J-HMDB extended annotations
* https://msropendata.com/datasets/ab980403-283f-47e4-9371-a84718ee6609 - MSRVD - Microsoft Research Video Description Corpus
* https://youtube-vos.org/dataset/rvos/ - Youtube-RVOS - Referring Video Object Segmentation 
 
## TO DO:

- [ ] Lit review
  - [x] relevant models
  - [ ] relevant published datasets
  - [ ] relevant potential datasets
- [x] Identify candidate partners in the accessibility community
  - [ ] Explore relevant non-english presence in this space
        - Maybe a separate project could be automated translation of described videos? - https://adp.acb.org/international.html
- [ ] rough model blue print
  - [ ] draft target function (problem specification)
  - [ ] draft architecture + optimization scheme
  - [ ] estimated minimum cardinality of dataset 
  - [ ] rough estimate of FLOP cost
- [ ] flesh out proposal (see above)
