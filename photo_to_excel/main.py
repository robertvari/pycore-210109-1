import os

folder_path = r"D:\Photos\CIW"  # raw string

# list comprehension
photo_list = [
    photo for photo in os.listdir(folder_path)
    if photo.lower().endswith(".jpg")
]

print(photo_list)
print( len(photo_list) )