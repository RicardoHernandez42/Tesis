import os
import numpy as np

g = open('/Users/richo/OneDrive - Fundacion Universidad de las Americas Puebla/Honores/stripe82candidateVar.dat')
text3 = g.readlines()
g.close()
text3 = text3[1:]
#ID = [line[5:12]]
zQSO = []
for line in text3:
    line = line[127:134]
    #zQSO.append(line[127:134].split('line[127:134]'))
    zQSO.append(line.split('line[127:134]'))
    print(zQSO)
zQSO = np.array(zQSO,dtype=np.float64,order="C")
    #print(zQSO)
    #break
#print(line)

#print(zQSO)
zQSO = []
ID = []
for line in text3:
    zQSO = float(line[126:134])
    ID = float(line[0:12])
ID = np.array(ID,dtype=np.float64,order="C")
zQSO = np.array(zQSO,dtype=np.float64,order="C")




  #  a = [line[127:134]]
   # if line[127:134] == '-9.9':
    #    line = line[127:134]
    #print(line[5:12],line[127:134])

#ID = np.array(ID,dtype=np.float64,order="C")
