import os
from collections import Counter
import numpy as np
import statistics
from os import listdir
from os.path import isfile, join


mypath = '/Users/richo/OneDrive - Fundacion Universidad de las Americas Puebla/Honores/AllLCs'
carpeta = '/Users/richo/OneDrive - Fundacion Universidad de las Americas Puebla/Honores/AllLCs'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for c in onlyfiles:
    file = os.path.splitext(c)[0]
    with open('/Volumes/ADATA/AllLC_completo/'+file+'_completo.txt', 'w') as out:
        for i in range(1,31):
            out.write('0,0,0,0,0' + '\n')
        f = open(mypath + '/' + c)
        text1 = f.readlines()
        f.close()
        print(c)   
        result=[]
        result2=[]
        for line in text1:
            if line[0] == '#':
                line = line[1:]
                result2.append(float(0))
            else:
                result2.append(line.split(' ')[2])
            result.append(line.split('.')[0])
        result = np.array(result,dtype=np.float64,order="C")  
        r = []
        i = []
        u = []
        z = []
        g = []
        fecha = []
        for a in range(0,len(result),5):
            r.append(result2[a])
            i.append(result2[a+1])
            u.append(result2[a+2])
            z.append(result2[a+3])
            g.append(result2[a+4])
            fecha.append(result[a])
        r = np.array(r,dtype=np.float64,order="C")
        i = np.array(i,dtype=np.float64,order="C")
        u = np.array(u,dtype=np.float64,order="C")
        z = np.array(z,dtype=np.float64,order="C")
        g = np.array(g,dtype=np.float64,order="C")
        fecha = np.array(fecha,dtype=np.float64,order="C")

        dfecha = Counter(fecha)
        fechar = list([item for item in dfecha if dfecha[item]>1])

        a = []
        b = []
        c = []
        d = []
        e = []
        f = []

        bi=[]
        ci=[]
        di=[]
        ei=[]
        fi=[]
        prom = []
        
        for v in fechar:
            for x in range(0,len(r)):
                if fecha[x] == v:
                    a.append(fecha[x])
                    b.append(r[x])
                    c.append(i[x])
                    d.append(u[x])
                    e.append(z[x])
                    f.append(g[x]) 
            for x in b:
                if x == 0:
                    bi.append(x)
            for x in c:
                if x == 0:
                    ci.append(x)
            for x in d:
                if x == 0:
                    di.append(x)
            for x in e:
                if x == 0:
                    ei.append(x)
            for x in f:
                if x == 0:
                    fi.append(x)
            bs = (len(b)-len(bi))
            cs = (len(c)-len(ci))
            ds = (len(d)-len(di))
            es = (len(e)-len(ei))
            fs = (len(f)-len(fi))
            if bs == 0:
                bs = 1
            else:
                bs = bs
            if cs == 0:
                cs = 1
            else:
                cs = cs
            if ds == 0:
                ds = 1
            else:
                ds = ds
            if es == 0:
                es = 1
            else:
                es = es
            if fs == 0:
                fs = 1
            else:
                fs = fs 
            br = sum(b)/bs
            cr = sum(c)/cs
            dr = sum(d)/ds
            er = sum(e)/es
            fr = sum(f)/fs
            a = []
            b = []
            c = []
            d = []
            e = []
            f = []
            bi=[]
            ci=[]
            di=[]
            ei=[]
            fi=[]
            prom.append([v,br,cr,dr,er,fr])
        fechan = []
        for v in range(0,len(prom)):  
            fechan.append(prom[v][0])
        fechan = np.array(fechan)
        
        for x in range(51075,54416):
            if x in result:
                if x in fechan:
                    ind = np.argwhere(fechan == x)
                    n = ind[0][0]
                    out.write(str(prom[n][1])+','+str(prom[n][2])+','+str(prom[n][3])+','+str(prom[n][4])+','+str(prom[n][5]) + '\n')
                else:
                    ind = np.argwhere(result == x)
                    n = ind[0][0]
                    out.write(str(result2[n])+','+str(result2[n+1])+','+str(result2[n+2])+','+str(result2[n+3])+','+str(result2[n+4]) + '\n')
            else:
                out.write('0,0,0,0,0' + '\n')
        for i in range(1,31):
            out.write('0,0,0,0,0' + '\n')
