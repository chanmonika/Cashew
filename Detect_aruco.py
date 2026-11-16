import cv2


img = cv2.imread("ArUco/marker6.png")

if img is None:
    print("Cannot read the image!")
    exit()

# choose the same dic
aruco_dict = cv2.aruco.getPredefinedDictionary(
    cv2.aruco.DICT_4X4_50
)

# detector
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

# Detect markers
corners, ids, rejected = detector.detectMarkers(img)

# check whether aruco detected
if ids is not None:
    print("Detected marker ID:", ids.flatten())

   #box
    cv2.aruco.drawDetectedMarkers(img, corners, ids)
else:
    print("No marker detected!")


cv2.imshow("ArUco Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()