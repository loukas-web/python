from shutil import copyfile
from my_import import make_directory, random_string, get_files, get_extensions
from my_import import make_directory_by_extension

import_path: str = "/home/loukas/Music/"
destination_path: str = "/home/loukas/Music/export/"

make_directory(destination_path)

filelist = get_files(import_path)

unique_extensions = get_extensions(filelist)

make_directory_by_extension(destination_path, unique_extensions)

for file in filelist:
    new_name = random_string()
    destination_folder = file[file.rfind(".")+1:].lower() + "/"
    copyfile(file, f"{destination_path}{destination_folder}{new_name}.{destination_folder[:-1]}")