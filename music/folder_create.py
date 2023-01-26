from os import mkdir


# path = "/mnt/2A548B6774E73BFC/"

def create_folder(count=0, path="/mnt/2A548B6774E73BFC/"):
    try:
        count += 1
        folder = str(count).rjust(5, "0") + "/"
        mkdir(path + folder)
        return path + folder
    except FileExistsError:
        return create_folder(count, path)
