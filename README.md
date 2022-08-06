# Home Security

## Description
This repo contains a project using a Raspberry pi, Django and a Tensorflow
pretrained Model to create a local webserver displaying camera footage 
from the raspberry pi. The camera feed is being augmented by the Tensorflow Object detection model. Any recognized objects will be recorded for the time they appear on screen. We can designate what we would like to record through the web app interface. The recordings are saved locally to the Pi and are available to be downloaded on the client side.


## Requirements
### Hardware
- Raspberry pi 4
- OS (or raspberry equivalent):
```
	Distributor ID:	Debian
	Description:	Debian GNU/Linux 11 (bullseye)
	Release:	11
	Codename:	bullseye
```



<img src="https://m.media-amazon.com/images/I/51rQwXKnJSL._AC_SX679_.jpg"
     alt="Raspberry Battery"
     style="float: left; width: 25%; height: 25%; margin-right: 5px;" />
 
- [Battery](https://www.amazon.com/gp/product/B0788B9YGW/ref=ppx_yo_dt_b_asin_image_o01_s00?ie=UTF8&psc=1)


<img src="https://m.media-amazon.com/images/I/61Gx0BEe+oL._AC_SX679_.jpg"
     alt="Raspberry Case"
     style="float: left; width: 25%; height: 25%; margin-right: 5px;" />
 
-[Case](https://www.amazon.com/gp/product/B07WPLDVQJ/ref=ppx_yo_dt_b_asin_image_o09_s00?ie=UTF8&th=1)

<img src="https://m.media-amazon.com/images/I/71J3ZZPHEgL._AC_SX679_.jpg"
     alt="Raspberry Camera"
     style="float: left; width: 25%; height: 25%; margin-right: 5px;" />
 
- [Infared Camera](https://www.amazon.com/dp/B07BK1QZ2L?psc=1&ref=ppx_yo2ov_dt_b_product_details)

### Software
- `curl https://pyenv.run | bash (pyenv installation)`
- python 3.8.8 (we will install with virual penv)
- python3 -m pip install tflite-runtime (we will install in the virtual env)
- django (install into venv)
- opencv-python (install into venv)


