import cv2
from PIL import Image
import numpy as np


cap = cv2.VideoCapture(0)
while True : 
    r,frame = cap.read()
    frame =cv2.flip(frame, 1)
    if not r : 
        print("cannot open the camera")
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #Red range 1: pure red near Hue 0
    lower_red1 = np.array([0, 185, 80])
    upper_red1 = np.array([4, 255, 255])

    # Red range 2: pure red near Hue 179
    lower_red2 = np.array([175, 185, 80])
    upper_red2 = np.array([179, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    mask = cv2.bitwise_or(mask1, mask2)
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    if bbox is not None : 
        x1,y1,x2,y2 = bbox
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 5)
        cv2.putText(
            frame,
            "RED",
            (x1, y1 - 15),
            cv2.FONT_HERSHEY_SIMPLEX,
            2,
            (0, 0, 255),
            3
        )
    
    #blue 
    
    lowerBlue = np.array([100,150,80])
    upperBlue = np.array([130,255,255])
    mask_blue = cv2.inRange(hsv, lowerBlue, upperBlue)
    maskB = Image.fromarray(mask_blue)
    bboxBlue = maskB.getbbox()
    if bboxBlue is not None : 
        x1,y1,x2,y2 = bboxBlue
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 5)
        cv2.putText(
            frame,
            "Blue",
            (x1, y1 - 15),
            cv2.FONT_HERSHEY_SIMPLEX,
            2,
            (0, 0, 255),
            3
        )
    cv2.imshow("RED blue", frame)

    if cv2.waitKey(1)  & 0xff == ord("p") :
        break

cap.release()
cv2.destroyAllWindows()