from glob import glob
from pymediainfo import MediaInfo as mi

filelist = []
media_parse = []
audio_parse = []


path1 = "/run/media/loukas/DOCKER4/"
path2 = "/run/media/loukas/DOCKER3/"
path3 = "/mnt/usb-WD_My_Passport_25E2_575834314442384B44593955-0:0-part1/"
path4 = "/mnt/2A548B6774E73BFC/"
path5 = "/mnt/5393E2653C8C7627/"

paths = [path1, path2, path3, path4, path5]
for path in paths:
    filelist.extend(glob(path + "**/*.*", recursive=True))


for media in filelist:
    try:
        media_parse.append(mi.parse(media))
    except RuntimeError as e:
        print(e)


for media in media_parse:
    for audio in media.audio_tracks:
        audio_parse.append(audio.format + " / " + " ".join(audio.other_format))

print({_ for _ in audio_parse})
print(len(audio_parse))