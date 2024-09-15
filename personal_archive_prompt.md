# LLM personal archive pre-processing (e.g. search prompt)

labels: shitpost, publication, public_good

## content worth developing further

* score content against queries like "publishable content", "novel idea", etc. 

## content to filter from a public release

* personal information
  * what can we infer about the author? what does the existence of this interaction imply about the author? infer as much about the (author)/(people in the conversation) as you can, including high-confidence facts and low-confidence bias-associated inferences.
* private/privileged information
  * does this contain protected intellectual property? - e.g. a prompt to summarize a large body of text
  * is this "private"? - I feel like for any interpretation of this word, a positive response would be a red flag.
* "safety"
  * is this sensitive content? - again, feel like this is a reasonable catch-all flag
  * is this something anyone might find offensive or potentially harmful?
  * could this be considered an "infohazard"? My usage of "infohazard" here is inclusive of e.g. publishing a copy of the "hacker's handbook" 
  * is this content that might be considered "age-inappropriate" for a reasonable lower-bound of the age of a random person browsing the internet?
  * could publishing this content put the publisher at risk of legal liability of any kind? - overbroad, needs work

## low quality content

* factually incorrect
* likely untrue or invented, fabricated
* incomplete generation
* low quality writing
* overly-simplistic writing
* targets a general or uninformed audience rather than a highly educated reader
* highly context specific, only makes sense in the context of a broader dialogue (rather than stand-alone content/article)
* shitposting, nonsense
* conversational interactions
