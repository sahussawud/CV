import cv2
import numpy as np

img = cv2.imread('./src/football.jpg');
print("Size of Picture : ", img.size)
print("Dtype : ", img.dtype)

# [row<Y coordinate>, column<X coordinate>]
e1 = cv2.getTickCount()
football = img[115:268, 811:980]
img2 = img.copy()   
img2[443:596, 881:1050] = football
img2[275:428, 997:1166] = football
e2 = cv2.getTickCount()

time = (e2-e1)/cv2.getTickFrequency()
print("Excecute time ", time, " s")

cv2.imshow('football_cp', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Split picture
b, g, r = cv2.split(img)
# Merge picture back
img = cv2.merge((b, g, r))
# blue color
b = img[:,:,0]