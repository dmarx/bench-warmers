# Split LoRA: hiding a third LoRA in the weights of two other LoRAs

labels: safety, experimental

let UV be a LoRAs matrices. given a LoRA 'A', its matrices are Ua Va.

Utilize a single training running to fit three LoRAs in parallel, X and Y, with matrices Ux Vx and Uy Vy respectively, and Z. The Z LoRA is given by Ux Vy.
if B is a batch, a given batch should K images for each LoRA. The loss can just be the sum of the three respective LoRA's losses.
