import os

folder_path = r"D:\Photos\CIW"  # raw string
photos = os.listdir(folder_path)

valid_photos = []
for item in photos:
    if not item.lower().endswith(".jpg"):
        continue

    valid_photos.append(item)

print(valid_photos)
print( len(valid_photos) )