import json
import csv

# Define the input and output file paths
input_path = "input.json"
output_path = "output.csv"

# Open the input file and load the JSON data
with open(input_path, "r") as input_file:
    data = json.load(input_file)

# Extract the field names from the first object in the JSON data
field_names = list(data[0].keys())

# Open the output file for writing
with open(output_path, "w", newline='') as output_file:
    # Create a CSV writer object and write the field names to the first row
    writer = csv.DictWriter(output_file, fieldnames=field_names)
    writer.writeheader()

    # Loop through each object in the JSON data and write it to the CSV file
    for obj in data:
        writer.writerow(obj)
