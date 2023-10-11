import numpy as np
from collections import Counter
import os
from os import listdir
from os.path import isfile, join
from PIL import Image


mypath = '/Volumes/ADATA/Entrenamiento_RRLyraetxt/'
carpeta = '/Volumes/ADATA/Entrenamiento_RRLyraetxt/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
count=1
for c in onlyfiles:
    file = os.path.splitext(c)[0]
    with open('/Volumes/ADATA/AllLC_promedio/'+file+'_completo_promedio.txt', 'w') as out:
        print(count,c)
        count=count+1
        f = open(mypath + '/' + c)
        text = f.readlines()
        f.close
        data = []
        r = []
        i = []
        u = []
        z = []
        g = []
        for line in text:
            r.append(line.split(',')[0])
            i.append(line.split(',')[1])
            u.append(line.split(',')[2])
            z.append(line.split(',')[3])
            g.append(line.split(',')[4])
        r = np.array(r,dtype=np.float64,order="C")
        i = np.array(i,dtype=np.float64,order="C")
        u = np.array(u,dtype=np.float64,order="C")
        z = np.array(z,dtype=np.float64,order="C")
        g = np.array(g,dtype=np.float64,order="C")

        for n in range(0,len(r)):
            a = [r[n],i[n],u[n],z[n],g[n]]
            data.append(a)
        data = np.array(data,dtype=np.float64,order="C")

        img = Image.fromarray(data)
        img.save('/Volumes/ADATA/EntrenamientoIm/RRLyrae/'+file+'.tiff')
