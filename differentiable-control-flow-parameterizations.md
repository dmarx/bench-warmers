# differentiable control flow parameterizations

control flow structures that are *tunable* via gradient descent. not just that we can backprop through them, but we can *fit* them.

## loop

```
a0 = 1 = starting value (no reason we need three degrees of freedom when two will do the job)
b = decay rate
c = threshold

x = a0
while x > c:
   ... # do a thing to be looped over
   x = decay(x,b)
```

fitting `b` and `c` is equivalent to calibrating the duration of a for loop

## if-then

```
a = 'then' outcome 
b = 'else' outcome
k = sigmoid params


s = sigmoid(x, k)
x = (1-s)*a + (s)*b
```

lerping the sigmoid outputs approximates lerping when s is 0 or 1, which is identical to a conditional
