import cv2
import numpy as np

location ="Resources/a.jpg"
def empty(i):
    pass
cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar",640,240)
cv2.createTrackbar("min Hue","Trackbar",0,179,empty)
cv2.createTrackbar("max Hue","Trackbar",179,179,empty)
cv2.createTrackbar("saturation Min","Trackbar",0,255,empty)
cv2.createTrackbar("saturation Max","Trackbar",255,255,empty)
cv2.createTrackbar("Value min","Trackbar",0,255,empty)
cv2.createTrackbar("value max","Trackbar",255,255,empty)
while True:
    image=cv2.imread(location)
    imagehsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    hminimum =cv2.getTrackbarPos("min Hue","Trackbar")
    hmaximum =cv2.getTrackbarPos("max Hue","Trackbar")
    saturation_minimum =cv2.getTrackbarPos("saturation Min","Trackbar")
    saturation_Maximum = cv2.getTrackbarPos("saturation Max","Trackbar")
    value_minimum = cv2.getTrackbarPos("Value min","Trackbar")
    value_Maximum = cv2.getTrackbarPos("value max","Trackbar")


    #5print(hminimum,hmaximum,saturation_minimum,saturation_Maximum,value_minimum,value_Maximum)
    lower = np.array([hminimum,saturation_minimum,value_minimum])
    upper = np.array([hmaximum,saturation_Maximum,value_Maximum])
    mask = cv2.inRange(imagehsv,lower,upper)
    resultImage = cv2.bitwise_and(image,image,mask=mask)
    cv2.imshow("image",resultImage)
    cv2.waitKey(1)