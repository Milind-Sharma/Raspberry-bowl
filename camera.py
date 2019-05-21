from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180
camera.start_preview(alpha=215)
sleep(10)
camera.stop_preview()
