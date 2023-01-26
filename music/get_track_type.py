from pymediainfo import MediaInfo as mi
from os import listdir

path = "/mnt/2A548B6774E73BFC/MyMusic/wmv/"

filelist = listdir(path)

file_parse = []
for file in filelist:
    parse = mi.parse(path + file)
    file_parse.append(parse)

audio_tracks = []
for file in file_parse:
    for track in file.audio_tracks:
        audio_tracks.append(track.track_type + " " + track.format + " " + " ".join(track.other_format))


for track in {_ for _ in audio_tracks}:
    print(track)
