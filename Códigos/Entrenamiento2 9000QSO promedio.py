import os
import numpy as np
import statistics
from os import listdir
from os.path import isfile, join

mypath = '/Volumes/ADATA/Entrenamiento2_9000QSO_completo/'
carpeta = '/Volumes/ADATA/Entrenamiento2_9000QSO_completo/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
count = 1
for c in onlyfiles:
    file = os.path.splitext(c)[0]
    with open('/Volumes/ADATA/Entrenamiento2_9000QSO_promedio/'+file+'_promedio.txt', 'w') as out:
        h = open(mypath + '/' + c)
        text2 = h.readlines()
        h.close()
        print(count,c)
        count=count+1
        date = []
        r = []
        i = []
        u = []
        z = []
        g = []
        for line in text2:
            #date.append(line.split(',')[0])
            r.append(line.split(',')[0])
            i.append(line.split(',')[1])
            u.append(line.split(',')[2])
            z.append(line.split(',')[3])
            g.append(line.split(',')[4])
        #date = np.array(date,dtype=np.float64,order="C")
        r = np.array(r,dtype=np.float64,order="C")
        i = np.array(i,dtype=np.float64,order="C")
        u = np.array(u,dtype=np.float64,order="C")
        z = np.array(z,dtype=np.float64,order="C")
        g = np.array(g,dtype=np.float64,order="C")
        
        for x in range(0,len(r)-1,2):
            if r[x] == 0:
                a = 1
            elif r[x+1] == 0:
                a = 1
            else:
                a = 2
            if i[x] == 0:
                b = 1
            elif i[x+1] == 0:
                b = 1
            else:
                b = 2
            if u[x] == 0:
                c = 1
            elif u[x+1] == 0:
                c = 1
            else:
                c = 2
            if z[x] == 0:
                d = 1
            elif z[x+1] == 0:
                d = 1
            else:
                d = 2
            if g[x] == 0:
                e = 1
            elif g[x+1] == 0:
                e = 1
            else:
                e = 2
            d =  [(r[x]+r[x+1])/a,(i[x]+i[x+1])/b,(u[x]+u[x+1])/c,(z[x]+z[x+1])/d,(g[x]+g[x+1])/e]
            out.write(str(d[0]) + ','+ str(d[1]) + ','+ str(d[2]) + ','+ str(d[3]) + ','+ str(d[4]) + '\n')
