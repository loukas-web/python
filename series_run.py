from pymediainfo import MediaInfo as mi
from glob import glob
from os import stat

path = '/run/media/loukas/5193EF280F2AB294/Netflix Marvel Series/'

file_list = glob(path + '**/*.mkv', recursive=True)
duration = []
size = []


for file in file_list:
    size.append(stat(file).st_size)
    parse = mi.parse(file)
    duration.append(float(parse.video_tracks[0].duration))

print(len(file_list))
print(sum(size))
print(sum(duration))
