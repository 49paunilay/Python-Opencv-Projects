import cv2
import numpy as np

image=np.zeros((512,512,3),np.uint8)
#  -------------------------     colouring the image --------------------------
#image[:] = 255,0,0
#-----------------------------------------------------------------------------
# ----------------------------  drawing a diagonal line -----------------------
"""
cv2.line(image,(0,0),(512,512),(0,255,255),2)
cv2.imshow("Image",image)
cv2.waitKey(0)
"""
# ----------------------------- Drawing a rectangle ---------------------------
"""
cv2.rectangle(image,(0,0),(350,350),(0,0,255),cv2.FILLED)
cv2.imshow("rectangle",image)
cv2.waitKey(0)

# for normal image
importedimage = cv2.imread("Resources/a.jpg")
cv2.rectangle(importedimage,(190,195),(300,350),(0,220,120),3)
cv2.imshow("image",importedimage)
cv2.waitKey(0)
"""

# ------------------------------ Drawing a rectangle ---------------------------
"""
cv2.circle(image,(250,250),50,(0,244,211),5)
cv2.imshow("Image",image)
cv2.waitKey(0)
"""
# ------------------------------ Adding text on image -----------------------
"""
cv2.putText(image,"This is great",(100,100),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(0,150,155),4)
cv2.imshow("Text",image)
cv2.waitKey(0)
"""
