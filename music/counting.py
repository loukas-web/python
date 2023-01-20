from pymediainfo import MediaInfo as mi
import os

path = "/mnt/2A548B6774E73BFC/MyMusic/mp3/"
file_list = sorted(os.listdir(path))

sampling_rate = []
channels = []

for file in file_list:
    try:
        parse = mi.parse(path + file)
        sampling_rate.append(parse.audio_tracks[0].sampling_rate)
        channels.append(parse.audio_tracks[0].channel_s)
    except IndexError as e:
        print(file, e)

print({_ for _ in sampling_rate})
print({_ for _ in channels})
print(len(file_list) == len(sampling_rate) == len(channels))