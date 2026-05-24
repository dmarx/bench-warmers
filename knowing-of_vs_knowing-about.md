# Knowing-*Of* Vs. Knowing-*about*

labels: philosophy, deep-thoughts, publication

(I think this crystallizes what's so fascinating to me about the "what's in a name?" project)

Let's say I show a VLM a photo it's never seen before and ask it about.
Now consider showing that same VLM a famous photo that showed up prominently in its training data, 
both visually and textually. Something like the marines planting the flag at iwo jima, a photo about which
a lot has been written, and also the surrounding context. Now let's say we take some famous image like this, 
leave the text contents in the dataset, but remove all copies of the image. If we ask the VLM questions
about the image by name, it will be able to respond to a lot of questions as if it were looking at the photo.

So we have a kind of semantic version of The Martian Neuroscientist here: Mary knows everything there is to 
know about the physiology and phenomenology of the human experience of color, but she was raised in a completely 
black and white environment and has never had the actual experience of color. There is something 
substantively different about the nature of her response to questions about the experience of color
before vs after she is transported to her first color-capable environment. 

Phenomenologists like to ascribe this to "qualia". Qualia is the externsic of the knowledge, but the intrinsic 
component is subtler and does not require "qualia" to reason about.

I posit that Mary's third hand knowledge "of" color vs first hand knowledge "about" color is 
similar to the phenomenon of the efficacy of naive bayes: given a handful of pieces of information that
I have strong priors for, I can semantically traingulate a lot of things very believably without
any direct knowledge about them.

Earlier, I invoked the example of "the marines planting the flag at iwo jima". Even if you've never
seen this photo or any visual representation of it, just from the title alone we can infer
a lot about what we expect the image to look like: "Iwo Jima" places it as the Pacific Theater of WWII. 
We can expect there to be multiple men in American military uniform, probably equipped for battle.
Also prominent in the photo, probably being carried by one or more men, is a flag, probably The American Flag.
WWII gives us a time period, which speaks to the photography technology and color quality we should anticipate.
And so on, and so forth, and that was just from the title. Now consider further that a text LLM has probably
read many descriptions of this image despite never having seen it: it knows there's five men,
all working together to raise the flag, maybe even knows descriptions of the appearances of the individual men,
knows what the background looks like, etc.

So now consider I invent a name -- Jose Soures (lol I pulled Jose Suarez out of my ass, turns out that's a baseball player).
From the first name, we've got male, probably latino. Name popularity changes over time, so we may even
be able to infer a rough age range. Consider if instead I asked for Zebadiah.

Let's say we ask a text to image model to generate an image by *name* like this. 
Person, place, whatever. And let's say the images it generates are consistently self-similar.
How do we differentiate "the model recognizes the person who I'm talking about and knows their face" vs.
"the model is able to make a lot of good educated guesses and/or has strong biases about information 
transmitted in the request, has no actual knowledge of the subject I'm asking about, but
is able to guess consistently enough to fake it?"
