# we need a documentation embedding standard

![](https://img.shields.io/badge/tag-standard-lightgrey)  
![](https://img.shields.io/badge/tag-documentation-lightgrey)  
![](https://img.shields.io/badge/tag-accessibility-lightgrey)  
![](https://img.shields.io/badge/tag-tooling-lightgrey)


https://twitter.com/DigThatData/status/1646891215290511362
https://discord.com/channels/1086642728764452924/1088253884725727322/1096231558207242240

some challenges here:

1. building the embedding representation for a documentation base should be part of the CD for those docs. it's the only way to ensure the embeddings are up to date and properly versioned.
2. the SOTA on language representation is a rapidly moving bar, so it's unreasonable to try to pick or impose a particular model as the standard representation space
3. if documentation owners pick how their docs are embedded, that means that specifying what model was used will need to be part of the documentation embedding spec.
- constraining expectation to huggingface-hosted models would help, but then there's still some securiity concern. even that aside, there's still the issue of needing to download
and inference some specific model just to be able to read a particular set of docs. that certainly doesn't make a ton of sense.
4. maybe we need some sort of standard for emitting natural language queries to docs. that way the docs could represent however they want, and the LLM would just expect to receive a
a cursor that yields relevant chunks of documentation.
5. starting to feel like what we need here is a documentation hosting and retrieval service, like readthedocs

one way we could potentially get around this would be docker. the repository could build a container that provides an endpoint for a lookup service. could even take text as a payload
and then the whole "fetching and using the correct model" thing would be abstracted away. 

frankly, a simple local embedding DB that could be pinged like this would just be super useful in general. 
