# This script renames the files in a specific folder in random names.
# Information
#
# 1. For the name generation, it uses capital letters, lower letters and numbers. If you want something else, change the "letters" variable.
# 1. The "letters" variable must be a string with whatever characters, numbers or punctuation you want the name to have.
# 1. For the "letter" variable use the ascii caracters, digits and punctuation from the "string" import.
#
# 2. For the randomization use the random.sample(). It takes 2 variables. The first one is the string "letters" and the second one is the number of characters you want to take from the string.

# 3. Warning: The folder must contain only one type of files (like mp3). Whatever type of files are you using, set the right file extension in the "ext" variable

import string
import os
import random

letters = string.ascii_letters + string.digits
path = "/mnt/2A548B6774E73BFC/MyMusic/export/"
ext = ".mka"
file_list = os.listdir(path)

for file in file_list:
    new_name = "".join(random.sample(letters, k=15))
    os.rename(path + file, path + new_name + ext)
