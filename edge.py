# coding: utf-8
from PIL import Image



def convert_image_to_ascii(img):
    ascii_string = ''
    orig_width, orig_height = img.size
    width = 50
    height = width * orig_height / orig_width

    img = img.resize((width, height)).convert('1')
    pixels = img.load()

    def get_char(x, y):
        #return pixels[x, y] and ' ' or '.'
        if not x or not y or x==width-1 or y==height-1:
            return ' '

        if not pixels[x,y]:
            if pixels[x+1,y] and pixels[x,y+1]:
                return '/'
            elif pixels[x-1,y] and pixels[x,y+1]:
                return '\\'
            elif pixels[x+1,y] and pixels[x,y-1]:
                return '\\'
            elif pixels[x-1,y] and pixels[x,y-1]:
                return '/'
            elif pixels[x,y-1]:
                return '_'
            elif pixels[x+1,y] or pixels[x-1,y]:
                return '|'
        #    elif not pixels[x,y-1] and not pixels[x+1,y-1] and not pixels[x-1,y-1]:
        #        return '_'
        return ' '


    for h in xrange(height):
        for w in xrange(width):
            pixel =  get_char(w, h)

            ascii_string += pixel

        ascii_string += '\n'

    return ascii_string


if __name__ == '__main__':
    len = Image.open('chooser_sa.png')
    print convert_image_to_ascii(len)
