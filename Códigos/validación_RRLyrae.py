import shutil
import os
from random import seed
from random import choice

source_dir = '/Volumes/ADATA/EntrenamientoIm/RRLyrae'
target_dir = '/Volumes/ADATA/ValidaciónIm/RRLyrae'

file_names = os.listdir(source_dir)


sequence = [i for i in range(0,len(file_names))]

seed(1)

for x in range(0,int(.25*len(file_names))):
    selection = choice(sequence)
    sequence.remove(selection)
    print(x,file_names[selection])
    shutil.move(os.path.join(source_dir, file_names[selection]), target_dir)
