# hypernetwork code embedding

* https://arxiv.org/abs/2206.00606
* https://github.com/pyt-team/TopoEmbedX

use LLM embeddings to seed information at varying levels of hierarchy for learning improved embeddings over the codebase

- AST for types
  - keywords, functions classes, variables, etc.
- openai embeddings over sliding windows of tokens
- learn embeddings for respective functions, classes, lines of text, etc
