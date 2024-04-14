# Continous Graph Embedding

labels: ricci_tensor, riemannian_geometry, experimental, gnn, topology, differential_geometry

Model the graph as a continuous manifold, model entities on the graph as points on the manifold, and a learnable shell parameter. 
The shell functionally defines the entity as a region of the manifold.
Define edge(from: Node, to: Node) as an indicator function that returns true if the veridical graph has an edge from x to y. 

```python
def edge(from: Node, to: Node):
  """an indicator function that returns true if the veridical graph has an edge from x to y."""
  d = distance(from, to)
  return d < from.shell.projected_onto(d).norm()
```

for a simple spherical representation, we can let the shell be a radius term. Any nodes inside the shell's radius, we draw an edge to.

for non-trivial geometry (still assuming trivial topology, no holes) we can fit a local covariance matrix to warp the local hypersphere (fixed radius) to a hyper-elipse (radius modulated by covariance). Covariance here is identical to the Ricci tensor of the local semantic tangent space (i.e. the curvature relative to the riemannian (banach?) "perspective" of that entity).

literal semantic relativity. QUAntiFIABLE semantic relativity.


## Expected Properties

### Semantic arithmetic over graphs

semantic arithmetic where we are conditioning on a graph over inputs. this is actually completely identical to a normal conditioning vector.

BUT: we can take advantage of the shell term to operate as a weighting function, and invert the spatial warps to normalize the weightings in the topology of the space.

Apply this representation to a dataset to learn the local warp tensor. Ricci tensor.

Can we use this to fit just the ricci tensors on a frozen representation? use that to measure the local curvature of the space?
