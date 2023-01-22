from pymediainfo import MediaInfo as mi
import os

path = "/mnt/2A548B6774E73BFC/MyMusic/mka/export/"
file_list = os.listdir(path)
count = 0

for file in file_list:
    stats = os.stat(path + file)
    file_parse = mi.parse(path + file)
    try:
        if file_parse.audio_tracks[0].channel_s < 2 or file_parse.audio_tracks[0].sampling_rate < 44100:
            count += 1
            print(count, file, "TryError")
            os.remove(path + file)
            continue
        elif float(file_parse.audio_tracks[0].duration) < 60000:
            count += 1
            print(count, file)
            os.remove(path + file)
            continue
        elif stats.st_size < 1048576:
            count += 1
            print(count, file, stats.st_size)
            os.remove(path + file)
            continue
    except TypeError:
        print(count, file, "TypeError")
        os.remove(path + file)