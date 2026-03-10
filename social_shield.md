# LLM Shield / Social Shield

labels: experimental, open_source, public_good, misinformation_countermeasures

use an LLM agent to dobackground research on the users who show up in your feed, or at the very least who you recently/frequently interact with.

warn user if they might be engaging with a bot

simple bot detection heuristics:

* unable to associate account with external identity
* account is no older than external identity
* account is < 1 year old
* following >> followers

manifest as a community label.
- rule: label includes name of "accusing" user.
- browser extension:  count labels applied by other users, and/or categorize autonomously and propose/associate own label
