# cycle refinement as mode finding (via fixed point iteration/annealing)

labels: publication, experimentation, text2image, text2video

* the text2video trick
* loopback img2img
* experiment: coordinate/gibbs loopback controlnet
  1. generate an image using normal text2image + controlnet, saving the preprocessing images
  2. new run, using only the pre-processing images for conditioning
  3. run the preprocessor on the output, new text 2image run conditioning on that, etc.

or just more broadly: MCMC image refinement, i.e. exploring output neighborhood to anneal into mode
