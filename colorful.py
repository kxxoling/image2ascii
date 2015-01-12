# coding: utf-8
from PIL import Image


ASCII_PIXELS = "MNHQ$OC?7>!:-;. "


def convert_image_to_ascii(img):
    ascii_html = '''
<html><head><style>span.char {
display: inline-block;
height: 10px;
width: 10px;
font-size: 10px;
}</style></head><body>'''
    orig_width, orig_height = img.size
    width = 150
    height = width * orig_height / orig_width

    img = img.resize((width, height))
    pixels = img.load()

    for h in xrange(height):
        ascii_html += '<div class="line">'
        for w in xrange(width):
            pixel = list(pixels[w, h])
            if len(pixel) == 3:
                pixel.append(1)
            ascii_char = ASCII_PIXELS[int(sum(pixel[:3]) / 3.0 / 256.0 * 16)]
            ascii_html += '<span class="char" style="color: rgba%s">%s</span>' % (tuple(pixel), ascii_char)

        ascii_html += '</div>\n'
    ascii_html += '</body></html>'

    return ascii_html


if __name__ == '__main__':
    img_name = 'meiling.jpg'
    img = Image.open(img_name)
    file_name = img_name.rsplit('.')[0]
    with open(file_name+'.html', 'w+') as target_file:
        target_file.write(convert_image_to_ascii(img))
