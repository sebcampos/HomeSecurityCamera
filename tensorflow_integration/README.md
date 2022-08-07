# Tensorflow + OpenCV
## Enable Camera support
First and formost a big thanks to this repository:

https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/

This is where all the code and logic for implementing a tflite object detection module with opencv comes from.

First we will need to enable the camera for Raspberry Pi
Run the following command in the terminal and you will see a window like so

`sudo raspi-config`

The terminal will display a interface, use the arrow keys to navigate to the `Interface Options` option and hit `Enter`

![raspi-config](../static/raspi-config.png)

Then, select enable Legacy Camera support

![enable-camera1](../static/enable-legacy-camera-support1)

![enable-camera2](../static/enable-legacy-camera-support2)


Finnaly reboot and we are ready to test the camera!

## Test Camera
Using the following command you can download a python file from this repo to test your camera
You can run it by calling the command `python <name_of_file>` to close the camera press the `q` key

```
wget https://raw.githubusercontent.com/sebcampos/HomeSecurityCamera/master/tensorflow_integration/video_capture_test.py
```
