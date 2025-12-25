import os
import json

# الحصول على مسار المشروع الحالي
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
categories = []
VALID_FOLDERS = ['amoled', 'anime', 'hero']  # المجلدات المراد قراءتها فقط
BASE_URL = "https://raw.githubusercontent.com/OmarShawkey13/RcWallPaper/refs/heads/main"

for folder in VALID_FOLDERS:
    folder_path = os.path.join(BASE_DIR, folder)
    
    if os.path.isdir(folder_path):
        # قراءة الصور
        images = sorted(
            [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png'))],
            key=lambda x: int(''.join(filter(str.isdigit, x.split('.')[0])) or 0)
        )

        if images:
            categories.append({
                "name": folder,
                "displayName": folder.capitalize(),
                "thumbnail": f"{BASE_URL}/{folder}/{images[0]}",
                "imageCount": len(images)
            })
            print(f"✓ {folder.capitalize()}: {len(images)} صورة")
        else:
            print(f"⚠ {folder}: لا توجد صور")

# احفظ البيانات
with open('category.json', 'w', encoding='utf-8') as f:
    json.dump({"categories": categories}, f, indent=2, ensure_ascii=False)

print(f"\n✅ تم إنشاء category.json ({len(categories)} فئات)")
