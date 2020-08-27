import cv2
import numpy as np



def nothing(x):
    pass    
# Create a black image, a window 
img = cv2.imread('./src/football.jpg')
img2 = cv2.imread('./src/peace.jpg')
cv2.namedWindow('image')
# create trackbars for color change 
cv2.createTrackbar('Overlay','image',0,100,nothing) 
# create switch for ON/OFF functionality 
rows, cols, channel = img2.shape

overlayValue = 0
while(1):
    
    
    overlay = cv2.getTrackbarPos('Overlay','image') 
    overlayValue = overlay/100
    
    imgCopy = img.copy()
    bgimg = imgCopy[0:rows, 0:cols]
    
    dst = cv2.addWeighted(bgimg, 1-overlayValue, img2, overlayValue, 0)
    imgCopy[0:rows, 0:cols] = dst
    cv2.imshow('image',imgCopy)


    k = cv2.waitKey(1) & 0xFF 
    if k == 27:
        break
    
cv2.destroyAllWindows()
