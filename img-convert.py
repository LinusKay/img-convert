from __future__ import print_function
from wand.image import Image
from os import remove, path, mkdir
import glob

# settings
# convert_from          - filetype to convert from. all other filetypes will be ignored
# convert_to            - filetype to convert to
# directory_in          - directory containing images to be converted
# directory_out         - directory to save converted images to
# delete_after_convert  - surprisingly, deletes original images after conversion
convert_from = 'heic'
convert_to = 'jpg'
directory_in = 'photos'
directory_out = 'photos/out'
delete_after_convert = False

# create directory if nonexistent
if not path.exists(directory_out): mkdir(directory_out)

# collect all images
images = glob.glob(directory_in + '\*.' + convert_from)

# count length of directory_in and convert_from
# used to retrieve image name
len_dir_in = len(directory_in)+1
len_ext = len(convert_from)+1

# loop through all images and convert
for image in images:
    image_name = image[len_dir_in:-len_ext]
    with Image(filename = image) as img:
        with img.convert(convert_to) as converted:
            converted.save(filename = directory_out + '\\' + image_name + '.jpeg')
            print('converted ' + image)
            if delete_after_convert: 
                remove(image)
                print('deleted ' + image)
