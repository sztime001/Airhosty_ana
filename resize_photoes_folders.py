# -*- coding: utf-8 -*-
"""
Created on Mon May 28 17:31:20 2018

@author: Sofei
"""



from PIL import Image
import os, sys

path_root = 'C:\\Users\\Sofei\\OneDrive\\photo with mark\\'
path_out = 'C:\\Users\\Sofei\\OneDrive\\photo with mark resized to 1920_1080\\'
dirs_root = os.listdir(path_root)
for item_f in dirs_root:
#item_f = 'Lindfield, 10,15-19, Havliah Road\\'
    path_folder = os.chdir(path_root+item_f+'\\')
    dirs = os.listdir(path_folder)
    for item in dirs:
        if os.path.isfile(path_root+item_f+'\\'+item):
            im = Image.open(path_root+item_f+'\\' +item)
            imResize = im.resize((1920,1080), Image.ANTIALIAS)
            dirs_out = os.chdir(path_out)
            if not os.path.exists(path_out+item_f):
                os.makedirs(path_out+item_f)
            f,e =  os.path.splitext(path_out+item_f+'\\'+item)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

#path_out = "C:\\Users\\Sofei\\OneDrive\\photo with mark resized to 1920_1080\\Lindfield, 10,15-19, Havliah Road\\"
#dirs = os.listdir( path_in )
#
#def resize():
#    for item in dirs:
#        if os.path.isfile(path_in+item):
#            im = Image.open(path_in+item)
#            f, e = os.path.splitext(path_out+item)
#            imResize = im.resize((1920,1080), Image.ANTIALIAS)
#            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)
#
#resize()