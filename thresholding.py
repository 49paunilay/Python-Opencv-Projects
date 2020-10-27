import cv2
import numpy as np

image = cv2.imread("Resources/shape.jpg")
success, threshold = cv2.threshold(image,30,255,cv2.THRESH_BINARY_INV)

cv2.imshow("Image",threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()