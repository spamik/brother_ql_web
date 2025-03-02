# -*- coding: utf-8 -*-

from PIL import Image
from io import BytesIO
from pdf2image import convert_from_bytes


def convert_image_to_bw(image, threshold, high_threshold=200):
    #fn = lambda x : 255 if x > threshold else 0
    #return image.convert('L').point(fn, mode='1') # convert to greyscale
    greyscale = image.convert('L')
    new_pixels = []
    for x in greyscale.getdata():
        if x <= threshold:
            new_pixels.append((0, 0, 0))
        elif x <= high_threshold:
            new_pixels.append((255, 0, 0))
        else:
            new_pixels.append((255, 255, 255))
    result = Image.new('RGB', greyscale.size)
    result.putdata(new_pixels)
    return result


def imgfile_to_image(file):
    s = BytesIO()
    file.save(s)
    im = Image.open(s)
    return im


def pdffile_to_image(file, dpi):
    s = BytesIO()
    file.save(s)
    s.seek(0)
    im = convert_from_bytes(
        s.read(),
        dpi = dpi
    )[0]
    return im


def image_to_png_bytes(im):
    image_buffer = BytesIO()
    im.save(image_buffer, format="PNG")
    image_buffer.seek(0)
    return image_buffer.read()
