# personalized anything

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
