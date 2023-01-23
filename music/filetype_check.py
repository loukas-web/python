import os

path = "/mnt/2A548B6774E73BFC/MyMusic/ogg/"
ext = []
filelist = os.listdir(path)

for file in filelist:
    ext.append(file[file.rfind("."):])

print({_ for _ in ext})