from os import path, mkdir, listdir
from shutil import move


# get path and list of files
def get_f_d_list(dir_name=None, get_dirs=False, tabs=0):
    if not path.isdir(dir_name):
        dir_name = path.dirname(__file__).replace("\\", "/")
        print(f"Directory not given/found")

    for t in range(tabs):
        print("\t", end="")
    print(f"Current directory: {dir_name}/\n")

    try:
        elements_list = listdir(dir_name)
        files_list = [f for f in elements_list if path.isfile(f"{dir_name}/{f}") and "." in f]

        if get_dirs:
            dirs_list = [d for d in elements_list if path.isdir(f"{dir_name}/{d}")]
            return dir_name, files_list, dirs_list
        return dir_name, files_list
    except IOError:
        print(f"Permission denied {dir_name}")
        files_list = []
        dirs_list = []

    if get_dirs:
        return dir_name, files_list, dirs_list
    return dir_name, files_list


# get all extensions appearing in directory
def get_all_file_extensions(files_list):
    ext_list = [file.split(".")[-1] for file in files_list]
    ext_list = list(set(ext_list))
    ext_list.sort()
    print(f"Available extensions: {ext_list}")
    return ext_list


# get file extension(s) to organise
def check_asked_extensions(ext_list, extensions):
    asked_ext_list = [ext for ext in extensions.split() if ext in ext_list]
    asked_ext_list.sort()
    print(f"Files with extensions {asked_ext_list} will be moved\n")
    return asked_ext_list


# get destination directory and transfer files
def check_dir_transfer_f(dir_path, dest_dir, files_list, ext_to_move_list):
    dest_path = f"{dir_path}/{dest_dir}"
    if not path.exists(dest_path):
        print(f"Creating directory: {dest_path}")
        mkdir(dest_path)
        print("Directory created")
    elif not path.isdir(dest_path):
        print(f"Creating directory: {dest_path}")
        mkdir(dest_path)
        print("Directory created")
    else:
        print("Directory found")

    moved_files = 0
    for file in files_list:
        if file.split(".")[-1] in ext_to_move_list:
            move(f"{dir_path}/{file}", f"{dest_path}/{file}")
            moved_files += 1

    return moved_files


if __name__ == '__main__':
    files_path = path.dirname(__file__).replace('\\', '/')
    print(f"File's path: {files_path}")
    chosen_path = input("path: ")
    chosen_path, f_list = get_f_d_list(chosen_path)
    all_e_list = get_all_file_extensions(f_list)
    e_list = check_asked_extensions(all_e_list, input("extensions: "))

    d_dir = input(f"Destination: {chosen_path}/")
    print(f"{check_dir_transfer_f(chosen_path, d_dir, f_list, e_list)} files moved successfully")
    input("Press Enter to exit...")
