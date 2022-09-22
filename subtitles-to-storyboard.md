# subtitles to storyboard

wrap an srt parser in a simple utility that tries to estimate good 'scene' transitions for image generation.

part of this parameterization is providing 
* target scene duration - how long a particular sequence will be, or alternatively how long a caption was relevant
* target tokens per caption - another dimension of constraint to help with segmentation

then.. yeah, just pass it an srt file and it would return a sequence of prompts with start and end times for each
