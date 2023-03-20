import json

# Define the input and output file paths
input_path = "input.json"
output_path = "output.txt"

# Open the input file and load the JSON data
with open(input_path, "r") as input_file:
    data = json.load(input_file)

# Open the output file for writing
with open(output_path, "w") as output_file:
  
    # Loop through each object in the JSON data
    for obj in data:
      
        # Get the object class and bounding box coordinates
        obj_class = obj["class"]
        bbox = obj["bbox"]
        xmin, ymin, xmax, ymax = bbox["xmin"], bbox["ymin"], bbox["xmax"], bbox["ymax"]
        
        # Convert the coordinates to YOLO format (normalized values between 0 and 1)
        img_width, img_height = 640, 480  # Replace with actual image dimensions
        x_center, y_center = (xmin + xmax) / 2 / img_width, (ymin + ymax) / 2 / img_height
        width, height = (xmax - xmin) / img_width, (ymax - ymin) / img_height
        
        # Write the object data to the output file in YOLO format
        output_file.write(f"{obj_class} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")
