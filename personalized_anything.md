# personalized anything

labels: productivity, personalization, llm, gdpr_data_export

here's how this would work e.g. for mastodon. generalized from there.

1. consume feeds of mastodon people i follow
2. use plugin adaptors to expose content to an LLM, add CLIP embeddings + images
3. track my likes
4. predict likes
5. track what I have and have not seen
6. >> potential emergent behavior: recommends content to me because it knows i haven't seen it and that the people around me are talking about it
7. i maintain my own personal searchable database
8. i use it for a feed
9. it RLHFs. assign a rank to each candidate document (separate model for classifying stuff i don't even need to archive)


so i'm thinking about mastodon right now, but this could really be a feed of anything. subreddits. hackernews. github repos. 

just let an LLM see your content interaction history and ask it directly if a piece of content is something you'd find interesting. 

NTS: crack open the twitter data export

----------------

i've already got my twitter export, i just need to finetune on that.
grab some pre-trained multimodal model, finetune it on whether a tweet was authored, liked, or retweeted by me. for quote tweets, fill the contents...
naw i'm making this too complicated, just generic LLM autoregressive next word prediction objective should be fine. 

---

relevant:

* https://github.com/ljsabc/Fujisaki

anyway, multimodal model. LLaVA or whatever. 

"instruct" tune it, predicting my reply tweet in response to the context "prompt"

... this has to already be a thing by now, right?

---

this looks promising: https://github.com/georgia-tech-db/evadb

also this: https://github.com/kvablack/LLaVA-server

while we're at it: https://github.com/pgvector/pgvector

if i go llama family: https://github.com/coreylowman/llama-dfdx

---

fallback plan: augment a conventional LLM with visual descriptions

* https://github.com/ContextualAI/lens

maybe some shortlist of content like important AI papers:

* https://github.com/thunlp/Document-Plugin
* https://github.com/thunlp/Knowledge-Plugin

---

ok now we're talking: https://github.com/Luodian/Otter

- inherits from OpenFlamingo


---

separate project from personalized policies: persist papers from arxiv (plus code) as knowledge plugins for personalized research assistant

---

uh... hard maybe... https://github.com/princeton-nlp/MeZO
