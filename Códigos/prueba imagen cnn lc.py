from PIL import Image
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


f = open('/Volumes/ADATA/Copia de LC_98_completo_promedio.txt')
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

for n in range(len(r)-50,len(r)-15):
    a = [r[n],i[n],u[n],z[n],g[n]]
    data.append(a)
data = np.array(data,dtype=np.float64,order="C")

img = Image.fromarray(data)
print(img.size)
img = img.convert('L')
plt.figure()
plt.imshow(img)
##for n in range(0,5):
##    a = [r[n],i[n],u[n],z[n],g[n]]
##    data.append(a)
##data = np.array(data,dtype=np.float64,order="C")
##
##img = Image.fromarray(data)
##print(img.size)
##img = img.convert('L')
##plt.figure()
##plt.plot([1,2,3,4])
##plt.imshow(img)
