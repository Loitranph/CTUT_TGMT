import cv2

cap = cv2.VideoCapture(0)

while True:
    ret ,frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    height, width, ret= frame.shape
    cx = int(width / 2)
    cy = int(height / 2)

    # Chon gia tri diem anh
    pixel_center = hsv_frame[cx, cy]
    cv2.circle(frame, (cx, cy), 100, (255, 0, 0), 3)

    hue_value = pixel_center[0]
    color = "Undefined"

    if hue_value < 9:
        color = "RED"

    elif hue_value > 45 and hue_value < 95:
        color = "GREEN"

    elif hue_value > 95 and hue_value < 120:
        color = "BLUE"

    cv2.putText(frame, color, (30, 30), 0, 1, (0, 0, 255), 3)

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()