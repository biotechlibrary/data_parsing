import nibabel as nib

"""This script demonstrates how to use the nibabel package to load and analyze a NIfTI image file.

Usage: python nibabel_image_analysis.py <input_file>

Arguments:
    <input_file>: The path to a NIfTI image file (.nii or .nii.gz format) to be analyzed.

Output:
    The script outputs the following information to the console:
    - The shape of the image data array (i.e., number of voxels in x, y, z dimensions).
    - The size of the voxels in millimeters in x, y, z dimensions.
    - The mean intensity value of a 2D slice from the middle of the image.

The script loads the input NIfTI file using nibabel, extracts a 2D slice from the middle of the image, and computes its mean intensity value. The script serves as an example of how to use nibabel for basic image processing tasks.
"""

# Define the input file path
input_path = "input.nii.gz"

# Load the input file using nibabel
img = nib.load(input_path)

# Print the image dimensions and voxel size
print(f"Image shape: {img.shape}")
print(f"Voxel size: {img.header.get_zooms()}")

# Extract a 2D slice from the middle of the image
slice = img.dataobj[:,:,img.shape[2]//2]

# Compute the mean intensity value of the slice
mean_intensity = slice.mean()

# Print the mean intensity value
print(f"Mean intensity: {mean_intensity}")
