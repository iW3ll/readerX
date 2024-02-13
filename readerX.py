from PIL import Image
import exifread

def extract_location_info(image_path):
   
    with open(image_path, 'rb') as f:
       
        img = Image.open(f)

        
        exif_data = img._getexif()

       
        if exif_data is not None:
           
            tags = exifread.process_file(f)

            if 'GPS GPSLatitude' in tags and 'GPS GPSLongitude' in tags:
                latitude = tags['GPS GPSLatitude']
                longitude = tags['GPS GPSLongitude']

                lat_decimal = latitude.values[0] + latitude.values[1] / 60 + latitude.values[2] / 3600
                lon_decimal = longitude.values[0] + longitude.values[1] / 60 + longitude.values[2] / 3600

                return lat_decimal, lon_decimal
            else:
                return None
        else:
            print("No EXIF data found.")
            return None


image_path = 'path/to/your/image.jpg'
location_info = extract_location_info(image_path)

if location_info:
    print(f"Latitude: {location_info[0]}, Longitude: {location_info[1]}")
else:
    print("No location information found.")
