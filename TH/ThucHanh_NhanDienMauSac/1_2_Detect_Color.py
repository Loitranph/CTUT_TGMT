import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    red_lower = np.array([0, 50, 120], np.uint8)
    red_upper = np.array([30, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsv, red_lower, red_upper)
    red_cnt, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c_red in red_cnt:
        cv2.putText(frame, 'RED', (20, 40), 1, 3, (0, 0, 255), 2)

    green_lower = np.array([40, 70, 80], np.uint8)
    green_upper = np.array([70, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsv, green_lower, green_upper)
    green_cnt, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c_green in green_cnt:
        cv2.putText(frame, 'GREEN', (20, 80), 1, 3, (0, 255, 0), 2)

    blue_lower = np.array([90, 860, 20], np.uint8)
    blue_upper = np.array([121, 255, 255], np.uint8)
    blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)
    blue_cnt, _ = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c_blue in blue_cnt:
        cv2.putText(frame, 'BLUE', (20, 120), 1, 3, (255, 0, 0), 2)

    yellow_lower = np.array([25, 70, 120], np.uint8)
    yellow_upper = np.array([30, 255, 255], np.uint8)
    yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    yellow_cnt, _ = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c_yellow in yellow_cnt:
        cv2.putText(frame, 'YELLOW', (20, 160), 1, 3, (0, 255, 255), 2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

