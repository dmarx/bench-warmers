# Deep DSL

ongoing work: https://colab.research.google.com/drive/1DDGxDIEuxFCJskP2Mo1DN0wNHqS-QCD7#scrollTo=0sXZ2lFI9En5  
...that could be an open in colab button, that'd be a really easy way to tag 'metadata'. fucking badges! yes!


use tricky multi-step deep learning to unsupervisedly learn a 'deep' DSL and a model that can sample from it, to facilitate prompt construction

## architecture

* VQ-VAE
* two component latent
  1. tokens2codebook
    - encodes pattern template
    - includes mask token for unknown fill type 
    - codebook functionally forms a structural DSL over specialized "parts-of-speech" for building prompts
  2. noise vector
    - captures content representation
    - single feature vector? feature vector paired with each structural token?
    
## Training

1. Use a pretrained frozen LM as an input encoder
2. Pre-compute corpus encoding
3. seed codebook with medoid vectors from corpus
4. learn/tune codebook using reconstruction loss, + contrastive loss over the feature vector
  - might need to add a mapping network to transform input gaussian to feature space 
6. learn a mask token using reconstruction loss and masked prediction objection
7. learn a prior over templates for unconditional sampling

## Use

1. User authors a prompt
2. encodes prompt to DSL template (codebook)
3. sample new prompts by conditioning on the template vector and modulating noise vector
4. generate prompt variations by additionally conditioning on a semantic proximity to the input prompt
5. generate diversity by replacing template tokens with the mask token

## Related research

* https://github.com/NVlabs/PALAVRA



# old stuff

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
