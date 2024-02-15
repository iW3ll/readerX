import os
from PIL import Image
from PIL.ExifTags import TAGS

img_file = r""
image = Image.open(img_file)

exif = image._getexif()

if exif is not None:
    exif_dict = {}

    for tag, value in exif.items():
        if tag in TAGS:
            exif_dict[TAGS[tag]] = value

    print("Full EXIF data:", exif_dict)

    if "GPSInfo" in exif_dict:
        geo_coordinate = "{0} {1} {2:.2f} {3}, {4} {5} {6:.2f} {7}".format(
            exif_dict["GPSInfo"][2][0][0],
            exif_dict["GPSInfo"][2][1][0],
            exif_dict["GPSInfo"][2][2][0] / exif_dict["GPSInfo"][2][2][1],
            exif_dict["GPSInfo"][1],
            exif_dict["GPSInfo"][4][0][0],
            exif_dict["GPSInfo"][4][1][0],
            exif_dict["GPSInfo"][4][2][0] / exif_dict["GPSInfo"][4][2][1],
            exif_dict["GPSInfo"][3],
        )
        print("GPS coordinates:", geo_coordinate)
    else:
        print("No GPS information found in EXIF data.")
else:
    print("No EXIF data found in the image.")
