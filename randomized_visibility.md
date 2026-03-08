# Randomized visibility for subscription-gated content

labels: experimental, public_good, new_media

## Background

journalistic enterprises face an ongoing dilemma: the information they are 
hoping to communicate often has an urgency component. they *want* their message
to spread far and wide, to influence the public opinion. conversely though, 
they need to put bread on the table, and one of the maine ways they achieve this
is via a subscription model where some subset of content (often all) is only
accessible to subscribers.

### subscription model

the current "middle ground" is to attempt to attract new subscribers by making the
very top of the article visible (title, maybe first paragraph) to unsubscribed
visitors. this has the consequence that the spread of the substantive content
is usually significantly hindered. non-subscribers are disincentivized from
resharing because they can't even read the content, so reshares are limited to 
subscribers and people who were only going to reshare based on the title anyway.

### free articles

A newer middle ground approach is "gift links", where a subscriber has a limited ability
to share links to the full content that are viewable by non-subscribers. this 
approach is gaining popularity, but has the consequence that visibility of content is
a function of how it was discovered. If an unsubscribed user is looking for a
second source because e.g. they were provided a free article published by an
ideologically compromised source, they might stumble on the content via search and only
see the title validated but the content censored, so their view on the topic will still
be filtered through the perspective of the compromised source's narrative.

## Alternative: stochastic visibility

From the perspective of the unsubscribed person, whether or not they will encounter a
gifted link in the wild is a random process. What if we bake that random process directly
into the CMS? Assign each visitor a fingerprint, assign each fingerprint a visibility
latent, then condition the visibility of any given article on the latent of the visitor.

This way, some fraction of unsubscribed users will still have the potential to contribute to
virality effects by stumbling on the content randomly,with full visibility, and then resharing.

Additionally, parameterizing visibility in this way is amenable to time considerations.
We could make it so the function that evaluates the latent also considers the time since
publication, so content that has been very recently published has a higher likelihood of
visibility, satisfying the urgency of communicatingthe information, while preserving the
gated visibility for less recent visitors (and then perhaps reverting to high visibility 
again for older archival content for historiographical purposes).

## Weaknesses

This system is easily spoofed. Someone with a VPN could just visit different servers until
they get lucky.

This might actually be a feature rather than a bug, since it would incentivize revisiting
the same page multiple times, which creates the opportunity to serve multiple ads to the
same user.

Relatedly, another approach could be to hide portions of the content until the user clicks
on an ad. But that's pretty obnoxious. Very 1998. Visitors don't want that, and most 
advertisers probably don't want that either.

## Conclusion

Information wants to be shared. The subscription model itself undermines the dynamics that 
subscription growth depends on, as well as undermining the influence of the author.

By adding a stochastic element to content visibility for non-subscribers, we can
simultaneously leverage some of the incentivization of the subscription model while also
promoting the network effects required for having the desired influence and subscribers.
