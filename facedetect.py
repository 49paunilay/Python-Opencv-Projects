import cv2

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
image=cv2.imread("Resources/a.jpg")
imagegray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imagegray,1.1,4)
for (x,y,width,height) in faces:
    print('here')
    cv2.rectangle(image,(x,y),(x+width,y+height),(0,255,255),2)
cv2.imshow("Image",image)
cv2.waitKey(0)