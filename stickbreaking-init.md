# stick-breaking prior for semi-correlated feature initialization

fleshing this out a bit more, I'm pretty sure the idea here was to intelligently add capacity to a network mid-training?

---

use a stickbreaking prior of chinese restuarant or indian buffet process (etc) to sample features weights into correlated groups

each "table" has its own weight sampling parameters that are fixed. so whenever we break a stick or create a new table (etc), we sample a 
e.g. a mean and variance for weight initialization

