from ultralytics import YOLO

model = YOLO('yolov8n-seg.pt')

#source=1 for mac webcam 
#source=0 for windows
model.predict(source="1", show=True, boxes=False, retina_masks=True)