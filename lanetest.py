from pygame import mixer
import cv2 
import numpy as np
import matplotlib.pyplot as plt 
import sys

mixer.init()
mixer.music.load("Resources/park.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()
def cannyfunc(image):
    # --Turning into gray ------------------------------
    gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    # --------------------- Filtering image ------------
    blur = cv2.GaussianBlur(gray,(5,5),0)
    # --------------------- strongest gradient change --
    canny=cv2.Canny(blur,50,150)
    # --------------------------------------------------
    return canny

def region_of_int(image):
    height=image.shape[0]
    # ------------ Setting the traingular area to mask ---------------
    trainglar_area=np.array([[(200,height),(1100,height),(550,250)]])
    mask=np.zeros_like(image)
    cv2.fillPoly(mask,trainglar_area,255)
    image_after_crop=cv2.bitwise_and(image,mask)
    return image_after_crop
def display_lines(image,lines):
    line_image=np.zeros_like(image)
    if lines is not None:
        for line in lines:
            try:
                x1,y1,x2,y2 = line
                cv2.line(line_image,(x1,y1),(x2,y2),(255,255,0),10)
            except:
                print('Finished')
                sys.exit(0)
    return line_image

def  coordinate(image,lines_pam):
    #print(lines_pam)
    try:
        slope , intercept=lines_pam
        y1=image.shape[0]
        y2 = int(y1*(3/5))
        x1 = int((y1-intercept)/slope)
        x2 = int((y2-intercept)/slope)
        return np.array([x1,y1,x2,y2])
    except:
        print('Ended')
        cv2.destroyAllWindows()

    




def averageline(image,lines):
    left_fit=[]
    right_fit=[]
    for line in lines:
        x1,y1,x2,y2=line.reshape(4)
        parameters = np.polyfit((x1,x2),(y1,y2),1)
        slope = parameters[0]
        intercept=parameters[1]
        if slope<0:
            left_fit.append((slope,intercept))
        else:
            right_fit.append((slope,intercept))
    left_fit_avg= np.average(left_fit,axis=0)
    right_fit_avg = np.average(right_fit,axis=0)
    left_line = coordinate(image,left_fit_avg)
    right_line =coordinate(image,right_fit_avg)
    return np.array([left_line,right_line])



# --------------------- Reading image -------------
#laneimage = cv2.imread("Resources/lane.jpg")
# -------------------------------------------------

video = cv2.VideoCapture("Resources/test2.mp4")
while True:
    success, laneimage = video.read()


    copylaneimage=np.copy(laneimage)
    cannyimg=cannyfunc(copylaneimage)

    croppedimg=region_of_int(cannyimg)
    lines =cv2.HoughLinesP(croppedimg,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)
    average_lines = averageline(copylaneimage,lines)
    return_lines = display_lines(copylaneimage,average_lines)

    resultant = cv2.addWeighted(copylaneimage,0.8,return_lines,1,1)
    
    cv2.imshow("Image",resultant)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break