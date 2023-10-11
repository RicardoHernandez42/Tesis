#6578
import os
from collections import Counter
import numpy as np
import statistics
from os import listdir
from os.path import isfile, join
import shutil

count = 1
mypath1 = '/Volumes/ADATA/RRLyraetxtNuevostxtpromedio/'
onlyfiles1 = [f for f in listdir(mypath1) if isfile(join(mypath1, f))]
for c in onlyfiles1:
    shutil.copy(mypath1+c, '/Volumes/ADATA/Entrenamientotxt/')
    print(count,c)
    count=count+1
