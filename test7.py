import glob

path = "/run/media/loukas/DOCKER3/MyMusic/"

summr = []

summr.append(len(glob.glob(path + "**/*.mp3", recursive=True)))
summr.append(len(glob.glob(path + "**/*.MP3", recursive=True)))
summr.append(len(glob.glob(path + "**/*.wma", recursive=True)))
summr.append(len(glob.glob(path + "**/*.ape", recursive=True)))
summr.append(len(glob.glob(path + "**/*.flac", recursive=True)))
summr.append(len(glob.glob(path + "**/*.wav", recursive=True)))
summr.append(len(glob.glob(path + "**/*.ogg", recursive=True)))

file_list = glob.glob(path + "**/*.*", recursive=True)

print(summr, sum(summr))
print(len(file_list))

exte = []

for file in file_list:
    dot = file.rfind(".")
    ext = file[dot + 1:]
    exte.append(ext)

ext2 = {_ for _ in exte}

ext2 = list(ext2)

ext2 = sorted(ext2, key=len)
print(ext2)