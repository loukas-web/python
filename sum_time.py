from glob import glob
from os.path import isfile
from pymediainfo import MediaInfo as mi

path = '/mnt/5393E2653C8C7627/ASMR/'

file_list = [_ for _ in glob(path + '**/*', recursive=True) if isfile(_)]

parse = []
for file in file_list:
    parse.append(mi.parse(file))

sum_time = 0
counter = 0

lst = []

for file in parse:
    for video in file.video_tracks:
        try:
            sum_time += video.duration
            lst.append(str(video.width) + 'x' + str(video.height))
        except TypeError as e:
            counter += 1
            print(counter, e)

print(sorted(list({_ for _ in lst})))
