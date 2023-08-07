# insta-edit

1. start with editing down a video based on ASR.
2. use generative models to make the sharp cuts seem more natural
   * adjust the audio first. this may involve changing the time domain.
     * simple version: fit a model to the speaker's voice, mask the domain of the cut, use text-to-speech diffusion to infill. i think there are even face conditioned models
   * use frame interpolation to visually smooth over the edit 
