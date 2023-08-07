# video edit model + klmc2 + cold-diffusion = text2video

![](https://img.shields.io/badge/tag-publicgood-lightgrey)  
![](https://img.shields.io/badge/tag-wip-84f8cf)  
![](https://img.shields.io/badge/tag-animation-lightgrey)  
![](https://img.shields.io/badge/tag-prompting-84f8cf)  
![](https://img.shields.io/badge/tag-tooling-lightgrey)  
![](https://img.shields.io/badge/tag-meta-lightgrey)  
![](https://img.shields.io/badge/tag-stability-lightgrey)


use klmc2 to generate a background (but in-domain) "noise" to pass to a video *editing* model, then repeatedly run editing passes to "decorrupt" the video, a la cold diffusion

re-sampling: we're gonna be re-running the video edit model. should we apply that sequentially down the entire video clip in a single pass and then repeat complete passes?
or should we "denoise" smaller segments first? maybe backtrack a chunk after each pass, following a diffusion sampling schedule. so like first pass is 100% of video, and each subsequent pass gets a "noise-level" worth of the video forward.
this way, we only fully resolve the first frame, and we have a minimal context of that frame encoded in the output, so the last frame will be conditional on the first.
but we also have a much higher degree of freedom to generate the earlier frames

-----------------

controlnet + video
