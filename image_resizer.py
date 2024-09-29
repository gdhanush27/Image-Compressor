# Description: This script resizes and compresses images to a target size range (in KB) while adding extra metadata to the image file.
import warnings
warnings.simplefilter("ignore", DeprecationWarning)

import subprocess
import sys
import os

try:
    from PIL import Image
except ImportError:
    print("Pillow (PIL) not found, installing Pillow...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    # Retry import after installation
    from PIL import Image
    print("Pillow installed and imported successfully!")

input_folder = input("Enter the input folder path: ").strip()
# check if the input folder exists
if not os.path.exists(input_folder):
    print("Input folder does not exist.")
    input("Press Enter to exit...")
    sys.exit(1)

output_folder = input("Enter the output folder path: ").strip()
# check if the input folder exists if not create it
if not os.path.exists(output_folder):
    print("Output folder does not exist. Creating output folder...")
    os.makedirs(output_folder)

# Set parameters
size = (132, 132)  # Size: 132x132 pixels
dpi = (200, 200)  # Resolution: 200 DPI
target_min_size = 20   # Minimum 20KB
target_max_size = 30   # Maximum 30KB
extra_data_size = 10240  # 10KB of extra metadata
# Print parameters
print(f"Size: {size[0]}x{size[1]} pixels")
print(f"Resolution: {dpi[0]} DPI")
print(f"Target size: {target_min_size}KB - {target_max_size}KB")
correct_details = input("Is the above information correct? (Y/N): ")

# Correct details
if correct_details.lower() != 'y':
    print("Please correct the parameters. Press Enter to keep the current values.")

    # Update size if input is provided
    new_size = input(f"Enter the size (width height) [Current: {size[0]} {size[1]}]: ").strip()
    if new_size:
        size = tuple(map(int, new_size.split()))

    # Update DPI if input is provided
    new_dpi = input(f"Enter the resolution (DPI) [Current: {dpi[0]}]: ").strip()
    if new_dpi:
        dpi = int(new_dpi)
        dpi = (dpi, dpi)

    # Update target_min_size if input is provided
    new_min_size = input(f"Enter the minimum target size (KB) [Current: {target_min_size}KB]: ").strip()
    if new_min_size:
        target_min_size = int(new_min_size)

    # Update target_max_size if input is provided
    new_max_size = input(f"Enter the maximum target size (KB) [Current: {target_max_size}KB]: ").strip()
    if new_max_size:
        target_max_size = int(new_max_size)


if not os.path.exists(output_folder):
    print("Making output folder...")
    os.makedirs(output_folder)
    
def resize_and_compress_image(image_path):
    # Open image
    quality=100
    img = Image.open(image_path)
    dpi = (200, 200)
    # Convert to RGB (to ensure consistent JPEG output)
    img = img.convert("RGB")
    # Resize the image
    img = img.resize(size)
    # Create a unique temporary file name
    final_image_path = os.path.join(output_folder, os.path.basename(image_path))
    def get_size(file_path):
        size = os.path.getsize(file_path)
        return size // 1024
    # Start with high quality (100) and save image
    img.save(final_image_path, dpi = dpi, quality=quality)
    img_size = get_size(final_image_path)
    n = 0
    if img_size==0:
        n = 2.5
    elif img_size<10:
        n=2
    elif img_size<20:
        n=1
    with open(final_image_path, 'ab') as f:  # Open file in append and binary mode
        f.write(b'\0' * (extra_data_size*n))  # Write null bytes to add metadata
    # Get the image size
    img_size = get_size(final_image_path)
    if img_size > target_max_size:
        print(f"Image needs compression: {os.path.basename(image_path)}")

try:    
    for image_file in os.listdir(input_folder):
        if image_file.endswith(('jpg', 'jpeg', 'png','JPG')):
            resize_and_compress_image(os.path.join(input_folder, image_file))
    print("Done!")
except Exception as e:
    print(f"An error occurred: {e}")

input("Press Enter to exit...")