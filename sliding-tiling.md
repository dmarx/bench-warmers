# Sliding Tiling

use the temporalnet tiling trick, hold on to last three frames, keep frozen as inpainting condition on next 6 tiles (so 3x3 grid, where the left wall of the grid is fixed). then slide it so there's only one wall left, freeze that, rinse and repeat for butter smooth.

oh yeah, within each cluster, run a tsp sort with the last frame fixed.

oh shit, tiled dreaming! don't even need an init video for this, can do this all from pure noise.

oh shit, klmc2 with tiling?

or even just normal img2img with tiling

* latent input
* multiplex latents into KxK grid, default K=3
* diffusion generation img2img over the grid as a single image
* demultiplex into K\*K images (b h c w K\*K)
* tsp sort, first imgage fixed (or maybe first three images?)
* persist first 6 as frames, shift remaining three to other side of grid
* iterate, multiplexing into (K-1)^2 grid
