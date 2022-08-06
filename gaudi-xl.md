# GAUDI-XL

i've been thinking about decoupling pose and scene for a while, this is basically a demonstration of that idea. 

fit a separate model as a prior over the (scene) latent. maybe an adaptor layer/module/network over a frozen TTI mode like stable diffusion 
or maybe even CLIP. I bet noised CLIP could work. simple way to regularize over the semantic content of a whole scene? that might be a 
separate idea to explore.


https://github.com/apple/ml-gaudi

throw some of these in the pot too, baby we got a stew goin!

* Fast rendering/training
  * https://github.com/NVlabs/instant-ngp
  * https://nv-tlabs.github.io/nglod/
  * https://arxiv.org/pdf/2107.02791.pdf
* few-input learning
  * https://github.com/hbb1/PREF
  * https://github.com/cwchenwang/NeRF-SR
* efficient nerf
  * https://nvlabs.github.io/eg3d/
