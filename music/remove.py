from pymediainfo import MediaInfo as mi
import os

path = "/mnt/2A548B6774E73BFC/MyMusic/mp3/"
file_list = os.listdir(path)
count1 = 0
count2 = 0

for file in file_list:
    file_parse = mi.parse(path + file)
    if file_parse.audio_tracks[0].channel_s < 2 or file_parse.audio_tracks[0].sampling_rate < 44100:
        print(file, "TryError")
        os.remove(path + file)
        count1 += 1
    if float(file_parse.audio_tracks[0].duration) < 60000:
        count2 += 1

print(count1, count2)