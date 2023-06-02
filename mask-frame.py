import os
import platform
from ultralytics import YOLO


print("1 - System Webcam")
print("2 - Video File")
print("3 - Process Image")
option = int(input("Enter Option: "))

# get all .pt files in models folder
models = ["yolov8n.pt", "yolov8n-seg.pt"] + [
    file for file in os.listdir("models") if file.endswith(".pt")
]

# print all .pt files in models folder
for i, model in enumerate(models):
    print(f"{i + 1} - {model}")
while True:
    if 0 < (int(input("Enter Option: "))) < models.__len__() + 1:
        model = YOLO(models[int(input("Enter Option: ")) - 1])
        break

print(model)

# if option == 1:
#     if platform.system() == "Darwin":  # MacOS
#         model.predict(source="1", show=True, boxes=False, retina_masks=True)
#     else:  # Windows & Linux
#         model.predict(source="0", show=True, boxes=False, retina_masks=True)
# elif option == 2:
#     model.predict(
#         "cache/lo6rBzkYw14.mp4",
#         show=True,
#         boxes=False,
#         retina_masks=True,
#     )
# elif option == 3:
#     model.predict(
#         "cache/crossed-ski-1.png",
#         show=True,
#         boxes=True,
#         save=True,
#     )
