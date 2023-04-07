# Predictive Safety for First Responders

![](https://img.shields.io/badge/tag-publicgood-lightgrey)  
![](https://img.shields.io/badge/tag-dataset-lightgrey)  
![](https://img.shields.io/badge/tag-completed-lightgrey)  
![](https://img.shields.io/badge/tag-publication-lightgrey)  
![](https://img.shields.io/badge/tag-3hi5this-darkgreen)  
![](https://img.shields.io/badge/tag-wip-lightgrey)


## 2022-09-29 - 1

rather than audio recordings, just use transcripts. duh. transcripts almost certainly exist. and if they don't, they should. especially now that whisper's free, there's basically no excuse not to. really easy public service we could do: consume livestreams of piblicly broadcast first responder incident operations radio broadcasts, convert to text. can further augment dataset with LoDD reports, etc.

----------

## 2022-09-29 - 0

train a causal perceiverIO on NFIRS/NFPA incident reports paired with radio audio, headcam video

given progress-indicating signals of a fire incident in the field (radio comm recordings, external footage, headcams), predict if it's likely to go sour

at the very least: could be a way of automating away a lot of burdensome documentation.

reducing documentation burden for first responders is by itself a tackleable problem...
