# Open Assistant

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
