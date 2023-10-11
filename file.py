import os
from collections import Counter
import numpy as np
import statistics
from os import listdir
from os.path import isfile, join


mypath = '/Users/richo/OneDrive - Fundacion Universidad de las Americas Puebla/Honores/AllLCs'
carpeta = '/Users/richo/OneDrive - Fundacion Universidad de las Americas Puebla/Honores/AllLCs'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
with open('/Volumes/ADATA/File.txt', 'w') as out:
    for c in onlyfiles:
        file = os.path.splitext(c)[0]
        out.write(file + '\n')
    
