import os
from hashlib import md5
import re

def delete_duplicate_files(directory):
    # Regular expression pattern to match file names ending with (1), (2), etc.
    pattern = re.compile(r'\s\(\d+\)$')

    # Iterate over each file in the directory and its subdirectories
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            # Get the name of the file without the extension
            name, ext = os.path.splitext(filename)

            # Check if the name matches the pattern
            if pattern.search(name):
                # Delete the duplicate file
                os.remove(os.path.join(foldername, filename))

    print("Duplicate files deleted successfully.")

def delete_non_image_files(directory):
    # Iterate over each file in the directory and its subdirectories
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            # Get the full path of the file
            filepath = os.path.join(foldername, filename)

            # Check if the file is not an image
            if os.path.isfile(filepath) and not filename.lower().endswith(('.jpg','.jpeg', '.png',)):
                # Delete the non-image file
                os.remove(filepath)

    print("Non-image files deleted successfully.")
# Specify the directory containing the images
directory = 'suzuki'

# Call the function to delete duplicate images
delete_duplicate_files(directory)
