import nibabel as nib

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
