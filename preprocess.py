import os
from PIL import Image 

basewidth = 600
rootDir = 'data'

for dirName, subdirList, fileList in os.walk(rootDir):

        for fname in fileList:

                ext = os.path.splitext(fname)[-1].lower()
                if ext.endswith(('.jpg','.png','.bmp')):
                        img = Image.open(dirName + '/' + fname)
                        wpercent = (basewidth / float(img.size[0]))
                        hsize = int((float(img.size[1]) * float(wpercent)))
                        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
                        img.convert('RGB').save(dirName + '/' + os.path.splitext(fname)[0] + '.jpg')

                        if ext.endswith(('.png','.bmp')):   #remove duplicates
                            os.remove(dirName + '/' + fname)



