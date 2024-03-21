# thinking fast and slow

labels: experimental

weights = W

decompose W into W = W1 + W2 s.t. W1 and W2 have same dimension

set a (alpha) to be a mixing rate, which starts at zero.

Learn W as W = W1 + a * W2, increasing `a` throughout training in proportion to lr

W2 are the "slow" weights and are learned conventionally

W1 will be learned parameterized as a hyperlora, and so are our "fast" weights.

let W1 = VZ where V is a learnable vector and Z is a fixed, randomly initialized orthonormal matrix (i.e. random projections)

the "slow" weights are essentially a residual.

we could "stack" residuals if we wanted higher-order granularity
