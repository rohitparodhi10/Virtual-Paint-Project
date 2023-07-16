import cv2
import numpy as np
import matplotlib.pyplot as plt


#FOR READ IMAGE
img=cv2.imread(r"C:\Users\Mr-SWIFT\Downloads\img.jfif") #for read the image that we have to use
cv2.imshow('image',img) #for show image
cv2.waitKey(0) #for dealy 
#--------------------------------------------------------------#
#CONVERT IMAGE INTO GREY
imgG=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #cvtColor method is used for convert one color to another color
cv2.imshow('grey image',imgG)
cv2.waitKey(0)
#---------------------------------------------------------------#
#FOR BLUR IMAGE
imgBlur=cv2.GaussianBlur(imgG,(7,7),0)#7,7 is the kernal size 
cv2.imshow("blur image",imgBlur)
cv2.waitKey(0)
#----------------------------------------------------------------#
#FOR THE EDGES OF IMAGE
imgEdges=cv2.Canny(imgG,100,100) #100,100 is the how deep we have to see our image #canny function is use to show the edges of image #o extract useful structural information from different vision objects and dramatically reduce the amount of data to be processed.
cv2.imshow("Edges of image",imgEdges)
cv2.waitKey(0) 
#----------------------------------------------------------------#
#FOR THE THICKNESS OF EDGES
imgDilation=cv2.dilate(imgEdges,(10,10))
cv2.imshow("Dilation of image",imgDilation)
cv2.waitKey(0)
#-----------------------------------------------------------------#
imgErode=cv2.erode(imgEdges,(1,1)) #the areas of dark regions grow in size and bright regions reduce. 
#For example, the size of an object in dark shade or black shade increases, 
#while it decreases in white shade or bright shade.
cv2.imshow("Erode of image",imgErode)
cv2.waitKey(0)
#------------------------------------------------------------------#
#resize the image & Crop Image
#firstly we find dthe real size of the image, for that we use shape 
print(img.shape)#shape is (168,300,3) where 168 is height 300 width and 3 is BGR 
#for resize we use 
imgResize=cv2.resize(img,(120,150))
cv2.imshow('resize image',imgResize)
cv2.waitKey(0)
#for image croping we use give directly dimension for crop part
imgCrop=img[0:200,200:400]
cv2.imshow('crop image',imgCrop)
cv2.waitKey(0)
#-------------------------------------------------------------------#
#Color and makes the shape on image
#Here i crete the new image with same color and draw the shape on that
imgNew=np.zeros((512,512,3),np.uint8)
#if we want to color whole image with diffrent color then we use[:-colun is for whole area]
imgNew[:]=0,255,2
#but if we have to color specific part of the image then we have to give the dimension's
imgNew[0:200,200:400]=0,155,0
#for draw the shape on image we will use cv2 line function
cv2.line(imgNew,(0,0),(500,600),(0,135,3),8)
cv2.rectangle(imgNew,(1,3),(300,400),(0,123,3),9,cv2.FILLED)
cv2.circle(imgNew,(400,500),40,(0,145,8),10)
cv2.putText(imgNew,"This is My OPEN CV Program",(200,400),cv2.FONT_HERSHEY_SIMPLEX,2,(0,156,8),9)
#when we dont know about image width start point and end point then do this
#cv2.line(imgNew,(imgNew.shape[1],imgNew.shape[0]),(0,412,0))
cv2.imshow('new color image',imgNew)
cv2.waitKey(0)
#-------------------------------------------------------------------#
#WORD PERSPECTIVE
imgCard=cv2.imread(r'C:\Users\Mr-SWIFT\Downloads\51XsBrbfl5L._SY355_.jpg')
cv2.imshow('Image of card',imgCard)
cv2.waitKey(0)
width,height=250,350 #[Universal size of cards 250inch(Height)and 350inch (width)]
pt1=np.float32([[231,81],[342,141],[152,238],[261,292]]) #for the values open paint and drag the image in paint and move the cursor on the corrner after that we wil get the image values
pt2=np.float32([[0,0],[width,0],[0,height],[width,height]]) #pt2 shows values from which direction like first value from width and height and in 2nd we know the width but not height and in 3rd we know the height bit not the width and in last we dont know the hieght and width both
matrix=cv2.getPerspectiveTransform(pt1,pt2)#this is use to get our values in matrix form
imgOutput=cv2.warpPerspective(imgCard,matrix,(width,height))#this is the method where we have to put all the things like pt and matrix and height and width
cv2.imshow('Perspective image',imgOutput)
cv2.waitKey(0)
#------------------------------------------------------------------------#
#Joining Image
imgJoin=cv2.imread(r"C:\Users\Mr-SWIFT\Downloads\images.jfif")
cv2.imshow('joining image',imgJoin)
imgHor=np.hstack((imgJoin,imgJoin,imgJoin))
imgVer=np.vstack((imgJoin,imgJoin,imgJoin))
cv2.imshow("Horizontal image ",imgHor)
cv2.imshow('Vertical Image',imgVer)
cv2.waitKey(0)
#--------------------------------------------------------------------------------#
 
 



