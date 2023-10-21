from PIL import Image
from PIL.ExifTags import TAGS
import os.path, time
import datetime
import pathlib
import filetype


def check_type(f):
    if filetype.is_image(f):
        return True
    else:
        return False

def get_date(f):
    img = Image.open(f)
    exifdata = img._getexif()
    if exifdata:
        date = exifdata.get(306)
        return date
    else:
        file = pathlib.Path(f)
        ctime = datetime.datetime.fromtimestamp(file.stat().st_ctime, tz=datetime.timezone.utc)
        return ctime 

directory = input('Enter directory to date:')
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    print(f"Image name {filename}, created at {get_date(f)}")
    


