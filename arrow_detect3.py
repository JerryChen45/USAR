import cv2
import numpy as np

LOWER_HSV = np.array([0, 0, 210])
UPPER_HSV = np.array([180, 25, 255])

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot connect to stream")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.GaussianBlur(frame, (7, 7), 0)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        arrow_mask = cv2.inRange(hsv, LOWER_HSV, UPPER_HSV)

        cv2.imshow("arrow_mask", arrow_mask)

        contours, _ = cv2.findContours(arrow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            largest = max(contours, key=cv2.contourArea)
            area = cv2.contourArea(largest)

            if area > 500:
                x_min = largest[:, :, 0].min()
                x_max = largest[:, :, 0].max()
                y_min = largest[:, :, 1].min()
                y_max = largest[:, :, 1].max()

                cropped_mask = arrow_mask[y_min:y_max, x_min:x_max]

                cw = cropped_mask.shape[1]
                left_half = cropped_mask[:, :cw // 2]
                right_half = cropped_mask[:, cw // 2:]
                cv2.imshow("cropped", cropped_mask)

                left_pixels = cv2.countNonZero(left_half)
                right_pixels = cv2.countNonZero(right_half)

                if left_pixels < right_pixels:
                    direction = "LEFT"
                else:
                    direction = "RIGHT"

                cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
                cv2.putText(frame, direction, (10, 30),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)

        cv2.imshow("frame", frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()