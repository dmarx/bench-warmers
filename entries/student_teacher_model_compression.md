# student-teacher model compression

this is a classic approach, right? why isn't this a thing that someone's already thrown at LLMs or SD? or is it?  
i have a strong hunch there's still model compression wins to be achieved here.


anyway, the general idea I have here is to train an MLP on an auto-regressive reconstruction loss over the token softmax
