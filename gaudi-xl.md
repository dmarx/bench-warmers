# GAUDI-XL

i've been thinking about decoupling pose and scene for a while, this is basically a demonstration of that idea. 

fit a separate model as a prior over the (scene) latent. maybe an adaptor layer/module/network over a frozen TTI mode like stable diffusion 
or maybe even CLIP. I bet noised CLIP could work. simple way to regularize over the semantic content of a whole scene? that might be a 
separate idea to explore.
