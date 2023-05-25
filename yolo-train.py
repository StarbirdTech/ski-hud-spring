import os
from dotenv import load_dotenv
from ultralytics import YOLO
from roboflow import Roboflow


def get_dataset(project_workspace, project_name, project_version):
    project_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "cache",
        "datasets",
        f"{project_name}-{project_version}",
    )
    if not os.path.exists(project_path):
        load_dotenv()
        Roboflow(api_key=os.getenv("ROBOFLOW_API_KEY")).workspace(
            project_workspace
        ).project(project_name).version(project_version).download(
            "yolov8", project_path
        )
        print(f"✅  Cached {project_name}-{project_version}")
    return os.path.join(project_path, "data.yaml")


YOLO("yolov8n.pt").train(
    data=get_dataset("lloyd","crossed-skis-detection", 1),
    imgsz=640,
    epochs=50,
    batch=8,
    name="yolov8n_v8_50e",
)
