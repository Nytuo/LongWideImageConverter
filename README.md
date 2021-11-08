# Python Tools

This is a set of tools in python that I have created.

# decomposer.py

Needed modules:

- PIL (Pillow)
- os
- alive_progress (for the progressbar, you could edit the code to remove it)

This is an image decomposer that take a folder of images and detect horizontal images and divide them by two.

# ImageDownloader.py

This tool get all images on a website (provided by a URL or a file containing URLs) and download them into a destination folder (a "out" folder where the python file is stored is created and more if there are a list of URL to download).
To get it work you just have to specify the form, the URL and wait for the magic.
Designed to scrap manga scan.

Needed modules:

- bs4 (beautifulSoup4)
- requests
- shutil
- os
- alive_progress (for the progressbar, you could edit the code to remove it)

# LongWideImageConverter.py

Did you ever wanted to have all your images in only one ? Now it's possible.

This little python Program help you to have all your images in one file!
I made it to get one image of my manga/comics which are miscropped (but can be used in other ways).

To use it, very simple, run the python file in a IDE with the PIL (pillow) module installed and follow the instructions on screen.

- Enter the path of the directory containing the images.
- Enter the path of a directory which will contains the new one.
- Indicate if it is a manga or not (IF you want it reversed or not)
- Wait until it's finish

Needed modules:

- PIL (pillow)
- os
- alive_progress (for the progressbar, you could edit the code to remove it)
