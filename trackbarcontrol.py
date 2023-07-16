import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow('TrackBar')
cv2.resizeWindow('TrackBar',640,240)

cv2.createTrackbar('Hue_Min',"TrackBar",0,179,empty)
cv2.createTrackbar('Hue_Max','TrackBar',179,179,empty)
cv2.createTrackbar("Sat_Min","TrackBar",0,255,empty)
cv2.createTrackbar('Sat_Max','TrackBar',255,255,empty)
cv2.createTrackbar('Value_Min',"TrackBar",0,255,empty)
cv2.createTrackbar('Value_Max',"TrackBar",255,255,empty)

img=cv2.imread(r'C:\Users\Mr-SWIFT\Downloads\Felis_silvestris_silvestris_small_gradual_decrease_of_quality.png')
imgr=cv2.resize(img,(150,150))
#cv2.imshow("The Image",img)
cv2.waitKey(0)

while True:

    imgHSV=cv2.cvtColor(imgr,cv2.COLOR_BGR2HSV)
    
    Hue_Min=cv2.getTrackbarPos('Hue_Min',"TrackBar")
    Hue_Max=cv2.getTrackbarPos('Hue_Max',"TrackBar")
    Sat_Min=cv2.getTrackbarPos('Sat_Min',"TrackBar")
    Sat_Max=cv2.getTrackbarPos('Sat_Max',"TrackBar")
    Value_Min=cv2.getTrackbarPos('Value_Min',"TrackBar")
    Value_Max=cv2.getTrackbarPos('Value_Max',"TrackBar")

    print(Hue_Min,Hue_Max,Sat_Min,Sat_Max,Value_Min,Value_Max)
    lower=np.array([Hue_Min,Sat_Min,Value_Min])
    upper=np.array([Hue_Max,Sat_Max,Value_Max])
    mask=cv2.inRange(imgHSV,lower,upper)
    finalimage=cv2.bitwise_and(imgr,imgHSV,mask=mask)

    cv2.imshow("HSV Image",imgHSV)
    cv2.imshow("Final Image",finalimage)
    cv2.waitKey(1)