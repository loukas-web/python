from glob import glob
from os import stat, rename
from os.path import isfile
from folder_create import create_folder

path = '/mnt/2A548B6774E73BFC/MyMusic/export/'
max_size = 4_700_000_000
size = 0
count = 0
filelist = [_ for _ in glob(path + '*') if isfile(_)]

export_path = create_folder(path=path)
export_list = []

def sort_key(file):
    return stat(file).st_size

filelist.sort(key=sort_key)

for file in range(1, len(filelist)):
    file_size = stat(filelist[file-1]).st_size
    file_size_new = stat(filelist[file]).st_size

    if size + file_size <= max_size:
        export_list.append(filelist[file-1])
        size += file_size
        count += 1    
    elif size - file_size + file_size_new <= max_size:
        export_list.pop()
        export_list.append(filelist[file])
        size -= file_size
        size += file_size_new
    
    if file ==len(filelist) - 1 and size + file_size_new <= max_size:
        export_list.append(filelist[file])


    if size == max_size:
        break

print(size, count, export_path)

for file in export_list:
    rename(file, file.replace(path, export_path))