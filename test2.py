import os
from pymediainfo import MediaInfo as mi

path = "/home/loukas/Videos/Westworld.S04.720p.BluRay.x264-BROADCAST/"
filelist = os.listdir(path)
duration = []

for file in filelist:
    file_parse = mi.parse(path + file)
    duration.append(float(file_parse.audio_tracks[0].duration))

print(len(filelist), sum(duration) / 1000 / 3600)
