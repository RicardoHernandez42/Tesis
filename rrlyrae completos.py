import os
from collections import Counter
import numpy as np
import statistics
from os import listdir
from os.path import isfile, join


mypath = '/Volumes/ADATA/RRLyraetxtNuevos/'
carpeta = '/Volumes/ADATA/RRLyraetxtNuevos/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for c in onlyfiles:
    file = os.path.splitext(c)[0]
    with open('/Volumes/ADATA/RRLyraetxtNuevostxtcompletos/LC_'+file+'_completo.txt', 'w') as out:
        for i in range(1,31):
            out.write('0,0,0,0,0' + '\n')
        print(c)
        Ra,Dec,ufecha,u1,uerr,gfecha,g1,gerr,rfecha,r1,rerr,ifecha,i1,ierr,zfecha,z1,zerr = np.loadtxt(mypath + '/' + c, delimiter=' ',unpack=True)
        r = []
        i = []
        u = []
        z = []
        g = []
        fecha = []
        for a in ufecha:
            fecha.append(int(a))
        for a in u1:
            if a == -99.99:
                u.append(float(0))
            else:
                u.append(a)
        for a in g1:
            if a == -99.99:
                g.append(float(0))
            else:
                g.append(a)
        for a in r1:
            if a == -99.99:
                r.append(float(0))
            else:
                r.append(a)
        for a in i1:
             if a == -99.99:
                i.append(float(0))
             else:
                i.append(a)
        for a in z1:
            if a == -99.99:
                z.append(float(0))
            else:
                z.append(a)
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
            if x in fecha:
                if x in fechan:
                    ind = np.argwhere(fechan == x)
                    n = ind[0][0]
                    out.write(str(prom[n][1])+','+str(prom[n][2])+','+str(prom[n][3])+','+str(prom[n][4])+','+str(prom[n][5]) + '\n')
                else:
                    ind = np.argwhere(fecha == x)
                    n = ind[0][0]
                    out.write(str(r[n])+','+str(i[n])+','+str(u[n])+','+str(z[n])+','+str(g[n]) + '\n')
            else:
                out.write('0,0,0,0,0' + '\n')
        for i in range(1,31):
            out.write('0,0,0,0,0' + '\n')
