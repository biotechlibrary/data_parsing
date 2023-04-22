# data_parsing

This repository contains scripts for parsing and converting various types of data files.

## Scripts

### `convert_1d_to_nifti.py`

Converts a 1D text file of fMRI time series into a NIfTI image file.

Usage: 
```
python convert_1d_to_nifti.py <input_file> <output_file> <tr>
```

Arguments:
- `<input_file>`: The path to a 1D text file containing fMRI time series data (e.g., output from FSL's `fslmeants` command).
- `<output_file>`: The desired path and filename of the output NIfTI image file (.nii or .nii.gz format).
- `<tr>`: The repetition time (TR) of the fMRI data in seconds.

Output:
- A NIfTI image file of the fMRI time series data, with voxel-wise time courses represented as image volumes.

### `json_2_csv.py`

Converts a JSON file to a CSV file.

Usage: 
```
python json_2_csv.py <input_file> <output_file>
```

Arguments:
- `<input_file>`: The path to a JSON file to be converted.
- `<output_file>`: The desired path and filename of the output CSV file.

Output:
- A CSV file containing the same data as the input JSON file.

### `json_2_yolov5.py`

Converts a JSON file containing object detection annotations to a YOLOv5-compatible format.

Usage: 
```
python json_2_yolov5.py <input_file> <output_file>
```

Arguments:
- `<input_file>`: The path to a JSON file containing object detection annotations.
- `<output_file>`: The desired path and filename of the output YOLOv5 file.

Output:
- A YOLOv5 file containing the same object detection annotations as the input JSON file.

### `nibabel_image_analysis.py`

Demonstrates how to use the nibabel package to load and analyze a NIfTI image file.

Usage: 
```
python nibabel_image_analysis.py <input_file>
```

Arguments:
- `<input_file>`: The path to a NIfTI image file to be analyzed.

Output:
- The shape of the image data array (i.e., number of voxels in x, y, z dimensions).
- The size of the voxels in millimeters in x, y, z dimensions.
- The mean intensity value of a 2D slice from the middle of the image.

### `overlay_img_files.py`

Overlays two NIfTI image files and saves the result as a PNG file.

Usage:
```
python overlay_img_files.py <input_file_1> <input_file_2> <output_file>
```

Arguments:
- `<input_file_1>`: The path to the first NIfTI image file to be overlaid.
- `<input_file_2>`: The path to the second NIfTI image file to be overlaid.
- `<output_file>`: The desired path and filename of the output PNG file.

Output:
- A PNG file showing the overlay of the two input NIfTI images.

### view_nifti.py
Loads a NIfTI image file and visualizes it using the nilearn package.

Usage: python view_nifti.py <nifti_file>

Arguments:

<nifti_file>: The path to a NIfTI image file to be visualized.
Output:

A plot of the NIfTI image using nilearn's plotting functions.
If the input image has three dimensions, it will be displayed as an anatomical image. If the input image has four dimensions, the first volume of the image will be displayed as an EPI image. If the input image has more than four dimensions, an error message will be printed.

