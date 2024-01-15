# Diffusion Video Models for Climate Change Prediction

labels: experimental, public_good

satellite image data over time.

* spherical embedding for position on earth
  * https://arxiv.org/abs/2310.06743
* time embedding for date correlation
* predict from an image or a context of images (same place, different dates)
* after fitting model, finetune controlnets for incorporating information from different modalities
  * do people ever cross-train controlnets? like finetune one while another is already applied to try and get them to work together better?

## relevant data

* https://developers.google.com/earth-engine/datasets/
* https://neo.gsfc.nasa.gov/
* https://landsat.gsfc.nasa.gov/data/

## Relevant projects

* SatCLIP
  * https://arxiv.org/abs/2311.17179
  * https://twitter.com/kklmmr/status/1732799037860880448
  * https://github.com/microsoft/satclip
