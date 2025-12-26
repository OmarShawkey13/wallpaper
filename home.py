import os
import json

# مسار المشروع الحالي
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "https://raw.githubusercontent.com/OmarShawkey13/WallPaper/refs/heads/main"
OUTPUT_FILE = os.path.join(BASE_DIR, "home.json")

# فولدرات يتم تجاهلها (اختياري)
IGNORE_FOLDERS = {'.git', '.github', '__pycache__'}

wallpapers = []

# لف على كل الفولدرات الموجودة في المشروع
for folder in sorted(os.listdir(BASE_DIR)):
    folder_path = os.path.join(BASE_DIR, folder)

    if not os.path.isdir(folder_path):
        continue

    if folder in IGNORE_FOLDERS:
        continue

    images = sorted(
        [
            f for f in os.listdir(folder_path)
            if f.lower().endswith(('.jpg', '.png'))
        ],
        key=lambda x: int(''.join(filter(str.isdigit, os.path.splitext(x)[0])) or 0)
    )

    if not images:
        continue

    for image in images:
        wallpapers.append({
            "urlImage": f"{BASE_URL}/{folder}/{image}"
        })

    print(f"✓ {folder}: {len(images)} صورة")

# حفظ البيانات في ملف JSON
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(
        {"wallpaper": wallpapers},
        f,
        indent=2,
        ensure_ascii=False
    )

print(f"\n✅ تم إنشاء home.json ({len(wallpapers)} صورة إجمالي)")
