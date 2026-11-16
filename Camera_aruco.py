#use camera to detct import cv2
import numpy as np
import cv2
cap = cv2.VideoCapture(0)

#ArUco dictionary
aruco_dict = cv2.aruco.getPredefinedDictionary(
    cv2.aruco.DICT_4X4_50
)

#Create detector
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

#Marker physical size 
marker_length = 0.05
half = marker_length / 2

# Define 3D marker corners
object_points = np.array([
    [-half,  half, 0],
    [ half,  half, 0],
    [ half, -half, 0],
    [-half, -half, 0]
], dtype=np.float32)

# camera parameters
camera_matrix = np.array([
    [800, 0, 320],
    [0, 800, 240],
    [0, 0, 1]
], dtype=np.float64)

dist_coeffs = np.zeros((5, 1))

while True:

    ret, frame = cap.read()

    if not ret:
        print("Cannot open camera!")
        break
    

    # Detect markers
    corners, ids, rejected = detector.detectMarkers(frame)

    if ids is not None:

        cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        for i in range(len(ids)):

            print("Detected ID:", ids[i][0])

            image_points = corners[i].reshape(4, 2)

            # Estimate position
            success, rvec, tvec = cv2.solvePnP(
                object_points,
                image_points,
                camera_matrix,
                dist_coeffs
            )

            if success:

                x, y, z = tvec.flatten()

                distance = np.linalg.norm(tvec)

                print("X:", round(x, 3), "m")
                print("Y:", round(y, 3), "m")
                print("Z:", round(z, 3), "m")
                print("Distance:", round(distance, 3), "m")

                # Draw coordinate axes
                cv2.drawFrameAxes(
                    frame,
                    camera_matrix,
                    dist_coeffs,
                    rvec,
                    tvec,
                    0.03
                )
    frame = cv2.flip(frame, 1)

    cv2.imshow("ArUco Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()