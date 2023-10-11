import shutil
import os
import numpy as np
from collections import Counter
import os
from os import listdir
from os.path import isfile, join

g = open('/Users/richo/OneDrive - Fundacion Universidad de las Americas Puebla/Honores/stripe82candidateVar.txt')
#/Users/richo/OneDrive\ -\ Fundacion\ Universidad\ de\ las\ Americas\ Puebla/Honores/stripe82candidateVar.txt 
text3 = g.readlines()
g.close()
text3 = text3[1:]

zQSO = []
ID = []

for line in text3:
    zQSO.append(line[127:134])
    ID.append(line[5:12])
zQSO = np.array(zQSO,dtype=np.float64,order="C")
ID = np.array(ID,dtype=np.float64,order="C")

for i in range(0,len(zQSO)):
    print('LC_',ID[i],'num',i)
    if zQSO[i] == -9.9:
        d=str(int(ID[i]))
        shutil.copy('/Volumes/ADATA/AllLC_promedio/LC_'+d+'_completo_promedio.txt', '/Volumes/ADATA/Pruebatxt/')
    else:
        d=str(int(ID[i]))
        shutil.copy('/Volumes/ADATA/AllLC_promedio/LC_'+d+'_completo_promedio.txt', '/Volumes/ADATA/Entrenamientotxt/')
