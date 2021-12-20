from picamera import PiCamera
import time
from datetime import datetime

class MyCamera:
    def __init__(self, timeStump: str) :
        camera=PiCamera()
        camera.start_preview()

        time.sleep(2)

        output_path = '/home/pi/Source/TetraWatch/data/'

        camera.capture(output_path + timeStump + '.jpg')
        camera.stop_preview()