from shutil import copyfile
from my_import import make_directory, random_string, get_files, get_extensions
from my_import import make_directory_by_extension, get_single_extension

import_path: str = "/run/media/loukas/DOCKER3/MyMusic/"
destination_path: str = "/mnt/2A548B6774E73BFC/MyMusic/"

make_directory(destination_path)

filelist = get_files(import_path)

make_directory_by_extension(destination_path, get_extensions(filelist))

for file in filelist:
    new_name = random_string()
    ext = get_single_extension(file)
    destination_file = destination_path + ext + "/" + new_name + "." + ext
    copyfile(file, destination_file)
