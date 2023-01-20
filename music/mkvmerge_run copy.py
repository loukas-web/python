import os

path = "/mnt/2A548B6774E73BFC/MyMusic/aac/"
export = "export/"
export_with_warnings = "export_with_warnings/"
errored = "errored/"
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
    file_original = path + file
    file_new = file_original.replace(".aac", ".mka")
    command = f"mkvmerge --ui-language en_US --output {file_new} --language 0:en {file_original}"
    return_code = os.system(command)

    match return_code:
        case 0:
            os.rename(file_new, path + export + file.replace(".aac", ".mka"))
            os.remove(file_original)
        case 256:
            os.rename(file_new, path + export_with_warnings + file.replace(".aac", ".mka"))
        case 512:
            #os.rename(file_original, path + errored + file)
            print("error")
