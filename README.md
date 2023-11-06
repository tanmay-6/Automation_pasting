# Automation_pasting
Cool trick to save a lot of manual work as a designer!

There is this python library named #PILLOW which works with images.
To install it simply run: pip install Pillow
https://pypi.org/project/Pillow/ (documentation)

TIP : Follow the main.py file to go through the code.
Save all the logos in a directory (relative addresses in my case).
Make the csv file for all the names. (see make_csv.py for code)
After that read the csv in main file, and make a list of all the logo files (you can also iterate through csv I just felt secured to do so :P)
Now take the template file and loop for all the logos/images.
Inside the loop I have resized the logo/image using thumbnail function. (logos which were too large to handle you can also explore image.resize() funtion in documentation)
Then you can go with pasting each logo on to template while saving all the files in the output directory.

NOTE: I had some logos with transparency so have to add a transparency mask and therefore have to use if/else.

There you go 100 logos pasted in 2 seconds and one click. ( Cheers to chatgpt XD )
