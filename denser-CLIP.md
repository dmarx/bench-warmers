# Denser CLIP representations

![](https://img.shields.io/badge/tag-wip-lightgrey)  
![](https://img.shields.io/badge/tag-tooling-lightgrey)  
![](https://img.shields.io/badge/tag-experimental-lightgrey)


Max Woolf has some shallow resuls suggesting that we might have more powerful CLIP representations
by incorporating the activations from additional penultimate layers: https://github.com/minimaxir/imgbeddings/blob/main/DESIGN.md

I think this merits looking into. really wouldn't be that hard, basically just need to add this representational strategy to a CLIP evaluation harness.
