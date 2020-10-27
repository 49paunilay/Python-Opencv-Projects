import cv2
import numpy as np

image = cv2.imread("Resources/shape.jpg",cv2.IMREAD_GRAYSCALE)

_,th1=cv2.threshold(image,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow("Image",th2)
cv2.waitKey(0)
cv2.destroyAllWindows()