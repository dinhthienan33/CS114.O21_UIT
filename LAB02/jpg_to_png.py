from PIL import Image
import os

def convert_to_png(input_dir, output_dir):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over the files in the input directory
    for filename in os.listdir(input_dir):
        
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            # Open the JPEG image
            # Convert to PNG format
            output_filename = filename.rsplit(".", 1)[0] + ".png"
            output_path = os.path.join(output_dir, output_filename)

        elif (filename.endswith(".png")): 
            output_path = os.path.join(output_dir, filename)
        else : 
            continue
        image_path = os.path.join(input_dir, filename)
        image = Image.open(image_path)
        image.save(output_path, "PNG")
# Specify the input and output directories
input_directory = r"D:\Nam 2\ML\ThayAnThuthach\cs114.o21.x.lab01-competition"
output_directory = "data"

# Call the function to perform the conversion
convert_to_png(input_directory, output_directory)