import cv2
import json

# Define the input file paths
image_path = "image.jpg"
annotation_path = "annotation.json"

# Load the image and annotation data
img = cv2.imread(image_path)
with open(annotation_path, "r") as f:
    annotation_data = json.load(f)

# Loop through each object in the annotation data and draw a rectangle on the image
for obj in annotation_data:
    xmin, ymin, xmax, ymax = obj["bbox"]
    cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

# Display the annotated image
cv2.imshow("Annotated Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
