import cv2
import numpy as np
import math

# Using CPU
from object_detection import ObjectDetection

# Using GPU
# from gpu_object_detection import ObjectDetection

detector = ObjectDetection()
capture = cv2.VideoCapture("video.mp4")

count = 0
prev_centers = []
tracking_objects = {}
track_id = 0

while True:
    ret, frame = capture.read()
    if not ret:
        break
    count += 1

    curr_centers = []
    classIDs, conf_score, boxes = detector.detect(frame)
    for box in boxes:
        x, y, w, h = box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cx = int(x + w/2)
        cy = int(y + h/2)
        curr_centers.append((cx, cy))

    if count <= 2:
        for c in curr_centers:
            for p in prev_centers:
                distance = math.sqrt((c[0] - p[0])**2 + (c[1] - p[1])**2)
                if distance < 20:
                    tracking_objects[track_id] = c
                    track_id += 1
    else:
        for id, p in tracking_objects.copy().items():
            object_exits = False
            for c in curr_centers.copy():
                distance = math.sqrt((c[0] - p[0])**2 + (c[1] - p[1])**2)
                if distance < 20:
                    tracking_objects[id] = c
                    object_exits = True
                    if c in curr_centers:
                        curr_centers.remove(c)
                    continue

            if not object_exits:
                tracking_objects.pop(id)

        for center in curr_centers:
            tracking_objects[track_id] = center
            track_id += 1

    for id, center in tracking_objects.items():
        cv2.circle(frame, center, 5, (0, 0, 255), cv2.FILLED)
        cv2.putText(frame, str(id), (center[0], center[1]-5), 0, 1, (0, 0, 255), 2)

    prev_centers = curr_centers.copy()

    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()