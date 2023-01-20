import os

path = "/mnt/2A548B6774E73BFC/MyMusic/aac/"
file_list = sorted(os.listdir(path))
count = 0

for file in file_list:
    stats = os.stat(path + file)
    size = stats.st_size
    if size<1048576:
        count += 1
        print(file, size)
        os.remove(path + file)
print(count)