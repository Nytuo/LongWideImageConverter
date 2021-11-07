# Importation of the libraries, PIL to manipulate images and os to get the directory path,etc...
from PIL import Image
import os
from alive_progress import alive_bar


# Variables Declaration
images_files = []  # List containing the files in a folder
# The path of the directory containing the images
path = input("[?] Enter a path here: ")
# The Path where the images have to be saved and if the original files need to be deleted
eraser = input("[?] Erase the original file ? [True/False]")
if eraser == "True":
    des_dir = path
else:
    des_dir = input("[?] Please enter where the file will be saved: ")

# List all the files in the given directory
directory = os.listdir(path)
print("[i] Images are being scanned, please wait...")
with alive_bar() as bar:

    for file in directory:
        images_files.append(path + "/" + file)
    bar()
# Sorting the list in the alphabetic order
print("[i] Sorting the images by alphabetic order...")
with alive_bar() as bar:

    images_files.sort()
    bar()


# Open each with PIL
images = [Image.open(x) for x in images_files]

print("[i] Images are being divided, please wait...")
# This is the most important, for the horizontal images, create two images and fill them with the parts of the origial image
i = 0

with alive_bar() as bar:
    for img in images:
        if img.size[0] > img.size[1]:
            the_one = Image.new('RGB', (int(img.size[0]/2), int(img.size[1])))
            the_two = Image.new('RGB', (int(img.size[0]/2), int(img.size[1])))
            im1 = img.crop((0, 0,
                            img.size[0]/2, img.size[1]))
            im2 = img.crop((img.size[0]/2, 0,
                            img.size[0], img.size[1]))
            the_one.paste(im1, (0, 0))
            the_two.paste(im2, (0, 0))
            if i < 10:
                the_one.save(des_dir + "/000" + str(i)+'_part1.png')
                the_two.save(des_dir + "/000" + str(i) + '_part2.png')
            elif i >= 10 and i < 100:
                the_one.save(des_dir + "/00" + str(i)+'_part1.png')
                the_two.save(des_dir + "/00" + str(i) + '_part2.png')
            elif i >= 100 and i < 1000:
                the_one.save(des_dir + "/0" + str(i)+'_part1.png')
                the_two.save(des_dir + "/0" + str(i) + '_part2.png')
            else:
                the_one.save(des_dir + "/" + str(i)+'_part1.png')
                the_two.save(des_dir + "/" + str(i) + '_part2.png')
            os.remove(images_files[i])
        bar()
        i += 1

print("[!] Finished!")
