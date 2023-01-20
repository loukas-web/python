from pymediainfo import MediaInfo as mi
import os

path = "/mnt/2A548B6774E73BFC/MyMusic/mp3/2/"
file_list = sorted(os.listdir(path))
sampling_rate = []
channels = []
count_try = 0
count_ie = 0
count_te = 0
count_re = 0
for file in file_list:
    try:
        file_parse = mi.parse(path + file)
        if file_parse.audio_tracks[0].channel_s < 2 or file_parse.audio_tracks[0].sampling_rate < 44100:
            print(file, "TryError")
            count_try += 1
            #os.remove(path + file)
    except IndexError as e:
        #print(file, "IndexError")
        print(e)
        count_ie += 1
        #os.rename(path + file, path + "00ie" + str(count_ie) + ".mp3")
        #os.remove(path + file)
    except TypeError as e:
        #print(file, "TypeError")
        print(e)
        count_te += 1
        #os.rename(path + file, path + "00te" + str(count_te) + ".mp3")
        #os.remove(path + file)
    except RuntimeError:
        print(file)
        count_re += 1

print(count_try, count_ie, count_te, count_re)