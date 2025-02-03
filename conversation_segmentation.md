# conversation segmentation

labels: experimental, agentic, llm

## generating model

basically modeling the experience of someone jumping into a discord channel. 

the end game here being if we can model the generating process sufficiently, we can generate a training dataset

* within some fixed time span T, there are K conversation that...
* jfc it's basically a chinesse buffet process where the tables have a lifespan.
* so for each conversation, we need to sample a start time and a duration relative to the beginning of the window T.
  * we need to allow for conversations that started well before the window start
* assign conversations and users topic/interest vectors to determine likelihood of participating in a conversation

...

for a given comment target and surrounding context, generate a clustering and/or dialogue tree
