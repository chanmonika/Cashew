import cv2

#choose dictionary
aruco_dict = cv2.aruco.getPredefinedDictionary(
    cv2.aruco.DICT_4X4_50
)
#id
marker = cv2.aruco.generateImageMarker(
    aruco_dict,
    6,
    400
)

# Add a white margin
marker = cv2.copyMakeBorder(
    marker,
    50, 50, 50, 50,
    cv2.BORDER_CONSTANT,
    value=255
)

cv2.imwrite("marker6.png", marker)
cv2.imshow("ArUco Marker", marker)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Marker generated successfully!")