import os
from dotenv import load_dotenv
from ultralytics import YOLO
from roboflow import Roboflow
import torch


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


def train(dataset):
    if not torch.cuda.is_available():
        input("⚠️  Torch cannot access CUDA - Press ENTER to continue")

    YOLO("yolov8n.pt").train(
        data=dataset,
        imgsz=640,
        epochs=50,
        batch=8,
        name="yolov8n_v8_50e",
    )


if __name__ == "__main__":
    train(get_dataset("lloyd", "crossed-skis-detection", 1))
