# Palette of Priors

this is an older idea i've been kicking around, but i think it actually makes a lot more sense in the LoRA world than it did in the DreamBooth world

so here's a full experiment:

1. cluster LAION (peter did this already)
2. fit a LoRA for sd 1.5 on each cluster
3. take the PCA of the LoRAs
4. Fit a LoRA in the PCA basis

the original idea was to do this as a checkpoints and a full model merge, but this is way cleaner. could also expand the space a little via GLoRA, but that's a whole can of worms.
