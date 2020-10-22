import cv2
import numpy as np


face_cascade = cv2.CascadeClassifier('Resources/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Resources/haarcascades/haarcascade_eye.xml')

count=0
webcam = cv2.VideoCapture(0)
while True:
    ret, frame = webcam.read()
    actimage=frame
    imageGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(imageGray, 1.3, 5)
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(imageGray,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = imageGray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.imshow('img',frame)
    if cv2.waitKey(1) & 0xff==ord('s'):
        count+=1
        cv2.imwrite('Resources'+str(count)+'.jpg',frame)
        cv2.rectangle(frame,(0,200),(640,300),(0,255,255),cv2.FILLED)
        cv2.putText(frame,"Saved",(150,265),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255),1)
        cv2.imshow("Result",frame)
        cv2.waitKey(100)

