# Image Resizer and Compressor

This Python script resizes and compresses images to a target size range (in KB) while adding extra metadata to the image file. The script supports formats such as JPEG and PNG and allows you to adjust parameters like image size, DPI, and target size.

## Features
- Resize images to a specified width and height.
- Set the resolution (DPI) of the images.
- Compress images to a target size range (minimum and maximum in KB).
- Add extra metadata to the image files to increase their size, if needed.
- Automatically installs the `Pillow` library if it's not found.

## Requirements

- Python 3.x
- Pillow (automatically installed if missing)

## How to Use

1. Clone or download this repository to your local machine.
2. Place the images you want to resize and compress into a folder.
3. Run the script and provide the input folder path when prompted.

### Example Usage
```bash
python image_resizer.py
```

The script will:
- Prompt you to enter the path to the folder containing images.
- Resize all JPEG, JPG, and PNG images in the specified folder to a size of 132x132 pixels by default.
- Set the image resolution to 200 DPI.
- Compress the images so that they fall within the target size range (20KB to 30KB).
- Add 10KB of extra metadata to each image file.
- Output the compressed images in a folder named `<input_folder>_compressed`.

### Modifying Parameters

Before processing, the script will display the default parameters and ask for confirmation. If you want to change any parameters, you can enter new values; otherwise, pressing Enter will retain the current values.

- **Size**: Default 132x132 pixels (can be modified)
- **Resolution (DPI)**: Default 200 DPI (can be modified)
- **Target Minimum Size**: Default 20KB (can be modified)
- **Target Maximum Size**: Default 30KB (can be modified)
- **Extra Metadata**: Default 10KB


## Output

The processed images are saved in a new folder called `<input_folder>_compressed`. The script ensures that the compressed images remain within the specified size range. If an image exceeds the maximum size, it is flagged for further compression.

## Dependencies

This script requires the `Pillow` library for image processing. If Pillow is not installed, the script will automatically install it using `pip`.

## Error Handling

- The script will alert you if the input folder does not exist or if an image fails to process.
- All errors will be printed to the console, and the script will safely exit.

## License

This project is licensed under the [MIT License](LICENSE). 