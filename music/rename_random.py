import string
import os
import random

letters = string.ascii_letters + string.digits
path = "/mnt/2A548B6774E73BFC/MyMusic/mp3/"
ext = ".mp3"
file_list = sorted(os.listdir(path))
count = 0

for file in file_list:
    new_name = "".join(random.sample(letters, k=15))
    os.rename(path + file, path + new_name + ext)
    count += 1

print(len(file_list), count, len(file_list) == count)