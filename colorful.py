# coding: utf-8
from PIL import Image


ASCII_PIXELS = "MNHQ$OC?7>!:-;. "

def convert_image_to_ascii(img):
    ascii_html = '''
<html><head><style>span.char {
display: inline-block;
height: 10px;
width: 10px;
}</style></head><body>'''
    orig_width, orig_height = img.size
    width = 50
    height = width * orig_height / orig_width

    img = img.resize((width, height))
    pixels = img.load()

    for h in xrange(height):
        ascii_html += '<div class="line">'
        for w in xrange(width):
            pixel = pixels[w, h]
            ascii_char = ASCII_PIXELS[int(sum(pixel) / 3.0 / 256.0 * 16)]
            ascii_html += '<span class="char" style="color: rgba%s">%s</span>' % (pixel, ascii_char)

        ascii_html += '</div>\n'
    ascii_html += '</body></html>'

    return ascii_html


if __name__ == '__main__':
    len = Image.open('chooser_sa.png')
    print convert_image_to_ascii(len)
