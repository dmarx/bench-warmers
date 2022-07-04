# single video sparse quantized auto-encoder

`2022-06-29`

inspired by: https://www.cs.cmu.edu/~aayushb/Video-ViSA/

to accelerate learning, we can leverage a pre-trained VQGAN. 
1. project all frames of the video into the latent of a pre-trained vqgan, accounting for all codebook tokens used in the latent representation
2. define a new sparse codebook by constraining attention to only those tokens that were previously used to represent frames in the video.
3. game set match? can we use this representation for efficient interpolation?
