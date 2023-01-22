from glob import glob
import os
from pymediainfo import MediaInfo as mi

path = "/run/media/loukas/DOCKER3/MyMusic/"
filelist = [_ for _ in glob(path + "**/*", recursive=True) if os.path.isfile(_)]
file_parse = []
file_audio = []

for file in filelist:
    file_parse.append(mi.parse(file))

for file in file_parse:
    if len(file.audio_tracks) > 0:
        file_audio.append(file.audio_tracks)

print(len(filelist), len(file_parse), len(file_audio))