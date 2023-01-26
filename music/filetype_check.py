from glob import glob
import os

path = "/mnt/2A548B6774E73BFC/MyMusic/Music/"
ext = []
filelist = [_ for _ in glob(path + "**/*", recursive=True) if os.path.isfile(_)]

for file in filelist:
    ext.append(file[file.rfind("."):])

print({_ for _ in ext})
