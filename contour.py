# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 13:18:19 2018

@author: Amit
"""
from PIL import Image
im = Image.open('circle.png')
width, height = im.size

def rgb_of_pixel(x, y):
    r, g, b = im.getpixel((x, y))
    a = (r, g, b)
    return a


all_pixels = []
for x in range(width):
    for y in range(height):
        all_pixels.append(rgb_of_pixel(x, y))
       