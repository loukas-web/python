from pymediainfo import MediaInfo as mi
import os

path = "/mnt/2A548B6774E73BFC/MyMusic/temp/"
file_list = [_ for _ in os.listdir(path) if ".mka" in _]
sampling_rate = []
channels = []
duration = []

for file in file_list:
    try:
        parse = mi.parse(path + file)
        if len(parse.audio_tracks) == 0:
            print(file)
        sampling_rate.append(parse.audio_tracks[0].sampling_rate)
        channels.append(parse.audio_tracks[0].channel_s)
        duration.append(float(parse.audio_tracks[0].duration))
    except IndexError as e:
        print(file, e)
    except TypeError as e:
        print(file)

print({_ for _ in sampling_rate})
print({_ for _ in channels})
print(len(file_list), len(sampling_rate), len(channels), len(duration), sum(duration))
