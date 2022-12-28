# Learned conditional semantic controls

![](https://img.shields.io/badge/tag-animation-lightgrey)
![](https://img.shields.io/badge/tag-prompting-lightgrey)
![](https://img.shields.io/badge/tag-colab-lightgrey)
![](https://img.shields.io/badge/tag-tooling-lightgrey)
![](https://img.shields.io/badge/tag-experimental-lightgrey)

1. use something like KLMC2 with a weak conditioning weight to draw samples in the neighborhood of a prompt
2. collect the latents from this sampling process and learn a reduced rank representation over the latents (e.g. PCA)
3. the rank-reduced representation should provide a semantic basis whose directions are specifically relevant to the conditioning prompt and feasible outputs
