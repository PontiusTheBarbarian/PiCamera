# https://picamera.readthedocs.io/en/release-1.13/recipes1.html#recording-video-to-a-file 

import picamera

print("Recording started!")
camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.start_recording('my_video.h264')
camera.wait_recording(60)
camera.stop_recording()
print("Recording finished.")
camera.stop_preview()
camera.close()