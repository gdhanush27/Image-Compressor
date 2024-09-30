# This is the updated version of the script that uses a GUI to select input and output folders, and set parameters for resizing and compressing images. 
# The script uses Tkinter for the GUI and PIL (Pillow) for image processing.

import warnings
warnings.simplefilter("ignore", DeprecationWarning)

import subprocess
import sys
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

# Install Pillow if not present
try:
    from PIL import Image
except ImportError:
    print("Pillow (PIL) not found, installing Pillow...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image
    print("Pillow installed and imported successfully!")

# Function to select input folder
def select_input_folder():
    folder = filedialog.askdirectory(title="Select Input Folder")
    input_folder_var.set(folder)

# Function to select output folder
def select_output_folder():
    folder = filedialog.askdirectory(title="Select Output Folder")
    output_folder_var.set(folder)

# Function to resize and compress images
def resize_and_compress_image(image_path, output_folder, size, dpi, extra_data_size, target_min_size, target_max_size):
    quality = 100
    img = Image.open(image_path)
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
    img.save(final_image_path, dpi=dpi, quality=quality)
    img_size = get_size(final_image_path)
    n = int(target_max_size-target_min_size) // 10  # Number of iterations for compression

    # Write extra metadata
    with open(final_image_path, 'ab') as f:  # Open file in append and binary mode
        f.write(b'\0' * (extra_data_size * n))  # Write null bytes to add metadata

    # Get the image size
    img_size = get_size(final_image_path)
    if img_size > target_max_size:
        print(f"Image needs compression: {os.path.basename(image_path)}")

# Function to process images
def process_images():
    input_folder = input_folder_var.get().strip()
    output_folder = output_folder_var.get().strip()
    
    # Ensure folders exist
    if not os.path.exists(input_folder):
        messagebox.showerror("Error", "Input folder does not exist.")
        return
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get parameters from user input
    try:
        size = (int(width_var.get()), int(height_var.get()))
        dpi = (int(dpi_var.get()), int(dpi_var.get()))
        target_min_size = int(min_size_var.get())
        target_max_size = int(max_size_var.get())
        extra_data_size = 10240  # Default 10KB of extra metadata
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")
        return

    # Process each image
    try:
        for image_file in os.listdir(input_folder):
            if image_file.lower().endswith(('jpg', 'jpeg', 'png')):
                resize_and_compress_image(
                    os.path.join(input_folder, image_file), output_folder, size, dpi, extra_data_size, target_min_size, target_max_size
                )
        messagebox.showinfo("Success", "All images have been processed.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Tkinter window setup
root = tk.Tk()
root.title("Image Resizer and Compressor")

# Input folder selection
input_folder_var = tk.StringVar()
tk.Label(root, text="Input Folder:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=input_folder_var, width=40).grid(row=0, column=1, padx=10)
tk.Button(root, text="Browse", command=select_input_folder).grid(row=0, column=2, padx=10)

# Output folder selection
output_folder_var = tk.StringVar()
tk.Label(root, text="Output Folder:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=output_folder_var, width=40).grid(row=1, column=1, padx=10)
tk.Button(root, text="Browse", command=select_output_folder).grid(row=1, column=2, padx=10)

# Image size
tk.Label(root, text="Width:").grid(row=2, column=0, padx=10, pady=10)
width_var = tk.StringVar(value="132")
tk.Entry(root, textvariable=width_var, width=10).grid(row=2, column=1, sticky='w')

tk.Label(root, text="Height:").grid(row=2, column=1, padx=10, pady=10)
height_var = tk.StringVar(value="132")
tk.Entry(root, textvariable=height_var, width=10).grid(row=2, column=1, sticky='e')

# DPI setting
tk.Label(root, text="DPI:").grid(row=3, column=0, padx=10, pady=10)
dpi_var = tk.StringVar(value="200")
tk.Entry(root, textvariable=dpi_var, width=10).grid(row=3, column=1, sticky='w')

# Target size settings
tk.Label(root, text="Min Size (KB):").grid(row=4, column=0, padx=10, pady=10)
min_size_var = tk.StringVar(value="20")
tk.Entry(root, textvariable=min_size_var, width=10).grid(row=4, column=1, sticky='w')

tk.Label(root, text="Max Size (KB):").grid(row=4, column=1, padx=10, pady=10)
max_size_var = tk.StringVar(value="30")
tk.Entry(root, textvariable=max_size_var, width=10).grid(row=4, column=1, sticky='e')

# Process images button
tk.Button(root, text="Process Images", command=process_images).grid(row=5, column=0, columnspan=3, pady=20)

# Run the Tkinter main loop
root.mainloop()
