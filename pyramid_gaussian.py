import cv2

img = cv2.imread('../img/cat.jpg')

smaller = cv2.pyrDown(img) # img x 1/4
bigger = cv2.pyrUp(img) # img x 4

cv2.imshow('img', img)
cv2.imshow('pyrDown', smaller)
cv2.imshow('pyrUp', bigger)
cv2.waitKey(0)
cv2.destroyAllWindows()
