import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
image = cv2.imread("Resources/Back.png")
# -------------------- importing a video ---------------
"""
video = cv2.VideoCapture("Resources/vid.mp4")
while True:
    success, image = video.read()
    cv2.imshow("Video",image)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
"""

# ----------------------- Webcam ----------------------------
"""
webcame=cv2.VideoCapture(0)
# ------- setting width and height of the screen--------------
webcame.set(3,640)
webcame.set(4,480)
# ------------------------- set brightness -------------------
webcam.set(10,100)
--------------------------------------------------------------
while True:
    success, webcamimage=webcame.read()
    cv2.imshow("Webcam",webcamimage)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break

"""


#--------------------- Generate Gray tone image --------------
""" 
imageGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",imageGray)
cv2.waitKey(0)
"""

# --------------------   Blur image  -------------------------
"""
imageBlur = cv2.GaussianBlur(image,(3,3),0)
cv2.imshow("Blur Image",imageBlur)
cv2.waitKey(0)
"""
# -------------------- Canny Image ---------------------------
"""
imageCanny = cv2.Canny(image,100,110)
cv2.imshow("Canny",imageCanny)
cv2.waitKey(0)
"""
# --------------------  Dialated image -------------------
"""
imageCanny=cv2.Canny(image,100,150)
imageDialation = cv2.dilate(imageCanny,kernel,iterations=1)
cv2.imshow("Dialation",imageDialation)
cv2.waitKey(0)
"""

# --------------------- Erosion -------------------------
"""
imageCanny=cv2.Canny(image,100,150)
imageDialation = cv2.dilate(imageCanny,kernel,iterations=1)
imageeroted = cv2.erode(image,kernel,iterations=3)
cv2.imshow("Eroted",imageeroted)
cv2.waitKey(0)
"""

