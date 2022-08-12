let's assume that commas and pipes are the only separators we need to worry about rn.

1. Apply NER to separately classify:
  * artists names
    - van gogh
    - in the style of van gogh
    - (made|painted|illustrated|sculpted|designed|...) by van gogh
      - this feels like a separate kind of thing I might want to classify
      - ...I wonder if deconstructing prompts using compling tools might be a useful exercise? or rather, mine a prompt DSL out of the prompts.
      - basically what I'm doing right now already. 
      - if I can fully decompose prompts, I bet it'd be really easy to use that as a jumping off point to training a kind of prompt "infill" language model
      - seq2seq autoencoder trained to learn the semantic template (i.e. DSL) as the hidden latent representation along with a small "scratchpad" latent vector to learn a content encoding, really mainly for the purpose of training the AE, because without which there'd be no hope for guessing content that's been explicitly removed from the template. oh shit if we use a standard normal prior here like a noise vector for a GAN, we could use this for sampling. maybe I could even use an adversarial loss here? actually, I bet I could use contrastive and adversarial both. this is a whole idea onto itself, I bet I can train a model to learn this... shit what if I let it learn a REALLY limited (small) codebook for the template part? could it just learn a template? I could even encode a full sample sentence to get the correct template instead of needing to just know how to write it. so that meand after fitting the auto-encoder to construct the templating language (the learned codebook), we used masked prediction to learn the sampling language model, and then the masked token gives us a natural way for users to specify "i don't even know what goes here, figure it out". to do: put this on the workbench
  * art styles
    - abstract art
    - in the style of postmodernism
  * materials
    - made of glass
  * media (qua material)
  * 
  
  
an extension of this could be *guided* infill, so like conditioning the infill process on an artist name to stear *this* tool to provide similar artist names, etc.
