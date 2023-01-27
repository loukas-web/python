import os
from my_import import random_string, get_single_extension

path = "/home/loukas/Downloads/elena/"
file_list = os.listdir(path)

for file in file_list:
    ext = '.' + get_single_extension(path + file)
    new_name = random_string()
    os.rename(path + file, path + new_name + ext)
