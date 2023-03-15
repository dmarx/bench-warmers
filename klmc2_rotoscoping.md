# klmc2 rotoscoping

![](https://img.shields.io/badge/tag-animation-lightgrey)
![](https://img.shields.io/badge/tag-tooling-lightgrey)

q: can we construct a mapping between the respective hessians in RGB space and VAE space? maybe we can estimate the VAE hessian from the RGB optical flow field?

1. generate KLMC2 animations at different parameterizations (maybe scheduling parameter changes like in the consistency net thing?)
2. serialize the hessians used to generate the animation
3. estimate flow fields/RGB hessians from the final animation
4. fit a model on the flow fields/rgb hessians that predicts the VAE hessian

---

simpler solution: KLMC2 + controlnet

---

KLMC2 dreaming plus conditioning gradient on flow field transferred from an input video

~~POC with this for flow: https://www.youtube.com/watch?v=dx7whkxw1B0~~
-- no idea why i had this video in mind...
