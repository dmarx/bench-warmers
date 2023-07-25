# checkpoint-to-LoRA

labels: experimental, tooling

1. subtract checkpoint from base model to get delta weights
2. SVD the delta weights
3. that's it, we're done.

even if this is lossy, it might still be a good way to "warm start" LoRA training with a strong but noisy (i.e. low rank) prior

---

Looks like LoCON does this already? https://github.com/KohakuBlueleaf/LyCORIS
