import platform
from ultralytics import YOLO
from exampleContent import getFile

model = YOLO("yolov8n-seg.pt")

print("1 - System Webcam")
print("2 - Video File")
print("3 - Process Image")
option = int(input("Enter Option: "))

if option == 1:
    if platform.system() == "Darwin":  # MacOS
        model.predict(source="1", show=True, boxes=False, retina_masks=True)
    else:  # Windows & Linux
        model.predict(source="0", show=True, boxes=False, retina_masks=True)
elif option == 2:
    model.predict(
        getFile("uZsp5JxrpPg", "mp4"),
        show=True,
        boxes=False,
        retina_masks=True,
        save=True,
    )
elif option == 3:
    model.predict(
        "cache/crossed-ski-1.png",
        show=True,
        boxes=True,
        save=True,
    )
