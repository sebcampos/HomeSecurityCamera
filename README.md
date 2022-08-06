# Home Security

## Description
This repo contains a project using a Raspberry pi, Django and a Tensorflow
pretrained Model to create a local webserver displaying camera footage 
from the raspberry pi. The camera feed is being augmented by the Tensorflow Object detection model. Any recognized objects will be recorded for the time they appear on screen. We can designate what we would like to record through the web app interface. The recordings are saved locally to the Pi and are available to be downloaded on the client side.


## Requirements
### Hardware
- Raspberry pi 4
- OS (or raspberry equivalent): 
	Distributor ID:	Debian
	Description:	Debian GNU/Linux 11 (bullseye)
	Release:	11
	Codename:	bullseye

### Software
- `curl https://pyenv.run | bash (pyenv installation)`
- python 3.8.8 (we will install with virual penv)
- python3 -m pip install tflite-runtime (we will install in the virtual env)
- django (install into venv)
- opencv-python (install into venv)


