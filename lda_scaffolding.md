# LDA-scaffolding.: part of speech prediction as an auxilliary loss

label: experimental

this has to have been done before, right? 

for this to work, the auxiliary loss would only kick in at the end of a word. so run the whole world through the normal pre-training loss, and then score the last token.

bettery yet, model this as an isolated component, i.e. that could later be reused as a kind of plug-in, like a LoRA that warm-start's training

there must be some generic parameterization that could be used to cover grammar. maybe like an LDA? LDA-scaffolding.
