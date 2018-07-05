# -*- coding: utf-8 -*-
"""
Created on Mon May 28 17:31:20 2018

@author: Sofei
"""



import os, sys
import argparse
import shutil
import os.path
import ast
from datetime import datetime
from PIL import Image, ImageFont, ImageDraw, ImageEnhance



def watermark_image_with_text(im, text, color, fontfamily):
    im = im.convert('RGBA')
    imageWatermark = Image.new('RGBA', im.size, (255, 255, 255,0))

    draw = ImageDraw.Draw(imageWatermark)
    
    width, height = im.size
    margin = 10
    font = ImageFont.truetype(fontfamily, int(height/8))
    textWidth, textHeight = draw.textsize(text, font)
    x = width/2 - textWidth/2
    y = height/2 - textHeight/2

    draw.text((x, y), text, color, font)
    imWatermark = Image.alpha_composite(im, imageWatermark)
    imWatermark = imWatermark.convert('RGB')

    return imWatermark

def resize_image(im):
    #if the picture is vetical, rotate it to horizonal  
    rotate_flag = 0
    width, height = im.size
    if width < height:
        im = im.rotate(90)
        rotate_flag = 1
    #evaluate if resolution exceeds 1920*1080  
    width, height = im.size
    if 1920/width > 1080/height:
        width_re = 1920
        height_re = 1920/width*height
        im = im.resize((int(width_re),int(height_re)), Image.ANTIALIAS)
    else:
        height_re = 1080
        width_re = 1080/height*width
        im = im.resize((int(width_re),int(height_re)), Image.ANTIALIAS)
    if rotate_flag:
            im = im.rotate(-90)
            
    return im
        

path_in = 'C:/Users/Sofei/OneDrive/Properties/'
path_out = 'C:/Users/Sofei/OneDrive/Properties/'
dirs_root = os.listdir(path_in)
#for item_f in dirs_root:
for i in range(33,34):
    print('...executing folder No. ' + str(i) + '         ' + str(i/32*100) + '%')
    item_f = dirs_root[i]
#item_f = 'Lindfield, 10,15-19, Havliah Road\\'
    path_folder = os.chdir(path_in+item_f+'/Property Photos/')
    dirs = os.listdir(path_folder)
    for item in dirs:
        if os.path.isfile(path_in+item_f+'/Property Photos/'+item):
            #1. open image file 
            im = Image.open(path_in+item_f+'/Property Photos/' +item)      
            width, height = im.size
            
            #2. add watermark
            im = watermark_image_with_text(im, 'AIRHOSTY', (220,220,220,150),'arial')
            #save marked pictures
            dirs_out = os.chdir(path_out+item_f+'/Property Photos/')
            if not os.path.exists(path_out+item_f+'/Property Photos/'+'Watermarked/'):
                os.makedirs(path_out+item_f+'/Property Photos/'+'Watermarked/')
            f,e =  os.path.splitext(path_out+item_f+'/Property Photos/'+'Watermarked/'+item)
            im.save(f + ' watermarked.jpg', 'JPEG', quality=100)
            
            #3. resize pictures
            im = resize_image(im)
            #save resized pictures
            dirs_out = os.chdir(path_out+item_f+'/Property Photos/')
            if not os.path.exists(path_out+item_f+'/Property Photos/'+'Resized/'):
                os.makedirs(path_out+item_f+'/Property Photos/'+'Resized/')
            f,e =  os.path.splitext(path_out+item_f+'/Property Photos/'+'Resized/'+item)
            im.save(f + ' resized.jpg', 'JPEG', quality=100) 

            

        
