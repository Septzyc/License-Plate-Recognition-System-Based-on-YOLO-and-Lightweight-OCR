# License-Plate-Recognition-System-Based-on-YOLO-and-Lightweight-OCR
基于 YOLO 与轻量 OCR 的车牌识别系统设计与实现。图像处理结课论文。考虑到电脑GPU性能以及为了节省时间在百度上下载了53张车牌照片作为数据集（见car/images),用labelme手动标注后转换为txt文件(car/labels)，随后基于开源的yolov8n.pt训练模型能够识别车牌位置，随后又加入OCR使模型能够识别车牌文字。

## 数据集很小
因为我没太多时间训练，且不确定电脑GPU性能能否跑动上百张数据。

## 是我第一次半手搓yolov8识别车牌的完整过程哈哈，此模型还有很多能优化的地方。
