import os
import json

# الحصول على مسار المشروع الحالي
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "https://raw.githubusercontent.com/OmarShawkey13/RcWallPaper/refs/heads/main"
OUTPUT_FILE = os.path.join(BASE_DIR, "home.json")
VALID_FOLDERS = ['amoled', 'anime', 'hero']

wallpapers = []

# لف على الفولدرات المحددة
for folder in VALID_FOLDERS:
    folder_path = os.path.join(BASE_DIR, folder)
    
    if os.path.isdir(folder_path):
        images = sorted(
            [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.png'))],
            key=lambda x: int(''.join(filter(str.isdigit, x.split('.')[0])) or 0)
        )

        for image in images:
            wallpapers.append({
                "urlImage": f"{BASE_URL}/{folder}/{image}"
            })
        
        print(f"✓ {folder}: {len(images)} صورة")

# احفظ البيانات
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(
        {"wallpaper": wallpapers},
        f,
        indent=2,
        ensure_ascii=False
    )

print(f"\n✅ تم إنشاء home.json ({len(wallpapers)} صورة إجمالي)")
