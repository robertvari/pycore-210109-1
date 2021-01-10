import os
from PIL import Image, ExifTags
from openpyxl import Workbook


folder_path = r"D:\Photos\CIW"  # raw string

# list comprehension
photo_list = [
    photo for photo in os.listdir(folder_path)
    if photo.lower().endswith(".jpg")
]

workbook = Workbook()
sheet = workbook.active
sheet["A1"] = "Name"
sheet["B1"] = "Date"
sheet["C1"] = "Camera"
sheet["D1"] = "Lens"
sheet["E1"] = "ISO"

for photo in photo_list:
    pass

excel_file = "photo_data.xlsx"
workbook.save(excel_file)