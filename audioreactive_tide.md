# audioreactive tide

![](https://img.shields.io/badge/tag-animation-lightgrey)
![](https://img.shields.io/badge/tag-experimental-lightgrey)
![](https://img.shields.io/badge/tag-publication-lightgrey)

---

COMPLETED: https://twitter.com/DigThatData/status/1628633830616862720

Made with https://colab.research.google.com/github/dmarx/notebooks/blob/main/Stable_Diffusion_KLMC2_Animation.ipynb

supplemental 

```python
tide_audio_url = 'https://archive.org/download/aporee_9627_11535/110403zoom001.mp3'
!wget {tide_audio_url}

fname = '110403zoom001.mp3'
y, sr = librosa.load(fname)

flatness = librosa.feature.spectral_flatness(y)[0]
rms = librosa.feature.rms(y)[0]

tide_strength = flatness*rms
tide_fps = 43.2

###############

from scipy.signal import decimate
q=3
tide_slower = decimate(tide_strength, q) 

plt.figure(figsize=(30,10))
plt.plot(tide_slower)
slower_fps = tide_fps / q

min(tide_slower), max(tide_slower)
min_h, max_h = .05, .2
#tide_slow_shifted = tide_slower*(max_h-min_h) + min_h
tide_slower_normed = (tide_slower-min(tide_slower)) / max(tide_slower)
tide_slower_shifted = tide_slower_normed*(max_h-min_h) + min_h
plt.plot(tide_slower_shifted[:500])
#plt.plot(tide_slower_normed)

from scipy.signal import savgol_filter

smoothed = savgol_filter(tide_slower_shifted, window_length=15, polyorder=2)
plt.plot(smoothed[:500])


#dydx = smoothed[1:501] - smoothed[0:500]
dydx = smoothed[1:] - smoothed[:-1]
#plt.plot(((dydx**2)/2e-5)[:500])
#plt.plot((dydx)**2, color=['g' if (v > .1)  else 'b' for v in (dydx**2)])
#plt.plot([1 if (v>2e-5) else 0 for v in (dydx**2)[:500]])

dydx_smoothed = savgol_filter(dydx, window_length=51, polyorder=2)

s = np.sign(dydx_smoothed)
#sign_change = s[1:500] > s[:499]
sign_change = (s[1:] == 1 ) & (s[:-1] == -1)
inv_sign_change = (s[1:] == -1 ) & (s[:-1] == 1)
plt.plot(sign_change[:500])
plt.plot(inv_sign_change[:500])


# prompt transition: signchange to inverse signchange (orange to green)
# prompt stable but step still changing from inv to change (green to orange)
# so orange->green is every transition, so each prompt is orange->green in, orange->green out

sign_changes = np.where(sign_change)[0]
inv_sign_changes = np.where(inv_sign_change)[0]

# we want to start our "count" on an orange, so we need to adjust if green comes before orange
if sign_changes[0] > inv_sign_changes[0]:
  sign_changes = sign_changes[:-1]
  inv_sign_changes = inv_sign_changes[1:]

sign_changes[0], inv_sign_changes[0]

transitions = list(zip(sign_changes, inv_sign_changes))
```

```python
flowers = [
    'rose',
    'carnation',
    'tulip',
    'orchid',
    'sunflower',
    'snapdragon',
    "baby's breath",
    "lily",
    'dahlia',
    'poppy',
    'geranium',
]

import random

def pick_flower():
    return random.choice(flowers)

flower_seq = [pick_flower()]
while len(flower_seq) < len(transitions) + 1:
  curr_flower = pick_flower()
  if curr_flower != flower_seq[-1]:
    flower_seq.append(curr_flower)
    
###

#from itertools import pairwise
from itertools import tee

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


low, hi = 0.001, 1
schedules = [{in_[0]:low, in_[1]:hi, out_[0]:hi, out_[1]:low} for in_, out_ in list(pairwise(transitions))]
list(zip(flower_seq, schedules))

###

prompt_params = [(f"a beautiful bouquet of {flower} flowers", sched) for flower, sched in list(zip(flower_seq, schedules))]
prompt_params = [("a beautiful bouquet of roses", {0:1, 40:1, 69:0})] + prompt_params

negative_prompts = [
    ["watermark text", {0:-0.3} ],
     ["jpeg artifacts", {0:-0.1} ],
     ["artist's signature", {0:-0.1}]
]

prompts_params = prompt_params + negative_prompts

h = {i:v for i,v in enumerate(tide_slower_shifted)}

###


    
    
```



---

sync periodicity of an animation to audio of rolling ocean waves crashing

here's some decent "ocean waves" audio: 

* https://archive.org/details/aporee_9627_11535 - probably best
* https://archive.org/details/aporee_5762_7243 - not bad
* https://www.youtube.com/watch?v=rF5b60TabiI - this one might be the winner
* https://www.youtube.com/watch?v=k4WmQwUXK7k - another strong competitor
