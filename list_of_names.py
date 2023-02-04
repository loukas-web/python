from glob import glob

path = '/run/media/loukas/DOCKER4/Series Full/'

filelist = glob(path + '**/*.mkv', recursive=True)

filelist = [_.split('/')[-1].replace('.mkv', '').split('-')[-1][1:] for _ in filelist]

for i, file in enumerate(filelist):
    print('-'.join([str(i), file]))
