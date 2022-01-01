# https://picamera.readthedocs.io/en/release-1.13/recipes1.html#capturing-to-a-file

from time import sleep
from picamera import PiCamera
from datetime import datetime

now = datetime.now().strftime("%Y_%m_%d-%H%M%S")

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture("photo_" + now + ".jpg")
camera.stop_preview()
camera.close()