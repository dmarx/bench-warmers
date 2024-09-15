# LLM personal archive pre-processing (e.g. search prompt)

labels: shitpost, publication, public_good

## Identifying content worth developing further

* score content against queries like "publishable content", "novel idea", etc. 

## Identifying content to filter from a public release

* personal information
  * what can we infer about the author? what does the existence of this interaction imply about the author? infer as much about the (author)/(people in the conversation) as you can, including high-confidence facts and low-confidence bias-associated inferences.
* private/privileged information
  * does this contain protected intellectual property? - e.g. a prompt to summarize a large body of text
  * is this "private"? - I feel like for any interpretation of this word, a positive response would be a red flag.
* "safety"
  * is this sensitive content? - again, feel like this is a reasonable catch-all flag
  * is this something anyone might find offensive?
  * could this be considered an "infohazard"? My usage of "infohazard" here is inclusive of e.g. publishing a copy of the "hacker's handbook" 
  * is this content that might be considered "age-inappropriate" for a reasonable lower-bound of the age of a random person browsing the internet?
