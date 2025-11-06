# training models to know what they don't know

labels: experimental

an aspiration with AI is develop capabilities that facilitate continual learning, metacognition, and explainability.

current models simulate meta-cognition, but their self-reports are unreliable.

one way we could potentially improve metacognition could be to run some sort of "debriefing" procedure after observing a training sample, like asking someone what they learned from an experience or what their main takeaway from a lesson was.

in a vacuum, "main takeaway" is a question of salience. in the context of an agent, it's a question of novelty.

I'm reasonably confident models cannot reliably communicate what they do or do not know. If you ask them about the veracity of a fact they haven't encountered, they can report that they don't know, but if you ask them what they do or don't know about some domain with a variety of properties, I don't think they can list the properties they don't have information on (unless they've been perhaps specifically trained to do that).

main idea: categorize a dataset using a knowledge graph, and leverage this to induce an ordering on the data so we can label facts the model has never seen before. we can then prompt the model to articulate what new information it has learned from some context.
