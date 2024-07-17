import os

path = 'suzuki2'
img_files = os.listdir(path)

for i, img in enumerate(img_files, start=222):
    # Split the extension from the path and normalise it to lowercase.
    ext = os.path.splitext(img)[-1].lower()

    # Generate new name for the image.
    new_img = '22520003-22520010-22520398-22520630-22520053.suzuki'+'.' + str(i) + ext

    # Check if the new file name already exists
    if not os.path.exists(os.path.join(path, new_img)):
        # Rename the file
        os.rename(os.path.join(path, img), os.path.join(path, new_img))
    else:
        print(f"File {new_img} already exists. Skipping.")