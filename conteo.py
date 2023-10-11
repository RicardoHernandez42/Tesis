import shutil
import os
import numpy as np
from collections import Counter
import os
from os import listdir
from os.path import isfile, join

g = open('/Users/richo/Downloads/stripe82candidateVar_v1.1-1.dat')
#/Users/richo/OneDrive\ -\ Fundacion\ Universidad\ de\ las\ Americas\ Puebla/Honores/stripe82candidateVar.txt
line1 = next(g)
line2=next(g)
line3=next(g)
line4=next(g)
line5=next(g)
line6=next(g)
line7=next(g)
text3 = g.readlines()
g.close()
text3 = text3[1:]

zQSO = []
ID = []
QSO = []
NO = []

for line in text3:
    zQSO.append(line[127:134])
    ID.append(line[5:12])
zQSO = np.array(zQSO,dtype=np.float64,order="C")
ID = np.array(ID,dtype=np.float64,order="C")

for i in range(0,len(zQSO)):
   # print('LC_',ID[i],'num',i)
    if zQSO[i] == -9.9:
        d=str(int(ID[i]))
        NO.append(d)
    else:
        d=str(int(ID[i]))
        QSO.append(d)
print('quasar:', len(QSO))
print('no quasar:', len(NO))
