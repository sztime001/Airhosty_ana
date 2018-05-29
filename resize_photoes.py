# -*- coding: utf-8 -*-
"""
Created on Mon May 28 17:31:20 2018

@author: Sofei
"""




import os, sys
import argparse
import shutil
import os
import os.path
import ast
from datetime import datetime
from PIL import Image, ImageFont, ImageDraw, ImageEnhance

#path_in = "C:\\Users\\Sofei\\OneDrive\\photo with mark resized to 1920_1080\\Lindfield, 10,15-19, Havliah Road\\"
#path_out = "C:\\Users\\Sofei\\OneDrive\\photo with mark resized to 1920_1080\\Lindfield, 10,15-19, Havliah Road\\Resized\\"
#dirs = os.listdir(path_in)
#
#def resize(path_in,path_out):
#    for item in dirs:
#        if os.path.isfile(path_in+item):
#            im = Image.open(path_in+item)
#            f, e = os.path.splitext(path_out+item)
#            imResize = im.resize((1920,1080), Image.ANTIALIAS)
#            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)
#
#resize(path_in,path_out)

path_in = "C:\\Users\\Sofei\\OneDrive\\photo with mark resized to 1920_1080\\Lindfield, 10,15-19, Havliah Road\\Resized\\"
path_out = "C:\\Users\\Sofei\\OneDrive\\photo with mark resized to 1920_1080\\Lindfield, 10,15-19, Havliah Road\\Watermarked\\"
dirs = os.listdir(path_in)

def watermark_image_with_text(path_in,path_out, text, color, fontfamily):
    for item in dirs:
        if os.path.isfile(path_in+item):
            image = Image.open(path_in+item).convert("RGBA")
            imageWatermark = Image.new('RGBA', image.size, (255, 255, 255, 0))

            draw = ImageDraw.Draw(imageWatermark)
    
            width, height = image.size
            margin = 20
            font = ImageFont.truetype(fontfamily, int(height / 8))
            textWidth, textHeight = draw.textsize(text, font)
            x = width/2 - textWidth/2
            y = height/2 - textHeight/2

            draw.text((x, y), text, color, font)

            imWatermark = Image.alpha_composite(image, imageWatermark)
            f, e = os.path.splitext(path_out+item)
            imWatermark = imWatermark.convert('RGB')
            imWatermark.save(f + ' watermarked.jpg', 'JPEG', quality=90)

watermark_image_with_text(path_in,path_out, 'AIRHOSTY', (220,220,220,150),'arial')
