# Social Media and Singularity Theory: Information geometry and society

labels: alignment, publication, information geometry, philosophy

Thread: https://bsky.app/profile/digthatdata.bsky.social/post/3k3eujdu3un2m

This whole situation with volatility in the social media adoption space is a perfect demonstration of why "singularity theory" has become a big deal in explaining deep learning recently. Before we can adopt the "best" technology, as a society, we have to abandon the old one. But this requires achieving a critical mass, after which a phase change (adapting to the new normal) can happen. This kind of phase change happens at what's called a "singularity" -- used here in the same sense as how a black hole is a singularity. It's a geometry term of art. -- On either side of the singularity is a buffer region of slow change. Inertia. As you approach a region where change is possible, you accelerate towards that change as you get closer to it, but when you're not basically right on top of it, it's hard to get enough momentum to meaningfully change. We see this sort of phenomena all over the place socially. The social equivalent is Thomas Kuhn's "paradigm shifts" that happen in the neighborhood of "scientific revolutions". The revolution is a "signularity". 

Back to deep learning. So one of the subtle takeaways from the whole singularity thing is that if you *want* to change, you want to ride as close as you can to that volatile region where change is possible, and apply a kind of "pressure" that encourages your current state to move towards improvement. in deep learning, this pressure is the loss function, and the singularities represent successfully modeling a facet of the problem. so by understanding the geometry of the problem space like this, we can make inferences about how to steer the gradient towards singularities to learn as quickly as possible. back to social phenomena. locking in to a technology has its pros and cons. one of the pros is that we're all communicating with each other. but one of the cons is that it's harder to innovate as a society. geometrically: the closer we get to instabilities, the easier it is for society-wide innovation to be possible. but this only works if we apply the correct "pressures" to the system. While we're in the neighborhood of an instability, we're more susceptible to pressure and change generally. imho, the "alignment" problem is less about AGI specifically and more about applying the correct "pressure" in the neighborhood of  societal instability to push it towards improvement generally, while keeping it structurally in the region where continued improvement is still possible and not "overshooting" into a new state of stuck-in-the-mud, like we have with twitter lock-in.

it's important to be able to adapt, not just at a small scale, but at a large scale. global adaptation can only happen when the adaptation can propagate quickly, and this is what characterizes that singulartity. the volatility is the speed at which information propagates through the network.

Time for some graph theory I guess. so there are a variety of ways you can characterize how a graph (qua network) is connected, and certain connectivities can carry certain properties. we've established that a property we want is for information to propagate quickly. /n

In the context of a graph, we can formalize this property concretely as how many jumps it takes to get from one node to another. graphs that have small values for this property are called "small world" networks, and are characterized by having lots of "hubs", nodes with more connections than average

now imagine we constructed a similarity graph of like... i dunno, all the SDEs in the world, where two SDEs are "close" to each other if they use a similar technology stack. /n

Having a "small world network" in this space means having a wide diversity of tech stacks across SDEs, each of which is a small modification of a related tech stack.If everyone is locked in to the same exact tools, remove that one tool and it impacts everyone. /n

What would actually be optimal would be to have a diversity of tools, even if this came at the cost of individual tools having a more local scope in the global network. As long as things aren't *too* fragmented, you still get fast change propagation. /n

but if things are too centralized, you give up robustness to failures. This is the issue we're seeing with Cavendish bananas. We used to have a wide diversity of different delicious bananas to choose from. I've had the pleasure of having some outside the US. /n

But in the US, all you can find are Cavendish bananas. The convenience and consistency is lovely, but it came at the cost of diversity and if anything happens to that one species of banana, like a pandemic, bananas go from a major crop to an endangered species overnight. /n

We're seeing this same problem reflected all over the place. An unfortunate consequence of social media centralization is that we're all looking at the same thing. this has measurably hurt research. more scientists are being published, but fewer are being cited. /n

The solution is multi-scale structures that give us high robustness and low latency. The problem is incentivizing them.
