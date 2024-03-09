from PIL import Image

# Open image, set the path to the image here
path = "mona_lisa.jpg"

# ASCII characters table - from darkest to brightest
ascii_chars = ('@#&%?*^=+-:.' )

# Convert image to ascii 
def map_pixel_to_ascii(pixel_brightness, ascii_chars):
    normalized_brightness = pixel_brightness / 255.0

    scale_factor = len(ascii_chars) - 1
    ascii_index = int(normalized_brightness * scale_factor)
    
    return ascii_chars[ascii_index]

def image_to_ascii(image_path, ascii_chars):
    with Image.open(image_path) as img:
        img = img.convert("L")
        img = img.resize((100,100))

        width, height = img.size

        ascii_art = ""

        for y in range(height):
            for x in range(width):
                brightness = img.getpixel((x,y))

                corresponding_ascii_char = map_pixel_to_ascii(brightness, ascii_chars)
                ascii_art += corresponding_ascii_char

            ascii_art += '\n'
    
    f = open("image_to_ascii.txt", "w")
    f.write(ascii_art)

# Example usage
converted_ascii_art = image_to_ascii(path, ascii_chars)

# The output should result in a new file called "image_to_ascii.txt"