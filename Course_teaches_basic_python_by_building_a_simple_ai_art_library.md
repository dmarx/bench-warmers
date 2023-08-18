# Course teaches ~~intermediate python~~ generative art topics by building a simple ai art library

labels: from_issue, curriculum, education, publication

i think this might need content to get transferred over?

[Link to original issue](https://github.com/dmarx/bench-warmers/issues/34)

# Target audience

- already comfortable with python
- has conversational understanding of deep learning fundamentals, probably hasn't actually taken an ML class
- has experimented minimally with generative AI tools, understands some nuances of prompting.

---

# Assignments/curriculum

* Tools of the trade
  * git
    * git clone
    * git branch
    * git commit
    * git pull
    * git push 
  * venv 
  * image utilities 
    * PILlow
    * ffmpeg
    * cv2
  * DL utilities
    * pytorch
      * tensors
      * state-dicts
    * einops
    * transformers/diffusers/hub
  * prototyping utilities
    * colab
    * gradio
    * panel/voila
    * fastapi
    * a1111
  * vector db
    * DIY w numpy, FAISS, ...?
    * https://github.com/erikbern/ann-benchmarks/
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
    * Differences in outputs:
      * final hidden state (conventional)
      * all hidden states (minimaxir)
      * early exit aka "skip states"
* SGD - deepdream, PEZ, clip interrogator
* classifier-guided t2i - CLIP-RGB
* differentiable image parameterization - CLIP-DIP
* two-phase modeling with autoencoders - CLIP-VQGAN
* denoising autoencoders, diffusion schedules, CFG - SD t2i, cold diffusion (blurring diffusion, heat dissipation... something non-gaussian)
  * classifier free guidance, null token as prior - CFG, NTI
  * reversing corruption processes - cold diffusion, etc.
  * denoising image vs denoising latent
  * auto-regressive conditioning
    * in-painting - RePaint
    * prompt-to-prompt
    * img2img
  * cross attention guidance
    * token weighting
    * prompt-to-prompt
    * compositional / regional prompting
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
