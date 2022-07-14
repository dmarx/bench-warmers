# Layer-wise Super Resolution

**Insight**: When human artists paint, they build up their work in layers

**Idea**: decompose a generated image into layers, infill those layers, apply super resolution to layers, reconstruct image additively

## general procedure

1. apply something like salient object or foreground/background detection to identify the "top most" elements of an image
2. given a "top" element, mask and infill it.
3. rinse and repeat until most/all top elements are removed.
4. remove piecewise infills, perform a more global infill operation (procedure TBD, maybe only remove and fix infill region-wise)
5. apply super resolution to repaired background
6. in reverse order, iteratively return each removed element and apply super resolution
  - maybe the element-wise super resolution should or could be done using the original image context with a mask to isolate the region we want to clean up as a constraint? 

## motivating example

https://twitter.com/DigThatData/status/1547475210864996352/photo/1

For super resolution, I sort of want to remove the 'eyes' from the ocean component, super resolve that by itself, then add the eyes back on top of that.

similarly would be nice if we could infer a 'z level' attribute to the eyes in the sky, isolate most of the "top level" eyes for cleanup, super resolve the rough background, then separately super resolve the "top" and apply those back on cleanly

## Alternative uses

* infer a roadmap to guide how a human painter might approach making a similar piece
* manipulate specific components of a painting, e.g. move elemnts around. maybe we like a certain set of eyes and don'e want to remove them, but we want to reposition them

## Relevant works to build off of

* that paper where they used some evolutionary procedure to build up a painting with increasingly fine brushstrokes
* panoptic segmentation
* instance segmentation
* referring expression segmentation
* infill
  * [LAMA](https://github.com/geomagical/lama-with-refiner/tree/refinement)
  * Deep Image Prior
* Super resolution with image synthesis
