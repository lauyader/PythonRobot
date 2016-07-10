from SimpleCV import *
import time
#cam = Camera()
cam = Camera(1, {"width":640, "height":480})
while True:
    img = cam.getImage()
    img.save("prueba2.png")
    time.sleep(1) 
