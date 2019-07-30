#!/usr/bin/env python
# coding: utf-8

# ### Code for RGB To GRAYSCALE

# In[41]:


import cv2
from os import listdir,makedirs
from os.path import isfile,join

path = r'C:\\Users\\admin\\Desktop\\Tabarka Rajab\\tz\\' # Source Folder
dstpath = r'C:\\Users\\admin\\Desktop\\Tabarka Rajab\\tz\\' # Destination Folder

try:
    makedirs(dstpath)
except:
    print ("Directory already exist, images will be written in asme folder")

# Folder won't used
files = [f for f in listdir(path) if isfile(join(path,f))] 

for image in files:
    try:
        img = cv2.imread(os.path.join(path,image))
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        dstPath = join(dstpath,image)
        cv2.imwrite(dstPath,gray)
    except:
        print ("{} is not converted".format(image))


# ### Code for Image Resizing

# In[40]:


from PIL import Image
import os, sys

path = "C:\\Users\\admin\\Desktop\\Tabarka Rajab\\tz\\"
dirs = os.listdir( path )
print(dirs)

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((200,200), Image.ANTIALIAS)
            print(imResize)
            imResize.save(f + '.jpg', 'JPEG', quality=90)

resize()
print(resize())
print(resize(count()))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# 

# In[ ]:





# In[ ]:




