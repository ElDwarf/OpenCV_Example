import cv2
import numpy as np

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)
rval, img = vc.read()

while True:
    if img is not None:
        cv2.imshow("preview", img)
    rval, img = vc.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    lines = cv2.HoughLines(edges,1,np.pi/180, 200)
    if lines is not None:
        for r,theta in lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*r
            y0 = b*r
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            cv2.line(img,(x1,y1), (x2,y2), (0,0,255),2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
