# investigating identity formation as a concrete example of grokking dynamics (+ NameBasis)

labels: experimental, publication, safety, alignment, interpretability

---

CLIP/SD has learned a variety of biases associated with names. these include:

* fairly good grasp of flexible identity attached to certain proper names - barack obama
  * "flexible" wrt able to adequately generate images of person at variety of ages in variety of scenarios
* strong bias towards a specific depiction of a proper name (identity overfit) - mona lisa
* strong association of name parts to given identities (identity overfit) - winona (ryder)
* age, gender, ethnicity, cultural norms in name parts (identity underfit) - "vicki" = senior white lady, "sullivan" = british
  * age biases correlate to baby name popularities correlated to training data volume for different time periods. name-age correlation expected to become weaker over future decades/centuries if current training paradigms persist, to be replaced with "era" biases.
  * ethnicity, gender biases reflect ethnographic features of naming preferences, etymology, genetics - e.g. regionalization and/or genetic features common to a family name

hypothesis: we should be able to identify phase changes in "grokking" specific identities if we monitor the learning process. expected phases, roughly:

1. identity is fully overridden by biases adopted from name parts
2. coarse identity components stabilize - age, ethnicity, hair and eye color, clothing style, likely scenery
3. identity stabilizes - model grokks unique identity, can flexibly apply to creative scenarios
4. identity overfit - model forces depictions to satisfy narrow constraints from training data, e.g. a particular expression, outift, scene, etc.

sub-hypothesis: detectable change in netowrk weights delineating representation of a unique identity: the network "knows that it knows" a particular named entity

* phase change from approximating an identity as a composition of concepts to assigning an identity it's own concept region/direction
  * maybe this never happens and all identities are compositional? seems unlikely, expect some identities to be compositional and other strongly represented identities to comprise important components of the bases along which other identities are represented


 ## related work

 * https://celeb-basis.github.io/
 * grokking
 * rome

## related idea: NAME BASIS

hypothesis: similar to how celeb basis woks, there are very likely natural language tokens/phrases that can be composed to roughly build fairly appropriate "identity" representations. seems like age, ethnicity, gender, body type, hair color, eye color etc. all get encoded to varying degrees in name tokens (among other tokens we could use). it probably won't be *as* effective as something like celeb basis, but that would be pretty magiclal if we could use straight up prompt engineering to "paint" an identity.

one take on this might be to construct a celebbasis, then interpolate along the embedding dimensions and generate names for the respective embeddings to learn/mine composable natural language components
