import cv2
import numpy as np

image = cv2.imread("Resources/a.jpg")
print(image.shape)
# ---------------------- Image Resizing -----------
"""
imageResized=cv2.resize(image,(300,300))
cv2.imshow("Image",image)
cv2.imshow("Resized Image",imageResized)
cv2.waitKey(0)
"""
# --------------------- Cropping -----------------
"""
imagecropped = image[50:300,200:400]
cv2.imshow("cropped image",imagecropped)
cv2.waitKey(0)
"""
