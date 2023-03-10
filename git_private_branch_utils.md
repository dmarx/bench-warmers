# Git Utilities to simulate Github "Private Branch" functionality

it's an ongoing frustration that "public/private" visibility can only be controlled at the repo level. 

would probably not be too hard to write a few scripts/workflows to facilitate making a private clone behave as though it were hosting private branches 
of a public repo.

* headless clone "mirror"
* scheduled github synching workflows
* "publish" script publishes a branch to a public fork of the target repo and creates a PR to the origin repo
  *  PUBLIC - origin
  *  PUBLIC - fork (upstream=origin)
  *  PRIVATE - mirror (upstream=fork or upstream=origin)
