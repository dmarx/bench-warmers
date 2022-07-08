# Inverse Heat Dissipation Model with FlexConvs

* IHDM - https://arxiv.org/abs/2206.13397
* FlexConv - https://arxiv.org/abs/2110.08059

From FelxConv:

>  Intuitively, multiplication with the mask **blurs in the frequency domain**, as it is equivalent to convolution with the Fourier transform of the mask

Feel like this would pair nicely with IHDM since that's basically exactly the process that's being modeled

I think the CKConv repo has FlexConv? https://github.com/dwromero/ckconv

---

In FlexConv, they regularize the kernels highest frequency to mitigate aliasing, but I feel like they could take this a step further by applying a temperature/schedule to this regularization, starting at a frequency lower than the nyquist frequency to produce a low resolution kernel, than increasing the highest allowed frequency up to nyquist as learning progresses, so the learning momentum is encouraged to identify a direction that sharpens the kernel resolution as learning progresses
