# camera motion diffusion: few-shot finetuning using semantic checkpoint merging

use semantic algebra (king - man + woman = queen) to learn a camera-motion diffusion model via the following procedure:

1. fine tune a "Sintel Diffusion" model to capture the look of the film
2. From this checkpoint, train a next-frame prediction model trained on Sintel, conditioned on text descriptions of camera motion
3a. cross fingers, throw salt over shoulder, spin around three times
3b. subtract the first checkpoint from the second. the hope here is to marginalize out Sintel-specific effects to give us a generic next-frame diffusion model that conditions on natural language descirptions of camera motion.

This almost certainly won't work for any number of reasons. but it'd be pretty cool if it worked!
