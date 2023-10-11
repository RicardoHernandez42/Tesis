import shutil
import os
from random import seed
from random import choice

source_dir = '/Volumes/ADATA/EntrenamientoIm/Quasares'
target_dir = '/Volumes/ADATA/ValidaciónIm/Quasares'

file_names = os.listdir(source_dir)


sequence = [i for i in range(0,len(file_names))]

seed(1)

for x in range(0,int(.25*len(file_names))):
    selection = choice(sequence)
    sequence.remove(selection)
    print(x,file_names[selection])
    shutil.move(os.path.join(source_dir, file_names[selection]), target_dir)
#    for y in file_names:
#        if y == file_names[selection]:
#           print(x,file_names[selection]) 
#    shutil.move(os.path.join(source_dir, file_names[selection]), target_dir)
#    print(file_names[selection])
