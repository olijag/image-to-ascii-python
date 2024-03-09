This program converts images into ASCII art, transforming pixels from a specified image into characters based on their brightness levels. 
It uses the Python Imaging Library (PIL) to open, convert to grayscale, and resize the image for a uniform ASCII representation. 
The core of the program maps each pixel's brightness to a character from a predefined ASCII palette, ranging from dark to light symbols. 
This conversion creates a text representation of the image, preserving its essential visual details through the contrast of ASCII characters. 
The resulting ASCII art is then saved to a text file, allowing for easy sharing and viewing.


Usage:
To convert an image to ASCII art, place the image file in the same directory as this script or provide an absolute path. 
Update the 'path' variable with the image file's name (e.g., 'mona_lisa.jpg'). 
Run the script, and the ASCII art will be generated and saved to 'test.txt' in the current directory.
