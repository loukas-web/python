import os
path = "/mnt/2A548B6774E73BFC/MyMusic/mp3/"
file_list = os.listdir(path)

for file in file_list:
    if file.endswith(".mp3"):
        continue
    if file.endswith(".MP3"):
        continue
    if file.endswith(".Mp3"):
        continue
    print(file)