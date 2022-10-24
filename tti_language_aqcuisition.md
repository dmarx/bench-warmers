# data science project investigating "language acquisition" for TTI prompting

consider some subset of users who exhibit a clear "session" behavior that terminates with some sort of success signal, 
e.g. a user manipulates a block of text over some contiguous period of dreamstudio use, and then rate at which generated images are downloaded suddenly spikes.

let's call some measure of that interval the user's "time to success" (TtS) for that session.

I predict that as users get increasingly familiar with image generation and with a particular model, an individual's TtS will go down over time, possibly plateauing.

We could use this phenomenon (assuming it exists) to measure how easy a model is to learn, and how easy it is to use. 

* a model is easy to learn if the expected time for an individual's TtS improvement rate plateaus quickly.
* a model is easy to use if the expected TtS before plateau is low
