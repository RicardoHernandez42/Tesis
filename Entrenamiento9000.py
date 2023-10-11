import os
from collections import Counter
import numpy as np
import statistics
from os import listdir
from os.path import isfile, join
import shutil
count = 1
mypath = '/Users/richo/Downloads/QSO_S82'
path_s82 = '/Volumes/ADATA/Pruebatxt'
target_dir = '/Volumes/ADATA/Entrenamientotxt/'
target_dir2 = '/Volumes/ADATA/Entrenamientotxt2/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for c in onlyfiles:
    file = os.path.splitext(c)[0]
    new_file = path_s82+'/LC_'+file+'_completo_promedio.txt'
    if (isfile(new_file)):
        shutil.move(new_file, target_dir)
        print(count, c, 'sí')
        count=count+1
    else:
        shutil.copy(mypath+'/'+c, target_dir2)
        print(count,c, 'no')
        count=count+1
