import os

path = "/mnt/2A548B6774E73BFC/MyMusic/test/"
export = "export/"
export_with_warnings = "export_with_warnings/"
file_list = os.listdir(path)

try:
    os.mkdir(path + export)
except FileExistsError as e:
    print(e)

try:
    os.mkdir(path + export_with_warnings)
except FileExistsError as e:
    print(e)

for file in file_list:
    file_original = path + file
    file_new = file_original.replace(".mp3", ".mka")
    command = f"mkvmerge --ui-language en_US --output {file_new} --language 0:en {file_original}"
    return_code = os.system(command)

    match return_code:
        case 0:
            os.rename(file_new, path + export + file.replace(".mp3", ".mka"))
            os.remove(file_original)
        case 256:
            os.rename(file_new, path + export_with_warnings + file.replace(".mp3", ".mka"))
        case 512:
            print(file)
