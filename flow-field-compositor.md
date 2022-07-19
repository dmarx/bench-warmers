# flow field compositor

1. supply a list of video paths and weights (can be a function of 't') -- prompt for instance segmentation? Mask?
2. load each video and compute its flow field
3. pool over all videos fields
4. use this as an init...

wait no, that's not it. use each flow field as a separate channel, so we can attach different flows to different prompts, or some how apply them independently from each other.

anyway, some tool to facilitate/generalize working with multiple flow fields driving the same animation
