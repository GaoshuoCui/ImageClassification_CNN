import os
import shutil

root = os.getcwd()+'/train'
allfile=os.listdir(root)
print(len(allfile))
jpg_dir = os.getcwd()+'/tryimg'
xml_dir = os.getcwd()+'/tryxml'

for i in allfile:
    if i[-4:]=='.jpg':
        shutil.move(root+'/'+i,jpg_dir+'/'+i)
    elif i[-4:]=='.xml':
        shutil.move(root+'/'+i,xml_dir+'/'+i)