# 解决Spyder cv2.gapi自动重载报错，放在代码最顶部
import sys
import os
sys.modules['cv2.gapi.wip'] = None
import cv2
from ultralytics import YOLO

# 加载最轻量预训练模型（自动下载，不用自己训练）
model = YOLO("yolov8n.pt")

# --------------------------路径配置--------------------------
input_dir = "test"    # 同目录下test文件夹，存放待检测图片
output_dir = "output"  # 推理结果保存到outputli文件夹

# 如果文件夹不存在自动创建
if not os.path.exists(input_dir):
    os.makedirs(input_dir)
    print(f"已创建输入文件夹：{input_dir}，请放入jpg/png图片")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --------------------------推理参数（适配2G显存，参数不要删）--------------------------
results = model(
    source=input_dir,       # 读取整个test文件夹所有图片
    save=True,
    save_dir=output_dir,    # 指定输出文件夹为outputli
    imgsz=480,              # 降低分辨率防爆显存
    batch=1,
    conf=0.5,               # 低于50%置信度的物体不显示
    device=0                # 使用GPU；爆显存就改成 device="cpu"
)

# 批量打印每张图片的检测信息
for res in results:
    # 获取当前图片文件名
    img_name = os.path.basename(res.path)
    boxes = res.boxes
    print(f"\n图片：{img_name}，一共检测到 {len(boxes)} 个目标")
    if len(boxes) > 0:
        print("目标类别、置信度：")
        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            cls_name = model.names[cls_id]
            print(f"  {cls_name}  置信度：{conf:.2f}")

print(f"\n全部图片推理完成！标注图片保存在：{os.path.abspath(output_dir)}")