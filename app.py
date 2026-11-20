import cv2
from ultralytics import YOLO
from playsound import playsound
import time

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open camera
cap = cv2.VideoCapture(0)

last_spoken = 0
detection_count = 0   # 🔥 count detections

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    phone_detected = False

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]

            if label == "cell phone":
                phone_detected = True

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(frame, "PHONE DETECTED!", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    # 🔊 Voice logic
    if phone_detected and time.time() - last_spoken > 5:
        detection_count += 1

        print("Detection count:", detection_count)

        if detection_count <= 2:
            playsound("warning1.mp3")   # normal warning
        else:
            playsound("warning.mp3")   # strict warning

        last_spoken = time.time()

    cv2.imshow("Phone Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()