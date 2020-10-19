import cv2
import numpy as np
width,height = 250,350
image=cv2.imread("Resources/a.jpg")
# --------------------------------- Birds eye view ---------------------
"""
points = np.float32([[111,219],[287,188],[154,482],[352,440]])
points2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(points,points2)
outputimage=cv2.warpPerspective(image,matrix,(width,height))
cv2.imshow("Image",outputimage)
cv2.waitKey(0)
"""
# --------------------------------- Stacking image horizontally ---------
"""
horizontal = np.hstack((image,image))
cv2.imshow("Join",horizontal)
cv2.waitKey(0)
# ---------------------------------- Stacking image vertically -----------

vertical = np.hstack((image,image))
cv2.imshow("Join",vertical)
cv2.waitKey(0)
"""
