# Brushstroke Diffusion

# motivating idea

via https://twitter.com/DigThatData/status/1584826328704221184

> train a diffusion model to invert a "paint splatter" corruption process, so the noise latent would basically be jackson pollock paintings.

# related work

* https://github.com/Huage001/PaintTransformer
* https://github.com/arpitbansal297/Cold-Diffusion-Models

# brainstorming

* if the corruption process includes deleting brushstrokes, that would give opportunity for the inverse processes to include predicting new brushstrokes
* My hope here is that we could train a "touchup" model that iteratively predicts new brushstrokes or paint splatter or whatever atomic unit of a visual artists labor
* using the PaintTransformer brushstrokes as the final target of the inverse process, maybe we could shuffle or randomize strokes for the forward corruption?
  * pretrain on PaintTransformer, finetune on real art
