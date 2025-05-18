# Importing Ultralytics and Roboflow
!pip install ultralytics roboflow
from ultralytics import YOLO
from roboflow import Roboflow

# Downloading dataset from Roboflow in YOLO TXT Format
rf = Roboflow(api_key="API-KEY")  
project = rf.workspace("object-detection-part").project("android-ui-dataset")
version = project.version(2)
dataset = version.download("yolov8") 

# Yolo Model
model = YOLO("yolo11m.pt") 

# Training Model
model.train(
    data="android-ui-dataset-2/data.yaml",  # Roboflow’dan gelen YAML dosyası
    epochs=200,
    patience=10,
    workers=4,
    device = cuda,
    imgsz=640,
    batch=16,
    name="android-ui-yolov11"
)

# Model Evaluation
model.val()
