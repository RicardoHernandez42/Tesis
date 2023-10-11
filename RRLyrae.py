import os
from collections import Counter
import numpy as np
import statistics
from os import listdir
from os.path import isfile, join
import shutil

path_rrl = '/Volumes/ADATA/table1'
path_s82 = '/Volumes/ADATA/Pruebatxt'
target_dir = '/Volumes/ADATA/RRLyraetxt'
target_dir2 = '/Volumes/ADATA/RRLyraetxtNuevos'
onlyfiles = [f for f in listdir(path_rrl) if isfile(join(path_rrl, f))]


count=1
count1= 1
for c in onlyfiles:
    file = os.path.splitext(c)[0]
    new_file = path_s82+'/LC_'+file+'_completo_promedio.txt'
    #print(c)
    if (isfile(new_file)):
        shutil.move(new_file, target_dir)
        print(count)
        count=count+1
    else:
        shutil.copy(path_rrl+'/'+c, target_dir2)
        print(file, 'este archivo no se encuentra:', count1)
        count1=count1+1
#        print(file)
    
#print(len(onlyfiles))
    #shutil.move('/Volumes/ADATA/Pruebatxt/LC_'+file+'_completo_promedio.txt', '/Volumes/ADATA/RRLyraetxt')
#   if '/Volumes/ADATA/Pruebatxt/LC_'+file+'_completo_promedio.txt' in '/Volumes/ADATA/Pruebatxt':
