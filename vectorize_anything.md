# Seed differentiable vectorization with paths inferred from semantic segmentation

labels: experimentation, tooling, segmentation, svg

given a raster image, apply semantic segmentation and fit svg paths to the learned masks. Use these paths to initialize a differentiable image vectorization. could even parallelize across path-bounded regions and fit a vectorization to each independently, thereby producing semantically meaningful path objects and layers. furthering this idea, could apply this procedure recursively, initializing the sub-vecotirzation process with more granular segmentations, etc.

### relevant projects

* https://github.com/CASIA-IVA-Lab/FastSAM
* https://github.com/BachiLi/diffvg
* https://github.com/Picsart-AI-Research/LIVE-Layerwise-Image-Vectorization
* https://arxiv.org/abs/2211.11319 / https://ajayj.com/vectorfusion
