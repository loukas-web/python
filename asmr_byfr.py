from glob import glob
from os.path import isfile
from os import mkdir
from shutil import copyfile
from pymediainfo import MediaInfo as mi

path = '/mnt/5393E2653C8C7627/ASMR/'
export = '/run/media/loukas/DOCKER4/export/'
file_list = [_ for _ in glob(path + '**/*.mp4', recursive=True) if isfile(_)]

try:
    mkdir(export)
except FileExistsError as e:
    print(e)

for file in file_list:
    parse = mi.parse(file)
    fr: str = parse.video_tracks[0].frame_rate
    print(file)
    export_dr = export + fr.replace('.', '') + '/'
    try:
        mkdir(export_dr)
    except FileExistsError as e:
        print(e)
    copyfile(file, export_dr + file[file.rfind('/')+1:])
