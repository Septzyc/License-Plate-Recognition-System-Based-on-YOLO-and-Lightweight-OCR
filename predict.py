from ultralytics import YOLO
import cv2
from PIL import Image, ImageDraw, ImageFont
from cnocr import CnOcr

model = YOLO(r"runs\detect\train-3\weights\best.pt")
ocr = CnOcr(rec_model_name="densenet_lite_136-gru")

font = ImageFont.truetype(r"C:\Windows\Fonts\simhei.ttf", 28)

img_bgr = cv2.imread("test.jpg")
pil_img = Image.fromarray(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))
draw = ImageDraw.Draw(pil_img)

results = model(img_bgr)

for box in results[0].boxes.xyxy:
    x1, y1, x2, y2 = map(int, box)
    plate_crop = img_bgr[y1:y2, x1:x2]
    out = ocr.ocr_for_single_line(plate_crop)
    if out:
        plate_num = out["text"]
        print("车牌：", plate_num)
        cv2.rectangle(img_bgr, (x1, y1), (x2, y2), (0, 255, 0), 2)
        draw.text((x1, y1 - 35), plate_num, font=font, fill=(255, 0, 0))

pil_img.save("plate_result.jpg")