from PIL import Image
from PIL.ExifTags import TAGS


image = Image.open("Clara.jpg")
exifdata = image.getexif()

if exifdata:
    for tagid in exifdata:
        tagname = TAGS.get(tagid, tagid)
        value = exifdata.get(tagid)
        print(f"{tagname}: {value}")
else:
    print("No EXIF data found in this image.")

