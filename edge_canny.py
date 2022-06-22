import cv2, time
import numpy as np

img = cv2.imread("../img/sudoku.jpg")

edges = cv2.Canny(img,100,200)

cv2.imshow('Original', img)
cv2.imshow('Canny', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
