# look-ahead traversal sampling

here's how we can apply 'optimal odering' smoothing to image2image

1. for a frame at time=t, sample k variations
2. same thign for t+1
3. use traveling salesman to find shortest path through t and t+1
4. hold on to t, use it to sample new/addl t+1 candidates. 
5. rinse and repeat, incrementing t

goal here is to sample in the neighborhood of the serial animation we'd otherwise generate,
exploring the available local degrees of freedom to potentially find a nearby image that gives a smoother animation
