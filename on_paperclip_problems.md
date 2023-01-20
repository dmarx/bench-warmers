# On Paperclip Problems

layout my eleuther rant here, maybe invite Dean Pleban from dagshub to coauthor, follow up from our conversation
- boat turning evil before steering into rocks vs. already on the rocks and not bailing it out

---

**Why Complexity Theory Topics Are Important For Alignment

*(modified from [discussion](https://discord.com/channels/729741769192767510/730095596861521970/1052599419536670760) on Eleuther.AI discord, 2022-12-14)*

Summary: because AI systems interact with people and each other in complex ways and it's important to have tools to understand and investigate how large, complex, possibly dynamic and chaotic systems behave.

Complexity Theory provides tools that facilitate studying things like the dynamics of how information flows through a community. If a scenario for an AI risk has dynamics similar to a zombie apocalypse or an epidemic, these are the tools you're going to want to understand what kind of interventions will be effective in containing or intervening. Complexity Theory also contains tools for understanding and studying emergent behaviors of systems, studying how units in a system can collaborate to manifest complex behaviors that may be non obvious from studying the units in isolation.

> (But isn't the problem of AI safety mostly about how to make one safe AI? or at least, the effects of powerful AI in the hands of a bunch of humans, and how that transforms society, is a seperate problem from creating just one aligned superintelligence. right? What you're talking about seems related to governance, and policy things.)

what I'm talking about is how you can e.g. implement microsoft word in game of life. If your vision of AI is constrained to an automaton in that system, you miss the emergent behavior of the system which is actually what's doing the interesting thing. if an AGI manifests as some sort of super organism like an ant colony, it's pretty myopic for the alignment community to constrain their concerns to aligning a single ant when it's the behavior of the community en masse that actually has the macro impacts. 

> (Yes if an AI is more like an ant colony, complexity theory would help, but why would it be like an ant colony? (or some other system that's best described as a bunch of individual creating emergent macro behavior)

because as far as we can tell, that's how human cognition works as well. we're getting into epistemic territory now, but part of the knowledge gap I'm describing here is confusion over what "one safe AI" even means. the language you're using here reflects a folk psychological understanding of "identity" which contemporary research has increasingly identified is an illusion. we should be concerned about an "ant-colony-like" AGI because as far as we can tell, that's how our own mind works as well. the idea that you are a "single agent" is actually more a property of your outward behavior and not the composition of your cognition. it's all an illusion. https://plato.stanford.edu/entries/consciousness-unity/

> (I mean you can say, "behavior of cells are nothing like macro behaviors like emotions" but then do you need complexity theory to describe things like that? Like how does complexity theory help explain macro behaviors, that are a result of lots of cells or whatever doing their thing?)

not just lots of cells. collectives of what you want to describe as "agents". as a concrete example in the human model, there've been studies done with people whose hemispheres have been surgically severed demonstating that their different hemispheres can exhibit different beliefs. like, one side of your brain believes in god and the other doesn't.

> (or at least I can see sometiems that it's an illusion. usually it feels pretty much like I'm one thing)

and that 'feeling' is an emergent property of a bunch of things in a system interacting in complex ways 
here, i'll let MLST take over the consciousness/emergence conversation: https://www.youtube.com/watch?v=_KVAzAzO5HU

> yes but why does subsystems existing, mean that complexity theory is useful?
like water's wetness can be called an illusion, but it's still useful to have the concept "wetness" to describe things, as opposed to seeing it as molecules doing their thing

because AGI doesn't have to be a property of a single neural network. it can be an emergent property of how a bunch of different, seemingly isolated things interact with each other, and we are possibly part of that system and these are the tools for characterizing those kinds of behaviors that we otherwise can't see from inside the system.
consider maximizing paperclips

> what o you mean "and we are possibly part of that system"? like the entire human race + AI systems are 1 giant ant colony?

sort of. "I" am comprised of a lot of cells that I consider "me", but that also includes flora and fauna.
bacteria comprise part of the system that is DigThatData, and there are times when I will actively attack the things living in me because I consider them harmful

i assure you, my white blood cells have no idea that DigThatData is chatting on discord right now, despite contributing to that emergent behavior of the system they are a part of

given our understanding of ourselves and how emergent behavior and capabilities can evolve from complex dynamics, whether or not you suspect AGI could manifest as a macro system of this kind, it can't hurt to understand better how they work and how to characterize their behavior

being more concrete, the reason I think the alignment community should be concerned about this sort of thing is specifically because of the alignment community's purported concern for problems that could manifest in the form of **"paperclip maximization"**.

social media algorithms have been assigned to "maximize engagement" and "maximize CTR" etc., and it seems they've determined that the best way to do that is to ideologically polarize humanity, encouraging xenophoboia, stochastic terrorism, and civil war. this is, in my mind, directly analogous to every formulation of the "paperclip maximization" risk parable I've heard. so if that's a legitimate concern of the safety community, then it doesn't matter whether the "agent" is a single thing, or an emergent property of a system behaving a in a way that has no may or may not have intentionality. I find myself repeating this rant here every month or so, so you're definitely on-brand with alignment for being skeptical that this is "relevant" to safety research. But as far as I can tell, the concerns of the safety community aren't something that might manifest in the future, they're something that are already manifesting now but the safety community is unconcerned because it's not a "single AGI" doing it.

> "paperclip maximization" is not a precise enough description of problems imo, because it could arise from different kinds of alignment problems. **Outer misalignment**, where it thinks you want a lot of paperclips, but doesn't understand that turning everyone into paperclips is bad, and **Inner misalignment**, where it knows that you don't want to be turned into paperclips, but it doesn't care.

what I'm asserting is that the issue isn't that "maximize engagement" is a dumb goal for us to assign to a single AI. The issue is that it's a goal we've separately assigned to google ads, facebook, twitter feed, reddit front page, etc., and the way these different algorithms interact with us is difficult to characterize without considering emergent phenomena from network effects

whenever I talk about this, alignment researchers seem to feel it's out of scope. the "agency" thing is the best explanation I've been able to come up with for why that is, so that's why I'm leaning on that so much

insofar as my cognition could be characterized as an emergent property of a system of "agents" interacting, my assertion here is that there's no reason we shouldn't consider that "AGI" could manifest as twitter+amazon+facebook+... interacting as well, and it would be difficult for us to characterize the global behavior of that "AGI" without consdiering it as a system


> This looks more like a governance/policy problem than the problem of aligning a superintelligence.

are you familiar with conway's game of life? would you consider the arrangement of cellular automata a "policy problem"? the automata are analogous to interacting algorithms with their own independent rulesets.

> https://www.lesswrong.com/tag/coherent-extrapolated-volition - "we should find a way to program it in a way that it would act in our best interests – what we want it to do and not what we tell it to."

---

* 2022-11-22 - https://discord.com/channels/729741769192767510/730095596861521970/1044698916668592229
* 2022-07-05 - https://discord.com/channels/729741769192767510/730095596861521970/994086971410481253 - global warming is a paperclip knock on effect
* 2022-06-30 - https://discord.com/channels/729741769192767510/730095596861521970/992307615176601670 - still bitter about global warming
* 2022-06-22 - https://discord.com/channels/729741769192767510/730095596861521970/989261044084011079 - lol
* 2022-06-10 - https://discord.com/channels/729741769192767510/730095596861521970/985027049481699369 - BMK doesn't want to litigate the term, but clearly is fixated on a definition already
* 2022-05-20 - https://discord.com/channels/729741769192767510/730095596861521970/977254997614006333 - shorttermism doesn't mean we can't address multiples issues at once
* 2022-05-07 - https://discord.com/channels/729741769192767510/730095596861521970/972678812930285698 - "alignment" vs "solving politics/economics and ethics"
