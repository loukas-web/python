from os import mkdir
from glob import glob
from random import sample
from os.path import isfile
from string import ascii_letters, digits

# Tries to make a directory.
def make_directory(path: str):
    try:
        mkdir(path)
    except FileExistsError:
        print("The Folder Already Exists")

# Returns a string with random letters and digits.
def random_string(letters: str=ascii_letters+digits, number: int=15) -> str:
    return "".join(sample(letters, k=number))

# Get files from a directory recursively. Ignores folders.
def get_files(path: str) -> list[str]:
    return [_ for _ in glob(path + "**/*", recursive=True) if isfile(_)]

# Gets an extension from a single file. Ignores the dot in the extension.
def get_single_extension(file: str) -> str:
    return file[file.rfind(".")+1:].lower()

# Gets the extensions in a file list. Ignores the dot in the extension.
def get_extensions(filelist: list[str]) -> set:
        return {get_single_extension(file) for file in filelist}

def make_directory_by_extension(path: str, unique_extensions: set):
    for extension in unique_extensions:
        make_directory(path + extension + "/")