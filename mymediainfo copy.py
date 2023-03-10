from glob import glob
from pymediainfo import MediaInfo


def frequency(freq):
    for item in freq:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq


def match_frame_rate(frame_rate):
    match frame_rate:
        case '24.000':
            return '24p'
        case '25.000':
            return '25p'
        case '30.000':
            return '30p'
        case '48.000':
            return '48p'
        case '50.000':
            return '50p'
        case '60.000':
            return '60p'
        case '23.976':
            return '24000/1001p'
        case '29.97':
            return '30000/1001p'
        case '29.970':
            return '30000/1001p'
        case '47.952':
            return '48000/1001p'
        case '59.94':
            return '60000/1001p'
        case '59.940':
            return '60000/1001p'
        case other:
            return frame_rate


def file_without_extension(path_to_video):
    return path_to_video[:path_to_video.rfind('.')]


def ext(path_to_video):
    return path_to_video[path_to_video.rfind('.'):]


def folderpath(path_to_video):
    return path_to_video[:path_to_video.rfind('/') + 1]


def tomkvsrt(path_to_video):
    media_info = MediaInfo.parse(path_to_video)
    return f'mkvmerge --ui-language en_US --output "{file_without_extension(path_to_video)}.mkv" --language 0:en ' \
           f'--display-dimensions 0:{media_info.video_tracks[0].width}x{media_info.video_tracks[0].height} ' \
           f'--default-duration 0:{match_frame_rate(media_info.video_tracks[0].frame_rate)} ' \
           f'--fix-bitstream-timing-information 0:1 --language 1:en "(" "{file_without_extension(path_to_video)}' \
           f'{ext(path_to_video)}" ")" --track-order 0:1,0:0\n'


def savetofile(path_to_video):
    file = open(folderpath(path_to_video) + 'run', 'a')
    file.write(tomkvsrt(path_to_video))
    file.close()


pathofvideos = input('Give the path of the videos: ')

if pathofvideos[-1] != '/':
    pathofvideos += '/'

files = glob(f'{pathofvideos}*.mp4') + glob(f'{pathofvideos}*.webm')
for pathtovideo in files:
    savetofile(pathtovideo)

with open(pathofvideos + 'run', 'r') as f:
    filedata = f.read()

filedata = filedata.replace(pathofvideos, '')

with open(pathofvideos + 'run', 'w') as f:
    f.write(filedata)
