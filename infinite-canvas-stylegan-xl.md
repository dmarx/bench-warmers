# infinite canvas stylegan-xl

the translation invariance property of the stylegan3/xl latent makes it so you can explore "out of bounds", 
but there's still clearly a "central region" that the model prefers to operate within. This seems to manifest
as frame/border artifacts. I suspect the positional component of the latent could be reparameterized similar to 
ALiBi, which I think would fix a chunk of this.

to further permit this, we could fit a perceptual loss between the central region of the latent and random samples from elsewhere in the latent canvas,
the motvation here being that exploring randomly should still give you something that looks similar to where you started.
