import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../src/test01.jpg')
b, g, r = cv2.split(img)
img2 = cv2.merge([r, g, b])

#subplot 121 mean 1.. = row, .2. = column, ..1 = position
plt.subplot(121); plt.imshow(img) #expect distorted color
plt.subplot(122); plt.imshow(img2) #expect true color
plt.show()

cv2.imshow('bgr image', img)
cv2.imshow('rgb image', img2, interpolation = 'bicubic')

cv2.waitKey(0)
cv2.destroyAllWindows()