# Home Security Object Detection

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
	
	aarch64
	Linux raspberrypi 5.15.32-v8+ #1538 SMP PREEMPT Thu Mar 31 19:40:39 BST 2022 aarch64 GNU/Linux
```

<img src="https://m.media-amazon.com/images/I/81BjdWu7D+L._AC_SX679_.jpg"
     alt="MicroSD with adaptor"
     style="float: left; width: 25%; height: 25%; margin-right: 5px;" />

- [MicroSD with adaptor](https://www.amazon.com/SAMSUNG-Select-microSDXC-Adapter-MB-ME64HA/dp/B08879MG33/ref=sr_1_2?crid=2O7IZ8MNPYOHE&keywords=Samsung’s+64GB+EVO+Select&qid=1659810940&s=electronics&sprefix=samsung+s+64gb+evo+select+%2Celectronics%2C255&sr=1-2)

<img src="https://m.media-amazon.com/images/I/61pj7sQU3qL._AC_SX679_.jpg"
     alt="Raspberry Pi Charger"
     style="float: left; width: 25%; height: 25%; margin-right: 5px;" />

- [Raspberry Pi 4 Model B Official PSU, USB-C, 5.1V, 3A, US Plug, Black SC0218 Pi Accessory (KSA-15E-051300HU)](https://www.amazon.com/gp/product/B07W8XHMJZ/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1)

<img src="https://m.media-amazon.com/images/I/617iRYqu6+L._AC_SX679_.jpg"
     alt="Raspberry Pi"
     style="float: left; width: 25%; height: 25%; margin-right: 5px;" />

- [Raspberry Pi 4 Model B 2019 Quad Core 64 Bit WiFi Bluetooth (4GB)](https://www.amazon.com/gp/product/B07TC2BK1X/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1)

<img src="https://m.media-amazon.com/images/I/71J3ZZPHEgL._AC_SX679_.jpg"
     alt="Raspberry Camera"
     style="float: left; width: 25%; height: 25%; margin-right: 5px;" />
 
- [Infared Camera](https://www.amazon.com/dp/B07BK1QZ2L?psc=1&ref=ppx_yo2ov_dt_b_product_details)


#### Optional Hardware

<img src="https://m.media-amazon.com/images/I/51rQwXKnJSL._AC_SX679_.jpg"
     alt="Raspberry Battery"
     style="float: left; width: 25%; height: 25%; margin-right: 5px;" />
 
- [Battery](https://www.amazon.com/gp/product/B0788B9YGW/ref=ppx_yo_dt_b_asin_image_o01_s00?ie=UTF8&psc=1)


<img src="https://m.media-amazon.com/images/I/61Gx0BEe+oL._AC_SX679_.jpg"
     alt="Raspberry Case"
     style="float: left; width: 25%; height: 25%; margin-right: 5px;" />
 
- [Case](https://www.amazon.com/gp/product/B07WPLDVQJ/ref=ppx_yo_dt_b_asin_image_o09_s00?ie=UTF8&th=1)



### Software
- `curl https://pyenv.run | bash (pyenv installation)`
- python 3.8.8 (we will install with virual penv)
- python3 -m pip install tflite-runtime (we will install in the virtual env)
- django (install into venv)
- opencv-python (install into venv)

# Instalation Guide
- Visit Raspberry Pi website to download an imager for your operating system [Download from here](https://www.raspberrypi.com/software/)
- Once you have done that you can insert the sd card into your computer and launch the application

<img src="https://assets.raspberrypi.com/static/md-bfd602be71b2c1099b91877aed3b41f0.png"
     alt="Installing OS"
     style="float: left; width: 25%; height: 25%; margin-right: 5px;" />

- Click on Choose storage and select your microsd
