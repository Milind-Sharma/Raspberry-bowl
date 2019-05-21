from picamera import PiCamera
from time import sleep

camera = PiCamera()

#for normal video
camera.rotation = 180               #to rotate the camera if the preview is upside-down
camera.start_preview(alpha=215)     #alpha is used to adjust the transparency of the preview.range= 0-255.
sleep(10)                           #to turn off the preview after this time
camera.stop_preview()

#for capturing a photo
camera.start_preview(alpha=200)
sleep(2)
camera.capture('/home/pi/Desktop/Raspberry/single_photo/image.jpg') #storing the captured photo in the destination with name image.jpg
camera.stop_preview()

#for capturing multiple photos
camera.start_preview(alpha=200)
for i in range(3):                #for clicking multiple photos
    sleep(2)
    camera.capture('/home/pi/Desktop/Raspberry/loop_photos/image%s.jpg' % i)
camera.stop_preview()

#for recording a video
camera.start_preview(alpha=200)
camera.start_recording('/home/pi/Desktop/Raspberry/videos/videos.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()
