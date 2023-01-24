from glob import glob
from os import stat
import random

path = '/mnt/2A548B6774E73BFC/MyMusic/export/'
max_size = 734_003_200
size = 0
count = 0
filelist = glob(path + '*')

def sort_key(file):
    return stat(file).st_size

filelist.sort(key=sort_key)

for file in range(len(filelist) - 1):
    file_size = stat(filelist[file]).st_size
    file_size_new = stat(filelist[file + 1]).st_size

    if size + file_size <= max_size:
        size += file_size
        count += 1
    
    if size - file_size + file_size_new <= max_size:
        size -= file_size
        size += file_size_new

print(size, count)