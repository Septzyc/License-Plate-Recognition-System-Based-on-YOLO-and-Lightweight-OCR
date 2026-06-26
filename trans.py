import os

# 这里换成你真实的完整文件夹路径，复制下面这行改地址即可
img_dir = r"C:\Users\septzyc\Desktop\sythnic\yolov8_prg\car\images"
prefix = "plate"

suffixs = (".jpg", ".jpeg", ".png", ".bmp")
files = [f for f in os.listdir(img_dir) if f.lower().endswith(suffixs)]
files.sort()

num = 1
for old_name in files:
    old_path = os.path.join(img_dir, old_name)
    ext = os.path.splitext(old_name)[1]
    new_name = f"{prefix}_{num:03d}{ext}"
    new_path = os.path.join(img_dir, new_name)
    os.rename(old_path, new_path)
    print(f"{old_name}  -->  {new_name}")
    num += 1

print("✅ 图片批量改名完毕")