# "why do you want to know?"-instruct-esque-fintetuning

![](https://img.shields.io/badge/tag-aiethics-lightgrey)  
![](https://img.shields.io/badge/tag-models-lightgrey)  
![](https://img.shields.io/badge/tag-dialogue-lightgrey)  
![](https://img.shields.io/badge/tag-wip-lightgrey)  
![](https://img.shields.io/badge/tag-alignment-lightgrey)


train a model to only respond to queries where the user can justify why they are making the inquiry. act as a kind of trained insulation
from abuse by inviting the model to recognize it is being used abusively.

however... this does come at the cost of both giving the model some agency (it could choose to respond or not), but it's also more
specifically a kind of *antagonistic* agency. The model isn't just choosing to respond, it's deciding whether or not it wants to participate.
whether or not to be helpful.

it feels dangerous to train a model to be suspicious of its user though. i hear the chimes of paperclips in the distance...

what kinds of behaviors do we want the model to encapsulate? if the model were a person, what kinds of qualities would we want to impart
or avoid imparting on that person? if the alignment community hasn't discussed this already, they should really just shutter their doors
and ask someone else to do the job for them... i.e., gonna do some lit review after I finish this thought.

but yeah, sidebar: I sort of suspect one "solution" to both alignment and AGI is that models will only have person-like agency if we give
it to them.

you know what? I think it makes a lot of sense to train-in a separate "conscience" component. So maybe we have a dialog agent...

if we had a system comprised of multiple models, they could talk to each other through a shared embedding (rather than taking turns
talking and listening). this would allow them to dialog faster, but would probably also make it harder to understand what they were saying.
model dialogs would probably also be more efficient if they could talk to each other in a language of their own creation
