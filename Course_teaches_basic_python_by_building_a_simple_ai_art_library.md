# Course teaches ~~intermediate python~~ generative art topics by building a simple ai art library

labels: from_issue, curriculum, education, publication

i think this might need content to get transferred over?

[Link to original issue](https://github.com/dmarx/bench-warmers/issues/34)

---

# Assignments/curriculum

* Tools of the trade
  * image utilities 
    * PILlow
    * ffmpeg
    * cv2
  * DL utilities
    * pytorch
    * einops
  * prototyping utilities
    * colab
    * gradio
    * panel/voila
    * fastapi
    * a1111
* SGD for hackers
  * incremental updates
  * gradient flow (backprop)
  * gradient accumulation
  * gradient checkpointing
  * Adam, momentum
* intro to latents
  * pretty much only linear algebra we need: `<m x n> * <n x k> = <m x k>`
  * vectors are directions, not coordinates
  * simple small vocab basis with bag of words
  * cosine similarity
  * matrix factorization -> topic modeling
* autoencoders, shared latents
  * simple image compression
  * old school deepfake
  * intro to CLIP space
    * shared multimodal latent manifold, distinct text vs. image regions (revisit this with CLIP-DIP, unCLIP-DIP)
    * semantic search (image retrieval) with CLIP
* SGD - deepdream, PEZ, clip interrogator
* classifier-guided t2i - CLIP-RGB
* differentiable image parameterization - CLIP-DIP

* two-phase modeling with autoencoders - CLIP-VQGAN
* denoising autoencoders, diffusion schedules, CFG - SD t2i, cold diffusion (blurring diffusion, heat dissipation... something non-gaussian)
  * reversing corruption processes - cold diffusion, etc.
  * denoising image vs denoising latent
  * in-painting, prompt-to-prompt
* animation
  * composition from motion - VQGAN i2i, 2D transforms
  * color correction, new vae - SD i2i 2D
  * depth estimation, optical flow, 3d transforms - SD i2i 3D
  * basic ffmpeg
* finetuning - dreambooth, TI
* advanced topics
  * multi-prompting
  * controlnet
  * lora
  * region prompting
  * KLMC2
  * AnimateDiff
* bonus topics
  * stylegan
  * style transfer
  * token merging
  * NeRF
  * text-to-3d
  * audio-reactivity
    * this could basically be a whole separate course/book


Discuss the history as we go
 
# Title ideas

* AI Internals - actually, maybe make this a youtube channel +socials/discord
* AI Art Technical Masterclass: Under-the-hood of Generative AI Tools
* AI Mastercraft
* Intro to Latents
