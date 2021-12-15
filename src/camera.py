from picamera import PiCamera
from time import sleep

class MyCamera:
    def __init__(self) :
        camera=PiCamera()
        camera.start_preview()