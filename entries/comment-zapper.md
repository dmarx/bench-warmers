# comment zapper.md

![](https://img.shields.io/badge/tag-tooling-lightgrey)

code cleanup tool that:

1. looks for comments (AST parser?)
2. classifies the commented text as either code of natural language
  - simple knn classifier
  - some small test corpus vs surrounding code fragments
3. if a contiguous comment block contains only code, delete it

* need to avoid markdown
* how to prompt user approval?
