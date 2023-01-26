import os
from pymediainfo import MediaInfo as mi

file_parse = []
file_path: str = "/mnt/2A548B6774E73BFC/MyMusic/mp3/"
file_list: list[str] = sorted(os.listdir(file_path))

for file in file_list:
    file_parse.append(mi.parse(file_path + file))

file_duration = []
for file in file_parse:
    file_duration.append(file.audio_tracks[0].duration)

dur = {_ for _ in file_duration}

print(len(file_duration), len(dur))
