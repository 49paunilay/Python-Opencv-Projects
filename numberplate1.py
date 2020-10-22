import cv2
import numpy as np
webcam = cv2.VideoCapture(0)
webcam.set(3,640)
webcam.set(4,480)
webcam.set(10,100)
marea =400
count=0
face_cascade = cv2.CascadeClassifier('Resources/haarcascades/haarcascade_russian_plate_number.xml')
while True:
    ret, frame = webcam.read()
    imageGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    plates = face_cascade.detectMultiScale(imageGray, 1.3, 5)
    for (x,y,w,h) in plates:
        if (w*h)>marea:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame,"This is number Plate",(x,y+5),cv2.FONT_ITALIC,3,(0,255,255),2)
            numberplateimage=frame[y:y+h,x:x+w]
            cv2.imshow("The number Plate",numberplateimage)
    cv2.imshow("Webcam",frame)
    if cv2.waitKey(1) & 0xff==ord('s'):
        count+=1
        cv2.imwrite('Resources'+str(count)+'.jpg',imageRegionofInterest)
        cv2.rectangle(webcamimage,(0,200),(640,300),(0,255,255),cv2.FILLED)
        cv2.putText(webcamimage,"Saved",(150,265),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255),1)
        cv2.imshow("Result",webcamimage)
        cv2.waitKey(100)


