# Git Utilities to simulate Github "Private Branch" functionality

![](https://img.shields.io/badge/tag-tooling-lightgrey)  
![](https://img.shields.io/badge/tag-stability-lightgrey)  

it's an ongoing frustration that "public/private" visibility can only be controlled at the repo level. 

would probably not be too hard to write a few scripts/workflows to facilitate making a private clone behave as though it were hosting private branches 
of a public repo.

* headless clone "mirror"
* scheduled github synching workflows
* "publish" script publishes a branch to a public fork of the target repo and creates a PR to the origin repo
  *  PUBLIC - origin
  *  PUBLIC - fork (upstream=origin)
  *  PRIVATE - mirror (upstream=fork or upstream=origin)

Q: should POC start from a private repo we want to publish, or forking a "private branch" off of an already public repo?
  - ultimately want to support both of these, but need to pick one to start with.
  - probably simplest to assume the public code already exists and we're creating a fork.
  - the specific use case I want to address has both already existing in a disconnected fashion
  - ... need to start somehwere. let's start with adding a "private branch" to an already public repository

# Proposed workflows

## Adding a new "private branch" to an already public repository

to do: come up with a better name so I can stop using quotes everywhere.

https://stackoverflow.com/questions/3959924/whats-the-difference-between-git-clone-mirror-and-git-clone-bare
https://docs.gitlab.com/ee/user/project/repository/mirror/



