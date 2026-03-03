import cv2
import os

img = cv2.imread("C:/Users/paulrithish-intern/Pictures/bird.jpg")
edges = cv2.Canny(img, 100, 200)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()