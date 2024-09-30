# Image Resizer and Compressor (v2)

## Description
`image_resizer_v2.py` is a Python script with a graphical user interface (GUI) built using Tkinter. The script allows you to resize and compress images to fit within a specified file size range (in KB). Additionally, the script appends extra metadata to the image file, making it suitable for managing image sizes for specific applications.

The script processes images in a user-specified input folder and saves the resized and compressed images to an output folder. The user can adjust the image dimensions, DPI (dots per inch), and target file size through the GUI.

## Features
- **Graphical User Interface (GUI)**: Simple Tkinter-based GUI for easy user interaction.
- **Image Resizing**: Resizes images to user-specified dimensions (width x height in pixels).
- **Image Compression**: Compresses images to fit within a specified size range (in KB).
- **Extra Metadata**: Adds extra metadata to the images to reach the target file size range.
- **Supported Formats**: Works with `.jpg`, `.jpeg`, and `.png` image formats.
- **Automatic Folder Creation**: Creates the output folder if it does not exist.

## Screenshots
<p align="center">
<img src="assets\Screenshot.jpg" width="75%" />
</p>

## Prerequisites

- **Python 3.x**: The script runs on Python 3.x. Ensure that Python is installed on your system.
- **Pillow**: The script uses the Pillow library to manipulate images. Pillow is automatically installed if it is not already available.

## Installation

1. Clone or download the script to your local machine.
2. Ensure that the necessary Python libraries are installed. The script will automatically install Pillow if it is missing.

```bash
pip install Pillow
```

## How to Use

1. Clone or download this repository to your local machine.
2. Place the images you want to resize and compress into a folder.
3. Run the script and provide the input folder path when prompted.

### Example Usage
```bash
python image_resizer_v2.py
```

## How It Works

1. **Select Folders**: Users can select the input and output folders using a file dialog.
   - The **Input Folder** contains the images you want to resize and compress.
   - The **Output Folder** is where the processed images will be saved.
   
2. **Adjust Parameters**: 
   - **Image Dimensions**: Set the target width and height for resizing (default: 132x132 pixels).
   - **DPI**: Set the image resolution (default: 200 DPI).
   - **File Size**: Set the target minimum and maximum file size (in KB).
   - **Extra Metadata**: Adds 10KB of extra metadata to each image file to reach the desired size range.

3. **Processing**:
   - The script will resize and compress each image in the input folder.
   - Images are saved in the output folder with the new dimensions and file size.
   - If an image exceeds the target file size, it will be flagged for further compression.



## Error Handling
- The script will check for the existence of the input and output folders.
- Errors encountered during the image processing will be printed in the console, and the script will exit safely.

## Dependencies
- **Pillow**: Image processing library.

## Previous Versions
- [Version 1.0](./Older%20Versions/V1.0/README.md)  
## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.