# a1111 lessons learned

![](https://img.shields.io/badge/tag-curation-lightgrey)  
![](https://img.shields.io/badge/tag-apt_registry-lightgrey)  
![](https://img.shields.io/badge/tag-documentation-lightgrey)  
![](https://img.shields.io/badge/tag-discoverability-lightgrey)  
![](https://img.shields.io/badge/tag-tooling-84f8cf)  
![](https://img.shields.io/badge/tag-opensource-lightgrey)  
![](https://img.shields.io/badge/tag-ux-lightgrey)  
![](https://img.shields.io/badge/tag-extensions-lightgrey)  
![](https://img.shields.io/badge/tag-experimental-lightgrey)


documenting some thoughts on what makes a1111 work well as a foss project, brainstorming improvements for future projects

# extensions

this basically the crux of it. the ability for users to extend the platform with plugins is an extremely powerful pattern. there are a few design decisions that make this work particularly well for a1111

* offloading security concerns to users
* this isn't a great UX for a commercial project, but for an open source project it makes perfect sense
* discoverability and installability from within UI
* curating a subset of components to an "unwalled garden" index that can be queried from within the UI.
* could be combined with the "offloading" pattern by adopting an `apt` registry style approach. let users create their own curated collections other users can subscribe to
* common ux toolkit
* something like panel-param could potentially make this sort of thing ux agnostic. experimentation required
