from ultralytics import YOLO


class ObjectDetection:
    def __init__(self, model_name="yolov8n.pt"):
        # This will automatically download the YOLOv8-nano weights file and load it directly onto your GPU.
        self.model = YOLO(model_name)

    def detect(self, frame):
        results = self.model(frame, verbose=False)[0]

        boxes_data = results.boxes.xyxy.cpu().numpy()
        scores = results.boxes.conf.cpu().numpy()
        class_ids = results.boxes.cls.cpu().numpy().astype(int)

        # Convert x1, y1, x2, y2 format to x, y, w, h to keep main.py compatible
        boxes = []
        for box in boxes_data:
            x1, y1, x2, y2 = box
            boxes.append([int(x1), int(y1), int(x2 - x1), int(y2 - y1)])

        return class_ids, scores, boxes