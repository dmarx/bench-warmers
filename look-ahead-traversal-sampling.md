# look-ahead traversal sampling

![](https://img.shields.io/badge/tag-animation-lightgrey)  
![](https://img.shields.io/badge/tag-image_generation-lightgrey)  
![](https://img.shields.io/badge/tag-control-lightgrey)  
![](https://img.shields.io/badge/tag-experimental-lightgrey)  
![](https://img.shields.io/badge/tag-MCMC-lightgrey)



---

could turn this into a kind of naive MCMC (i.e., klmc2-esque). parameterize by the noise level/image guidance, number of candidates per iter.

if can make this "feel" like KLMC2, then can add in deforum-esque animation controls and image2image smoothly af

---


here's how we can apply 'optimal odering' smoothing to image2image

1. for a frame at time=t, sample k variations
2. same thign for t+1
3. use traveling salesman to find shortest path through t and t+1
- NB: this isn't even a traveling salesman thing anymore, this is just a simple nearest neighbors check.
4. hold on to t, use it to sample new/addl t+1 candidates.
6. rinse and repeat, incrementing t

goal here is to sample in the neighborhood of the serial animation we'd otherwise generate,
exploring the available local degrees of freedom to potentially find a nearby image that gives a smoother animation
