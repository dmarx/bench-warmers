# train an LLM with a "sense of self" token

labels: experimental, llm, theory_of_mind, ai_philosophy, 2hi4this

train a model to have a "sense of self" by explicitly encoding its "name" in a specific token. this is effectively just a `<start-of-document>` suffix token
that might have some edge cases where it shouldn't be used. But in particular, I'm envisioning choosing a redditor in a comments thread 
(probably author of highest scoring root comment with non-trivial returning engagement from author) and swapping out 
`RedditorUserName123:` with `<self>:`.

stupidly parallel training: 

augment a thread by picking a couple of different users and asking the LLM to simulate the perspective of each.
THIS IS ONLY ACCEPTABLE WITHIN THE SAME (mini)BATCH. Otherwise we're just asking the LLM to memorize the conversation.
Aggregate over conversations to reduce the batch.

If a thread has 100 comments across 10 users, that would be 1000 comments. if avg comment length is 100 tokens, that's O(1e5) tokens per thread.
I think critical batch size is generally O(4M)=O(1e6) tokens. So that's just O(1e1) threads per batch.

Effectively amplifies dataset size by O(1e3).

So for a target of O(14T)=O(1e13) tokens at O(1e6) tokens/batch, that's O(1e7)=O(10M) batches. 
At O(1e1) threads per batch, that's just O(1e6) comment threads.

It doesn't have to all be on the same node. we could distribute out non-overlapping subsets of users.
Preferably non-overlapping.
Actually, if we permit overlapping we could (poisson) bootstrap resample users, so we wouldn't even have to pre-allocate names. Each node
could just independently pick its own names to independently sample for its aug. 
