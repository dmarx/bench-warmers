# animating on autopilot

publish something jointly w disco + deforum folks as a survey of techniques and lessons learned from building the tools around them.

ok so far those are actually thoughts for like... a completely different paper. really i meant more like,

* euler angles vs. quaternions
* DSLs
  * pytti
  * disco/deforum
  * a1111
  * <that paper where they used fonts and colors and stuff in the prompt>
  * prompt weighting, parameter curving
* assorted tricks of the trade
  * prompting the "uncond" with a non-null token = prior prompting
  * zippy's turbo trick: coherence via novelty cadence (aka skip steps)
  * clip guidance
  * fuzzing mask edges for inpainting
  * LAB, HSV, color correction, MSE-VAE
  * forward-backward optical flow, depth warping
  * prompt lag
  
* audioreactivity
  * magnitude of some energy within the song -> dreaming procedure intensity
    * noise, strength
  * less is more
  * keyframes
  

* emergent phenomena
  * composition from motion
    * zoom w rapid accel/decel to change scene then stabilize, like shaking an etch a sketch
  * dreamed paintings on a canvas within the image
  * 

* effective development for generative art community
  * library vs notebook
  * dealing with git clone dependencies (napm cameo), PATH modifications
  * virtual environments, containerization, layperson-friendly setup (a1111 cameo)
* effective notebook development
  * emojis
  * toc nested semantically -> e.g. different levels of depth correspond to savepoints
* open source
  * open source collaboration  
  * what it means for a feature to be "ready" in open source
  * open source development particularly well suited for unicorn skillset -> simultaneous user research and development
    * figuring out how to do audioreactivity -> breaking down process into steps -> encapsulating steps in operations -> trying to add audioreactivity to different inputs, yielding new operations to encapsulate -> refine operators, parameterizations, combining redundancies -> usability of overall flow...
