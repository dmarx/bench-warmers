# design a 'file type' (or related spec/standard)

![](https://img.shields.io/badge/tag-animation-lightgrey)
![](https://img.shields.io/badge/tag-tooling-lightgrey)

specifically for ai art and animation

## Issues this would address:

* facilitate 'resume' functionality when a generation procedure encounters an error
* facilitate forking sequences from a given image/animation state for variation experimentation
* link images to the settings (especially prompts) that were used to generate them
  * facilitate 'prompt management' by artists, e.g. grouping images by prompts, grouping variations of prompts and prompt templates, etc.
* link images to their position in an animation sequence
  * this is potentially complicated by processes like frame interpolation

## Some requirements

* lossless
* fast read
* artist-friendly
  * unobstrusive - use of this doesn't create any kind of 'lock-in' and images can still be read without special tooling that knows this format
    * piggy back on a conventional image format, attach metadata somehow? 
  * i think striking a balance between making this functional and friendly is going to be difficult. maybe let 'resuming' be a different thing and focus on attaching prompts to images.
* pair prompt text with image
  * current convention of packing the prompt text into the filename is silly. truncated sure, but the whole thing? comeon.
  * this could probably be solved with normal image metadata (EXIF?). the real issue is if we want to preserve model state like tensors of latents. call that out of scope for now.
  * maybe at a 'fork', we could keep it to a settings diff?
* images in a sequence maintain some sort of reference to their immediate ancestor(s) and child(ren)
  * feels like a job for something like a hash
  * if we think of the 'previous image' is a component of the generating state, maybe we could off-load the bulk of the settings to a file and reference that file via a UUID
    * Under this formulation, this process becomes more about developing a system for standardizing how these parameters are shared and moved around
    * feels sort of like ML experimentation and model checkpointing. 
      * Current paradigms are designed more around reproducibility rather than bookkeeping
      * MLOps tools generally presume all content will stay in one place rather than being moved around, and the movement and sharing is really what I'm concerned with here.
* minimally able to consume images generated through common tools like disco, pytti-tools, dalle2, dreamstudio, etc.
  * given an image with prompt in filename, extract prompt from filename
  * given an image paired with settings, port into... whatever this ends up being.


## Relevant resources

* https://en.wikipedia.org/wiki/Metadata_Working_Group
* https://en.wikipedia.org/wiki/Extensible_Metadata_Platform
* https://en.wikipedia.org/wiki/Portable_Network_Graphics#Ancillary_chunks
  * iTXt
  * tEXt
  * zTXt
* https://en.wikipedia.org/wiki/APNG
* https://en.wikipedia.org/wiki/WebM
* https://en.wikipedia.org/wiki/Container_format
* https://en.wikipedia.org/wiki/Matroska
* https://docs.blender.org/manual/en/latest/files/media/video_formats.html#ffmpeg-containers
* https://en.wikipedia.org/wiki/Ogg

looks like can just use PIL.save to write metadata

* https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#png
* https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save

jesus, what a fucking rabbit hole...

* https://pillow.readthedocs.io/en/stable/PIL.html#PIL.PngImagePlugin.PngInfo

usage example: https://stackoverflow.com/a/58399815/819544

looks like we can attach and read arbitrary text this way, but unfortunately these keys/values don't want to appear in the windows details pane

might have more luck if I use these reserved EXIF keywords? https://www.w3.org/TR/PNG/#11textinfo
