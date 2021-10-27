# Importation of the libraries, PIL to manipulate images and os to get the directory path,etc...
from PIL import Image
import os

# Variables Declaration
images_files = []  # List containing the files in a folder
manga_mode = False  # True if manga mode is activated by the user
path = input("Enter a path here: ")  # The path of the directory containing the images
des_dir = input("Please enter where the file will be saved: ")  # The Path where the images have to be saved
MangaInput = input("Manga Mode (invert the lecture way) [yes/no]: ")  # Specify if you want the manga mode or not

# Manga Mode check
if MangaInput == "yes":
    manga_mode = True

elif MangaInput == "No":
    manga_mode = False

# List all the files in the given directory
directory = os.listdir(path)
print("Images are being scanned, please wait...")
for file in directory:
    images_files.append(path + "/" + file)
# Reverse the list in case of the manga mode
if manga_mode == True:
    images_files.reverse()

# Open each with PIL
images = [Image.open(x) for x in images_files]
total_width = 0
max_height = 0

print("Images are being processed, please wait...")
# Determine the max Height and the total width of the new image
for img in images:
    total_width += img.size[0]
    max_height = max(max_height, img.size[1])

# Creating the new image (in cache)
the_big_one = Image.new('RGB', (total_width, max_height))

# This is the most important, paste into the newly created image the other one, repeat this for the whole list
current_width = 0
for img in images:
    the_big_one.paste(img, (current_width, 0))
    current_width += img.size[0]

print("Images are being combined, please wait until the program finish...")
# Save the new images where you wanted to...
the_big_one.save(des_dir + '/TheBigOne.png')
print("Finished!")
