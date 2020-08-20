import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('./src/test01.jpg', 0)

# If Load an image success would print out a metric
print(img)

cv2.imshow('image', img)

# cv2.waitKey() waits for specified
# milliseconds for any keyboard event.
# If you press any key in that time,
# the program continues.
# If 0 is passed, it waits indefinitely for
# a key stroke return key press. 

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('./output/test01gray.png', img)