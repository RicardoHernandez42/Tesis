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

MiQSO = []
ID = []

for line in text3:
    MiQSO.append(line[134:142])
    ID.append(line[5:12])
MiQSO = np.array(MiQSO,dtype=np.float64,order="C")
ID = np.array(ID,dtype=np.float64,order="C")
#print(MiQSO)
for i in range(0,len(MiQSO)):
    print('LC_',ID[i])
    if MiQSO[i] != -9.9:
        d=str(int(ID[i]))
        shutil.move('/Volumes/ADATA/Pruebatxt/LC_'+d+'_completo_promedio.txt', '/Volumes/ADATA/AllLC_promedio/')
#        shutil.move('/Volumes/ADATA/Pruebatxt/LC_'+d+'_completo_promedio.txt', '/Volumes/ADATA/Entrenamientotxt/')
#    else:
#        d=str(int(ID[i]))
#        shutil.copy('/Volumes/ADATA/AllLC_promedio/LC_'+d+'_completo_promedio.txt', '/Volumes/ADATA/Entrenamientotxt/')
