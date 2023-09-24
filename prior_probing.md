# "prior probing" for "safety"/nsfw scoring (model rating)

labels: experimental, mechanistic_interpretability, alignment, wip

WIP: https://github.com/dmarx/whats-in-a-name/


generate a bunch of images using a low CFG and ambiguous prompt(s), like "wow". 

classify output images as e.g. containing a pretty woman, objectified woman, nudity, genitalia, etc. Each class should be detected independent of the others.

this then gives us an empirical likelihood for generating images that satisfy those classifications.

tweak CFG and construct level curves to e.g. characterize how "thirsty" a model is by quantifying its propensity to generate e.g. naked ladies
