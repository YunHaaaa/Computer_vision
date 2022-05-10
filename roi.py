import cv2
import numpy as np

img = cv2.imread('../img/cat2.jpg')

x=72; y=30; w=200; h=200;
roi = img[y:y+h, x:x+w]

print(roi.shape)
cv2.rectangle(roi, (0,0), (h-1, w-1), (0, 255, 0))
cv2.imshow("img", img)

key = cv2.waitKey(0)
print(key)
cv2.destroyAllWindows()
