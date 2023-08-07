# Open Assistant

![](https://img.shields.io/badge/tag-wip-lightgrey)
![](https://img.shields.io/badge/tag-publicgood-lightgrey)
![](https://img.shields.io/badge/tag-accessibility-lightgrey)
![](https://img.shields.io/badge/tag-stability-lightgrey)

lol I bet I saw the LAION thing and forgot it wasn't my own idea, even the name... whoops. what can I say: I sometimes brainstorm on cannabis. 

https://projects.laion.ai/Open-Assistant/

---

open source "alexa"

i'm sure this already exists or is in progress, but it feels like such a simple project i just think it'll be fun to spin up my own from scratch.

# requirements

* runs on an rpi
  * can be a client that connects to a separately hosted server that's still accessible on the network
* supports microphone input
* TTS input
* STT output
* custom trigger word
* intent classifier. start with simple "please" intent, which emits an interaction with chatgpt
* slot filler, start with naive slot that just performs an identity mapping of the transcription to send to chatgpt
