import cv2
import numpy as np

img=cv2.imread(r"C:\Users\Mr-SWIFT\Downloads\download (3).png")
cv2.imshow("image show",img)
cv2.waitKey(0)

imgG=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(img,(7,7),3)#The kernels will define the size of the convolution, the weights applied to it, and an anchor point usually positioned at the center.
#So in a 3x3 matrix, each pixel is affected only by the pixels around it, wherein a 7x7 farther pixels would change it.
imgCanny=cv2.Canny(img,100,100)
#define contours for shapes border are highlights
#---------------------------------------------------------------------------------------------------------------------------------------#
#What is Hierarchy?
#Normally we use the cv.findContours() function to detect objects in an image, right ?
#Sometimes objects are in different locations. But in some cases, some shapes are inside other shapes.
#Just like nested figures. In this case, we call outer one as parent and inner one as child. This way, 
#contours in an image has some relationship to each other. And we can specify how one contour is connected to each other, 
#like, is it child of some other contour, or is it a parent etc. Representation of this relationship is called the Hierarchy.

#Contour Retrieval Mode
#1. RETR_LIST
#This is the simplest of the four flags (from explanation point of view). 
#It simply retrieves all the contours, but doesn't create any parent-child relationship.
#Parents and kids are equal under this rule,
#and they are just contours. ie they all belongs to same hierarchy level.

#2. RETR_EXTERNAL
#If you use this flag, it returns only extreme outer flags.
#Only the eldest in every family is taken care of.
#It doesn't care about other members of the family :).

#3.RETR_CCOMP
#This flag retrieves all the contours and arranges them to a 2-level hierarchy.
#ie external contours of the object (ie its boundary) are placed in hierarchy-1. 
#And the contours of holes inside object (if any) is placed in hierarchy-2. 
#If any object inside it, its contour is placed again in hierarchy-1 only. 
#And its hole in hierarchy-2 and so on.
#
#4.RETR_TREE
#And this is the final guy, Mr.Perfect.
#It retrieves all the contours and creates a full family hierarchy list.
#It even tells, who is the grandpa, father, son, grandson and even beyond... :).
#--------------------------------------------------------------------------------------------------------------------------------------------------#

def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)

        if area>0:

            cv2.drawContours(conimg,cnt,-1,(255,0,0),3)#-1 is for all the shape we want contours
            perimeter=cv2.arcLength(cnt,True)
            print(perimeter)
            approx=cv2.approxPolyDP(cnt,0.02*perimeter,True,)
            print(approx)
            objCor=len(approx)
            x,y,w,h=cv2.boundingRect(cnt)
            cv2.rectangle(conimg,(x,y),(x+w,y+h),(0,245,5),3)   

        if objCor ==3: objectType='Tri'
        elseif:objCor==4: objectType=='square'
        else:objectType='None'
        cv2.putText(conimg,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
           
#Above, we told that contours are the boundaries of a shape with same intensity. 
#It stores the (x,y) coordinates of the boundary of a shape.
#But does it store all the coordinates ?
#That is specified by this contour approximation method.
#If you pass cv.CHAIN_APPROX_NONE, all the boundary points are stored. 
#But actually do we need all the points? For eg, you found the contour of a straight line.
#Do you need all the points on the line to represent that line?
#No, we need just two end points of that line. 
#This is what cv.CHAIN_APPROX_SIMPLE does.
#It removes all redundant points and compresses the contour, thereby saving memory.
#Below image of a rectangle demonstrate this technique. 
#Just draw a circle on all the coordinates in the contour array (drawn in blue color). 
#First image shows points I got with cv.CHAIN_APPROX_NONE (734 points) and second image shows the one with cv.CHAIN_APPROX_SIMPLE (only 4 points). 
#See, how much memory it saves!!!









conimg=img.copy()
getContours(imgCanny)
cv2.imshow('contour image',conimg)
cv2.imshow("Grey Image",imgG)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Edges Image",imgCanny)
cv2.waitKey(0)