import os
import cv2

img = cv2.imread('C:/Users/paulrithish-intern/Pictures/bird.jpg')
if img is None:
    print("Image not loaded. Check file path/name!")
    raise SystemExit

img = cv2.resize(img, (600, 400))

cv2.namedWindow("Edges", cv2.WINDOW_NORMAL)
def nothing(x):
    pass
cv2.createTrackbar("Low", "Edges", 50, 255, nothing)
cv2.createTrackbar("High", "Edges", 150, 255, nothing)

while True:

    low = cv2.getTrackbarPos("Low", "Edges")
    high = cv2.getTrackbarPos("High", "Edges")

    if high < low:
        high = low
        cv2.setTrackbarPos("High", "Edges", high)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    edges = cv2.Canny(blur, low, high)


    cv2.imshow("Original", img)
    cv2.imshow("Edges", edges)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv2.imwrite("edges_output.png", edges)
        print("Saved: edges_output.png")

cv2.destroyAllWindows()