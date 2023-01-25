import os

path = "/mnt/2A548B6774E73BFC/MyMusic/temp/"
export = "export/"
export_with_warnings = "export_with_warnings/"
errored = "errored/"
ext = ".wav"
file_list = os.listdir(path)

try:
    os.mkdir(path + export)
except FileExistsError as e:
    print(e)

try:
    os.mkdir(path + export_with_warnings)
except FileExistsError as e:
    print(e)

try:
    os.mkdir(path + errored)
except FileExistsError as e:
    print(e)

for file in file_list:
    file_new = file.replace(ext, ".mka")
    command = f"mkvmerge --ui-language en_US --output {path + file_new} --language 0:en {path + file}"
    return_code = os.system(command)

    match return_code:
        case 0:
            os.rename(path + file_new, path + export + file_new)
            os.rename(path + file, path + export + file)
        case 256:
            os.rename(path + file_new, path + export_with_warnings + file_new)
            os.rename(path + file, path + export_with_warnings + file)
        case 512:
            print(file, return_code)
            os.rename(path + file, path + errored + file)
