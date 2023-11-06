from PIL import Image
import random
import csv
import os

#loading csv file
csv_file_path="file_names.csv"

# List of logo file paths
logo_paths = []  # Add the paths to your logo images

with open(csv_file_path, newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        logo_paths.append(row[0]) 

template_list=["Community Partners.png","Community Partners-1.png","Community Partners-2.png","Community Partners-3.png",]

for logo_path in logo_paths:
    # Load the template file
    template = Image.open(random.choice(template_list))
    # Load the logo image
    logo = Image.open(logo_path)

    # Calculate the position to place the logo (you have to play a little)
    size = 700,400
    logo.thumbnail(size)
    width, height = logo.size
    print (width,height)
    x = 123+(956//2)-(width//2)
    y = 600 - (height//2)

    # Paste the logo onto the template
    #template.paste(logo,[x,y],logo) would work if there is no transparency
    if logo.mode in ('RGBA', 'LA') or (logo.mode == 'P' and 'transparency' in logo.info):
        # If the logo has an alpha channel, paste it with a mask
        template.paste(logo, (x, y), logo)
    else:
        # If the logo does not have an alpha channel, paste it without a mask
        template.paste(logo, (x, y))

    # Save the modified template with the logo
    output_path = r"path_to_save\output" + "\\" + os.path.basename(logo_path)
    template.save(output_path, "PNG")

# Close the template image
template.close()
