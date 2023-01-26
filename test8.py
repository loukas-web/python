import os

path: str = "/mnt/2A548B6774E73BFC/MyMusic/mp3/02/"
filelist = sorted(os.listdir(path))

filesize = []

for file in filelist:
    file_stat = os.stat(path + file)
    filesize.append(file_stat.st_size)

print(sum(filesize) / 1024 / 1024)
