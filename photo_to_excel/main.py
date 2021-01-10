import os

folder_path = r"D:\Photos\CIW"  # raw string

# list comprehension
valid_photos = [photo for photo in os.listdir(folder_path) if photo.lower().endswith(".jpg")]

print(valid_photos)
print( len(valid_photos) )