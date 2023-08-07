# Bam: Alignment Solved.

![](https://img.shields.io/badge/tag-meta-lightgrey)  
![](https://img.shields.io/badge/tag-experimental-lightgrey)  
![](https://img.shields.io/badge/tag-dataset-lightgrey)  
![](https://img.shields.io/badge/tag-alignment-lightgrey)


LLMs are a mirror on society because they encapsulate the biases of the data they were trained.

Therefore: if we were to simulate a dataset as if it were produced within "the best of all possible worlds",
the LLM will behave as if it came from such a place.

what would this entail? LAION 5B seems to be a solid representation of the internet:
how hard would it be to simulate a world from 5B generations?

maybe train a foundation model on this data to "align" the base model, giving us a kind of "naive optimist"
base model to work with, then finetune that base to fill it with facts. sort of like a child losing their innocence
as they encounter and learn hard truths about the world.

this is basically the idea behind data filtering, but it might be easier to just generate a bunch of data.

maybe we could apply some sort of "style transfer" to the pile/common crawl?
Like, for each webpage, pass it to an editing model that has a prompt like:

> "imagine you come from a world where no cruelty, pain, or death exists. Everyone is kind and friendly.
> People are supportive and empathetic towards strangers. There is no xenophobia, bigotry, or war. There
> is no inequality, there is no hatred. would this content be something you might encounter in this utopia?
> if not, change it into content that we might find there."

a classifier component passes through as much real human data as possible, trying to filter it to a "harmless" set.
anything that gets filtered out, goes through a "sunshine and rainbows" filter to try to preserve the data distribution,
so e.g. a news article about war might become a news article about international trade.

so first, let's build this rosiness classifier, and characterize the kind of content that falls into it as a sanity check.
next, we can experiment with translation functions. might even just be able to up-sample from related clusters,
or even just straight up filter it.

