import os
import json

# مسار المشروع الحالي
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "https://raw.githubusercontent.com/OmarShawkey13/WallPaper/refs/heads/main"

# فولدرات يتم تجاهلها
IGNORE_FOLDERS = {'.git', '.github', '__pycache__'}

categories = []

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
        print(f"⚠ {folder}: لا توجد صور")
        continue

    categories.append({
        "name": folder,
        "displayName": folder.capitalize(),
        "thumbnail": f"{BASE_URL}/{folder}/{images[0]}",
        "imageCount": len(images)
    })

    print(f"✓ {folder.capitalize()}: {len(images)} صورة")

# حفظ البيانات
with open('category.json', 'w', encoding='utf-8') as f:
    json.dump(
        {"categories": categories},
        f,
        indent=2,
        ensure_ascii=False
    )

print(f"\n✅ تم إنشاء category.json ({len(categories)} فئات)")
