##from PIL import Image
##from numpy import asarray
## load the image
##image = Image.open('/Users/richo/OneDrive - Fundacion Universidad de las Americas Puebla/Honores/CNN/prueba.png')
## convert image to numpy array
##data = asarray(image)
##print(type(data))
## summarize shape
##print(data.shape)
##
## create Pillow image
##image2 = Image.fromarray(data)
##print(type(image2))
##
## summarize image details
##print(image2.mode)
##print(image2.size)
##for i in range(0,len(data)):
##    print(data[i])

from PIL import Image
import numpy as np
from numpy import asarray
import matplotlib.pyplot as plt

pic = Image.open('/Volumes/ADATA/EntrenamientoIm/Quasares/LC_98_completo_promedio.tiff')
data = asarray(pic)
print(data[380:390])
