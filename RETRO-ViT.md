# RETRO-ViT
[WIP] Hey why not? It worked for text. Let's make retrieval for auto-regressive image generation a thing.

for the database, let's use CLIP embeddings for the image keys, and VQGAN tokens for the values. So for a given input text, we e.g. query laion for a handful of images with nearby CLIP embeddings, encode them into the VQGAN latent, and ... that's a lot of data... something something profit. 

Very half baked idea here, obviously, but you get the idea. maybe the retrieval database is just literally image patches? err... that's inviting copyright issues... hmm...

Here's a thought. If we have a codebook of size 8192 and a VQGAN latent of 16x16, that's only 2,097,152 possible configurations. What if we just precomputed all of them? Oh duh, it's 8192 ** (16*16). 

I should just come back to this later.

Maybe the "tokenizer" could be just passing an image patch through a linear projection? I should check how ViT does it.

...yeah totally, my original idea was solid. oh shit, we could just do a KNN lookup for image generation with a VQGAN. Pull back the K-nearest-neighbors by CLIP embedding and perform a pooling/reduction operation of some kind over the corresponding vq embeddings to get a single set of vq embeddings to decode. could start with a naive ...

oh shit, could we persist a neural compression of LAION? ...wait, why isn't neural compression more of a thing? I guess it'd be pretty lossy, but it'd be great for datasets.
