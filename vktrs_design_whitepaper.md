# (draft) vktrs design whitepaper

labels: publication

# title brainstorming
* "Mining for music
* Parameterizing coherent, complex, multipart animations

# ToC

* Notebook Design
  *  workspace
    * config.yaml: resume functionality
    * shared_assets/: reuse of processed artifacts
* Storyboard
  * hierarchical overrides
  * human readable = human editable
  * offloading state to disk to facilitate resuming
    * reload and save with each cell/change
  * Add complexity incrementally, layer by layer
  * thinking in tables - registering signals for reuse
  * isolated eval context for restricted DSL
* Scene Segmentation heuristics
  * too short > too long
  * ASR = simple auto-edit baseline
  * outlier detection for long scenes
* Coherence tricks
  * theme prompting
  * prompt lag
  * thematic structure analysis
* Audioreactivity Tooling
  * A DSL for signal processing
  * lessons from parsec: interactive UX >> sequential cells and scrolling
* Designing for keyframes
  * lessons from Chigozie/Disco/Deforum
* Animation tricks
  * variations animation
  * TSP sorting
  * specifying frames with ffmpeg
  * upsampling to facilitate social sharing

