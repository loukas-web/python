from os import mkdir
from glob import glob
from random import sample
from os.path import isfile
from string import ascii_letters, digits

def make_directory(path: str):
    try:
        mkdir(path)
    except FileExistsError:
        print("The Folder Already Exists")

def random_string(letters: str=ascii_letters+digits, number: int=15) -> str:
    return "".join(sample(letters, k=number))

def get_files(path: str) -> list[str]:
    return [_ for _ in glob(path + "**/*", recursive=True) if isfile(_)]

def get_extensions(filelist: list[str]) -> set:
    extensions = []
    for file in filelist:
        ext = file[file.rfind("."):].lower()
        extensions.append(ext)

    return {_ for _ in extensions}

def make_directory_by_extension(path: str, unique_extensions: set):
    for extension in unique_extensions:
        make_directory(path + extension[1:] + "/")