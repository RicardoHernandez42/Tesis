import os
from os import listdir
from os.path import isfile, join


mypath = '/Users/richo/OneDrive - Fundacion Universidad de las Americas Puebla/Honores/AllLCs'
carpeta = '/Users/richo/OneDrive - Fundacion Universidad de las Americas Puebla/Honores/AllLCs'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for c in onlyfiles:
    print(mypath + '/' + c)
