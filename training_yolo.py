from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="car.yaml",
    epochs=50,
    imgsz=640,
    batch=4,        # 2G显存，不要开batch=8
    workers=0,      # Windows系统必须设为0，防止数据加载卡死
    amp=False       # 核心：关闭AMP，避开这个bug
)
