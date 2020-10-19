import cv2
import numpy as np

webcame=cv2.VideoCapture(0)
# ------- setting width and height of the screen--------------
webcame.set(3,640)
webcame.set(4,480)
# ------------------------- set brightness -------------------
webcame.set(10,100)
mycolours=[[5,107,0,19,255,255],[133,56,0,159,156,255],[57,76,0,100,255,255]]
mycolourvalues=[[51,153,255],[255,0,255],[0,255,0]]
mypoints = []
 #[x,y,colorIndex]

def drawonCanvas(points,mycolourvalues):
    for point in points:
        cv2.circle(imageResult,(point[0],point[1]),10,mycolourvalues[point[2]],cv2.FILLED)


def getColor(image,mycolours,mycolourvalues):
    imagehsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    count=0
    newpoint=[]
    for color in mycolours:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imagehsv,lower,upper)
        x,y=getContours(mask)
        cv2.circle(imageResult,(x,y),10,mycolourvalues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newpoint.append([x,y,count])
        count+=1
        #cv2.imshow(str(color[0]),mask)
    return newpoint
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imageResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
        
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y

while True:
    success, webcamimage=webcame.read()
    imageResult=webcamimage.copy()
    newpoints=getColor(webcamimage,mycolours,mycolourvalues)
    if len(newpoints)!=0:
        for newpoint in newpoints:
            mypoints.append(newpoint)
    if len(mypoints)!=0:
        drawonCanvas(mypoints,mycolourvalues)
    cv2.imshow("Webcam",imageResult)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break

