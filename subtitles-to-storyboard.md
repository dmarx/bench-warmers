# subtitles to storyboard

![](https://img.shields.io/badge/tag-tooling-lightgrey)  
![](https://img.shields.io/badge/tag-wip-lightgrey)  
![](https://img.shields.io/badge/tag-opensource-lightgrey)  
![](https://img.shields.io/badge/tag-prompting-lightgrey)  
![](https://img.shields.io/badge/tag-accessibility-lightgrey)  
![](https://img.shields.io/badge/tag-animation-lightgrey)  
![](https://img.shields.io/badge/tag-completed-lightgrey)  


https://github.com/dmarx/video-killed-the-radio-star

---

POC! 
https://colab.research.google.com/drive/1maXdiY1CIijYgRjMda_6vEL7keP8wr-l#scrollTo=IwLoLLXpbzD2


---

wrap an srt parser in a simple utility that tries to estimate good 'scene' transitions for image generation.

part of this parameterization is providing 
* target scene duration - how long a particular sequence will be, or alternatively how long a caption was relevant
* target tokens per caption - another dimension of constraint to help with segmentation

then.. yeah, just pass it an srt file and it would return a sequence of prompts with start and end times for each
