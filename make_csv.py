import os
import csv

# Specify the directory path you want to list the files from
directory_path = "path_to_files/logo"

# Create a list to store the file names
file_names = []

# Iterate through the files in the directory and append their names to the list
for filename in os.listdir(directory_path):
    if os.path.isfile(os.path.join(directory_path, filename)):
        file_names.append("logo/"+filename)

# Specify the CSV file path to save the list of file names
csv_file_path = "file_names.csv"

# Write the list of file names to a CSV file
with open(csv_file_path, mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    #writer.writerow(["File Names"])  # Optional header row
    for file_name in file_names:
        writer.writerow([file_name])

print(f"File names saved to {csv_file_path}")
