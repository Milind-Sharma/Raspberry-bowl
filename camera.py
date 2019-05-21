from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180               //to rotate the camera if the preview is upside-down
camera.start_preview(alpha=215)
sleep(10)                           //to turn off the preview after this time
camera.stop_preview()
