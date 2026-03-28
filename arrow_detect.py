import cv2
import numpy as np

LOWER_BGR = np.array([64, 19, 19])
UPPER_BGR = np.array([118, 150, 80])

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot connect to Pi stream")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.GaussianBlur(frame, (7, 7), 0)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # define range in HSV (you'll need to tune these)
        LOWER_HSV = np.array([95,100, 100])
        UPPER_HSV = np.array([115, 255, 255])

        arrow_mask = cv2.inRange(hsv, LOWER_HSV, UPPER_HSV)

        h, w = frame.shape[:2]

        # arrow_mask = cv2.inRange(frame, LOWER_BGR, UPPER_BGR)
        cv2.imshow("arrow_mask", arrow_mask)

        # --- find contours in the mask ---
        contours, _ = cv2.findContours(arrow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            # grab the largest contour (most likely the arrow)
            largest = max(contours, key=cv2.contourArea)
            area = cv2.contourArea(largest)

            if area > 500:  # ignore tiny noise
                # bounding box
                x, y, bw, bh = cv2.boundingRect(largest)
                cv2.rectangle(frame, (x, y), (x + bw, y + bh), (0, 255, 0), 2)

                # center of the contour (moments)
                M = cv2.moments(largest)
                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])

                    # compare centroid to bounding box center
                    box_center_x = x + bw // 2
                    if cx > box_center_x:
                        direction = "RIGHT"
                    else:
                        direction = "LEFT"

                    cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
                    cv2.putText(frame, direction, (10, 30),
                                cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)

        cv2.imshow("frame", frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()