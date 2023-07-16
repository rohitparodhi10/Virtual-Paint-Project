import cv2#for use of open computer vision functions
import numpy as np# for use numerical operations

frameWidth=480#we set the camera width 
frameHeight=480#we set the camera height
capture=cv2.VideoCapture(0)#videoCapture is to detect the web cam or camera and detect the object
#give arugument 0 bcz we have only one camera and also we use webcam
capture.set(3, frameWidth)#call frameWidth(3 is nothing but an sequence)
capture.set(4, frameHeight)#call frameHeight
capture.set(10,180)#use for brightness

myColors=[[5,107,0,236,80,100],#orange color(starting 3 values are min og HSV and Last 3 are max of HSV)
          [133,56,0,159,156,255],#purple color
          [57,76,0,100,255,255]]#green color

myColorValues=[[51,153,255],
               [255,0,255],
               [0,255,0]]
myPoints=[]

def findColor(video,myColors,myColorValues):#define the function findcolor and give the argument video and myColors
    videoHSV=cv2.cvtColor(video,cv2.COLOR_BGR2HSV)#convert video in HSV
    count=0
    newPoints=[]
    for color in myColors:#use for condition and assign color to myColors
        lower=np.array(color[0:3])#set the lower HSV
        upper=np.array(color[3:6])#set the higher HSV
        mask=cv2.inRange(videoHSV,lower,upper)#use range for live value changes and we call videoHSV(use for convert video into HSV),lower and upper HSV
        #cv2.imshow(str(color[0]),mask)
        x,y=getContours(mask)
        cv2.circle(videocon,(x,y),15,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
    return newPoints    

def getContours(video):#define the function name with getCountours and pass thee argument video
    contours,hierarchy=cv2.findContours(video,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:#use for loop for we want contours work in loop
        area=cv2.contourArea(cnt)#we set the contourArea for compute(count) the object
        if area>500:#put if condition 
            cv2.drawContours(videocon,cnt,-1,(255,0,0),3)#draw contours is for draw the contours
            #-1 is for all the shape we want contours
            #perimeter=cv2.arcLength(cnt,True)
            #approx=cv2.approxPolyDP(cnt,0.02*perimeter,True,)
            x,y,w,h=cv2.boundingRect(cnt)#used for draw exact rectangle where object is located
    return x+w//2,y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(videocon,(point[0],point[1]),15,myColorValues[point[2]],cv2.FILLED)



while True:#use while loop for work code in loop
    success, video=capture.read()#call the videocapture 
    videocon=video.copy()#create the copy video for contours
    newPoints=findColor(video,myColors,myColorValues)#call the def function findColor
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)
    #cv2.imshow("Camera Is Open",video)#show the video i.e videocapture i.e open the camera
    cv2.imshow("Contour Video",videocon)#show the contours video

    if cv2.waitKey(1)==ord('q'):#use waitKey for wait and ord is used for return the unicode (q=113)
        break
            