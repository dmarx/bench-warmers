# warp klmc2.md

![](https://img.shields.io/badge/tag-wip-lightgrey)  
![](https://img.shields.io/badge/tag-tooling-lightgrey)  
![](https://img.shields.io/badge/tag-animation-lightgrey)


just add an optical flow loss.

shit, I should add classifier guidance too. and a clip prior.

i should probably just make these issues on the repo.

i'm hungry, but it's 2am. I wanna snack, but I feel like I should be making some kind of effort to sleep.

anyway: flow loss on klmc2, then use klmc2 with init image for vktrs, using init images from the input video OMG I should make that a feature.

similarly, vktrs could also detect scene changes (!!!) from the input video, then borrow the timing.

---

yo rotoscoping idea: just latent blend the init video in a little (instead of going full on, newly re-encoded, post-transform init image)
