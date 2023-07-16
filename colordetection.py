import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow('TrackBars') #trackbar we will crete for the control the HSV 
cv2.resizeWindow('TrackBars',640,240) #640 and 240 is size and height of the trackbar

cv2.createTrackbar('Hue Min','TrackBars',0,179,empty) #In create trackbar we first put trackbar name that is Hue then enter the window name where we have to use Hue then enter the min and max value of hue and last enter the empty funtion that pass the hue
#Hue maximum value is 360 but in OPEN CV HUE max value is 179
cv2.createTrackbar('Hue Max','TrackBars',179,179,empty)
cv2.createTrackbar('Sat Min','TrackBars',0,255,empty)
cv2.createTrackbar('Sat Max','TrackBars',255,255,empty)
cv2.createTrackbar('Val Min','TrackBars',0,255,empty)
cv2.createTrackbar('Val Max','TrackBars',255,255,empty)

 
img=cv2.imread(r"C:\Users\Mr-SWIFT\Downloads\download (1).jfif")
cv2.imshow('Original Car Image',img)
cv2.waitKey(0)
while True:#we use while loop bcz we want trackbar in loop 

    #Convert the image into HSV 
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #we use gettrackbarpos for change the trackbar value in realtime
    h_min=cv2.getTrackbarPos("Hue Min",'TrackBars')
    h_max=cv2.getTrackbarPos("Hue Max",'TrackBars')
    s_min=cv2.getTrackbarPos("Sat Min",'TrackBars')
    s_max=cv2.getTrackbarPos("Sat Max",'TrackBars')
    v_min=cv2.getTrackbarPos("Val Min",'TrackBars')
    v_max=cv2.getTrackbarPos("Val Max",'TrackBars')
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)#inrnage function help us to move our array in min to max value 
    ogImg=cv2.bitwise_and(img,img,mask=mask)#we use bitwiseand bcz we want a color image of car and control the car image with the trackbar

    cv2.imshow('Mask image',mask)
    cv2.imshow('Original image color detection',ogImg)


    cv2.imshow('HSV Image',imgHSV)
    cv2.waitKey(1)