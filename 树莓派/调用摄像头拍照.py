from picamera import PiCamera
from time import sleep

camera=PiCamera()

camera.rotation =180
camera.start_preview()
sleep(5)
camera.capture('image.jpg')  #图片保存的位置
camera.stop_preview()