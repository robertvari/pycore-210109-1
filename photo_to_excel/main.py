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
sheet["F1"] = "Dimensions"

for index, file_name in enumerate(photo_list):
    file_path = os.path.join(folder_path, file_name)

    img = Image.open(file_path)

    row = index + 3

    # add image name
    sheet[f"A{row}"] = file_name

    # add data to dimension column
    sheet[f"F{row}"] = f"{img.size[0]}x{img.size[1]}"

    exif_data = img._getexif()  # Sometimes None
    if not exif_data:
        continue

    for key, value in exif_data.items():
        tag_name = ExifTags.TAGS.get(key)
        if not tag_name:
            continue

        if tag_name == "DateTimeOriginal":
            sheet[f"B{row}"] = value

        if tag_name == "Model":
            sheet[f"C{row}"] = value

        if tag_name == "LensModel":
            sheet[f"D{row}"] = repr(value).replace("\\x00", "")

        if tag_name == "ISOSpeedRatings":
            sheet[f"E{row}"] = value

excel_file = os.path.join(folder_path, "photo_data.xlsx")
workbook.save(excel_file)