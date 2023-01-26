import os
from math import ceil

path = "/mnt/2A548B6774E73BFC/MyMusic/mka/"
file_list = os.listdir(path)
file_count = len(file_list)

files_per_folder = 5_000

folder_number = ceil(file_count / files_per_folder)
folder_digits = len(str(folder_number))

folders = [str(folder).rjust(folder_digits, "0") for folder in range(1, folder_number + 1)]

for folder in folders:
    try:
        os.mkdir(path + folder)
    except FileExistsError:
        print("Folder exists")

for file in range(len(file_list)):
    filename = path + file_list[file]
    new_folderpath = path + str(file % folder_number + 1).rjust(folder_digits, "0") + "/" + file_list[file]
    os.rename(filename, new_folderpath)
