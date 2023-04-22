from nilearn import plotting, image
import sys

"""This script loads a NIfTI image file and visualizes it using the nilearn package.

Usage: python view_nifti.py <nifti_file>

Arguments:
    <nifti_file>: The path to a NIfTI image file (.nii or .nii.gz format) to be visualized.

Output:
    A plot of the NIfTI image using nilearn's plotting functions.

If the input image is 3D, an anatomical plot will be generated. If the input image is 4D, a plot of the first volume will be generated. If the input image has any other number of dimensions, an error message will be printed.
"""

filename = sys.argv[1]  # Replace this with the path to your NIfTI file

img = image.load_img(filename)

if len(img.shape) == 3:
    plotting.plot_anat(filename)
elif len(img.shape) == 4:
    first_volume = image.index_img(filename, 0)
    plotting.plot_epi(first_volume)
else:
    print(f"Unsupported image dimension: {len(img.shape)}")

plotting.show()
