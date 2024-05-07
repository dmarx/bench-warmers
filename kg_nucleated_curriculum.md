# Knowledge-Nucleated Dynamic Curriculum Learning

labels: experimental, ssl, self_supervised_learning, curriculum_learning

**motivating hypothesis**: A component of a transformer model's learned representation is an implicit knowledge graph. If this is the case, we should be able to accelerate learning this component from strategic, preferential sampling of data to preferentially expand the graph with respect to local neighborhoods anchored on knowledge that has already been solidified

### Step 1: Nucleation

We need a "seed" graph to start this process. Construct a knowledge graph over some core foundational concepts or topics and represent this graph as a subsample of the dataset (i.e. relevant to this graph)

### Step 2. Learn the local graph

train on this subset of the data

### Step 3. Be curious

Apply a parameterized "curiosity" function to identify new topics and prioritize graph expansion.

Learn this function by collecting "generative rabbit hole" explorations, and/or wikipedia rabbit hole explorations

### Step 4. Do research

focusing on a neighborhood of related topics identified in the previous step, retrieve a new subset from the training corpus relevant to this topics. goto 2.

---

There are a few challenges here.

* catastrophic forgetting
  * If we can address catastrophic forgetting in a way that modularizes new information in a composable fashion, we could use this strategy to trivially parallelize training
* would be cool if we could regularize the learning process to prefer updates to fewew parameters. Maybe truncate the gradient to only the highest magnitude values or components (i.e. rank reduced gradient).
  * Maybe we can use LoRAs/ReLoRA as a way of parameterizing these knowledge neighborhoods? That would be pretty sweet if we could use this sampling strategy as a way to make ReLoRA work or something like that.
* Requires that we have a retrieval index over the dataset
  * the pile is sufficiently widely used that something like this probably already exists, but might be a bottleneck in this procedure.
  * maybe we can construct a job queue for neighborhood expansion and expand the dataset asynchronously relative to training?
