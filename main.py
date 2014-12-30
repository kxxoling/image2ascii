# coding: utf-8
from PIL import Image


ASCII_PIXELS = "MNHQ$OC?7>!:-;. "

def convert_image_to_ascii(img):
    ascii_string = ''
    orig_width, orig_height = img.size
    width = 50
    height = width * orig_height / orig_width

    img = img.resize((width, height))
    pixels = img.load()

    for h in xrange(height):
        for w in xrange(width):
            pixel = pixels[w, h]
            ascii_string += ASCII_PIXELS[int(sum(pixel) / 3.0 / 256.0 * 16)]

        ascii_string += '\n'

    return ascii_string


if __name__ == '__main__':
    len = Image.open('chooser_sa.png')
    print convert_image_to_ascii(len)
