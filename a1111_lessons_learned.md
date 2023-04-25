# a1111 lessons learned

![](https://img.shields.io/badge/tag-tooling-lightgrey)  
![](https://img.shields.io/badge/tag-opensource-lightgrey)  
![](https://img.shields.io/badge/tag-ux-lightgrey)  
![](https://img.shields.io/badge/tag-experimental-lightgrey)  
![](https://img.shields.io/badge/tag-stability-lightgrey)

documenting some thoughts on what makes a1111 work well as a foss project, brainstorming improvements for future projects

# extensions

this basically the crux of it. the ability for users to extend the platform with plugins is an extremely powerful pattern. there are a few design decisions that make this work particularly well for a1111

* offloading security concerns to users
* this isn't a great UX for a commercial project, but for an open source project it makes perfect sense
* discoverability and installability from within UI
  * discoverability further supported by a constrained tagging system
* curating a subset of components to an "unwalled garden" index that can be queried from within the UI.
* could be combined with the "offloading" pattern by adopting an `apt` registry style approach. let users create their own curated collections other users can subscribe to
* common ux toolkit
* something like panel-param could potentially make this sort of thing ux agnostic. experimentation required

## `modules.scripts.Script`

https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/master/modules/scripts.py

* workhorse appears to be [`scripts.Script`](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Developing-custom-scripts) class. could probably port a lot of funcitonality by supporting just this class
* encapsulates step-by-step processing flow with hooks and callbacks
* separation of data from processing
  * the `Scripts` class is structured to have methods overrided, but it's not actually an ABC. 
  * methods are all defined empty, users can override whichever ones they need or want.
  * separate runner class handles actually operating over the scripted procedure
  * abstracts away setup, building UI, batch processing

# misc

* internals: https://miro.com/app/board/uXjVMdgY-TY=/
* convenient and robust installation script
  - dummy-proof setup as much as possible
* in addition to UX customizability, extensive command-line flag options for backend customization and optimization as well
* separate categories of modifications encapsulated into isolated patterns
  * scripts
  * extensions
  * tabs
  * etc
* localizations explicitly supported

# questions

* what do the "hijack" procedures do?
