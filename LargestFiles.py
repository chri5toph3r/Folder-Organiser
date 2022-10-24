import os
import FolderOrganiser


def print_out(input_list, cur_path, info, blank_line=False, tabs=0):
    if len(input_list):
        if blank_line:
            print()

        for t in range(tabs):
            print("\t", end="")

        print(f"{cur_path} {info}:")
        for item in input_list:
            for t in range(tabs):
                print("\t", end="")
            print(item)
        return True
    return False


def set_path(cur_path, files_sizes, min_mb, tabs=0):
    cur_path, f_list, d_list = FolderOrganiser.get_f_d_list(cur_path, True, tabs=tabs)
    are_files = print_out(f_list, cur_path, "files", tabs=tabs)
    are_dirs = print_out(d_list, cur_path, "folders", are_files, tabs)

    if are_files:
        for f in f_list:
            file_stats = os.stat(f"{cur_path}/{f}")
            file_size_mb = file_stats.st_size / (1024 * 1024)
            if file_size_mb > min_mb:
                files_sizes.append((file_size_mb, f"{cur_path}/{f}"))

    if are_dirs:
        for d in d_list:
            set_path(f"{cur_path}/{d}", files_sizes, min_mb, tabs=tabs+1)

    return files_sizes


if __name__ == '__main__':
    files_path = os.path.dirname(__file__).replace('\\', '/')
    print(f"File's path: {files_path}")
    path = input("path: ")
    min_f_size = input("smallest file size to intake (in MB): ")

    f_sizes = []
    f_sizes = set_path(path, f_sizes, float(min_f_size))
    f_sizes.sort(reverse=True)
    print(f_sizes)
