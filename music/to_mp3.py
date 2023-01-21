import os
import random

path = "/mnt/2A548B6774E73BFC/MyMusic/mka/1/"
file_list = os.listdir(path)
exit_codes = []

for file in file_list:
    exit_code = os.system(f"ffmpeg -i {path + file} -c:a aac -ac 2 -ar 44100 -q 0 -vn -sn -dn -map_metadata -1 -map_chapters -1 {path + file.replace('.mka', '.aac')}")
    exit_codes.append(exit_code)
    print({_ for _ in exit_codes})