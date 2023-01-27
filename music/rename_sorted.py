from os import rename
from glob import glob
from my_import import random_string, get_single_extension, get_file_size

path = "/mnt/2A548B6774E73BFC/MyMusic/wmv/"
count = 0
file_list = glob(path + '*')

for file in file_list:
    ext = '.' + get_single_extension(file)
    new_name = random_string()
    rename(file, path + new_name + ext)

file_list = sorted(glob(path + '*'), key=get_file_size)
length = len(str(len(file_list)))

for file in file_list:
    count += 1
    new_name = str(count).rjust(length, '0')
    ext = '.' + get_single_extension(file)
    rename(file, path + new_name + ext)
