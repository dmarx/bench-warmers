# Scratchpad Prompting

Normal causal pre-training, but prefix the generation with a comment indicating a token budget of free thinking, bracketed with a forced closing token.

Something like:

```
{some arbitrary span of tokens. at some randomly selected index (maybe constrained to ends of sentences)}<SCRATCHPAD:500>{let the model do what it wants for a bit. mask this from the loss}</SCRATCHPAD>{normal autoregressive language modeling objective picking up as if the scratchpad span didn't exist}
```

Let the model generate what it wants to supplement the context.
