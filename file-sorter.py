import os
from os.path import isfile, join
from time import sleep
import shutil


def get_files(path: str):
    files = []
    for file in os.listdir(path):
        if isfile(join(path, file)):
            files.append(file)
    return files


def watch_folder(path: str):
    last_files = get_files(path)
    while True:
        new_files = []
        files = get_files(path)
        for file in files:
            if file not in last_files:
                new_files.append(file)
        if len(new_files) != 0:
            return new_files
        else:
            sleep(5)


def sort(files: list, path: str):
    for file in files:
        extension = f'.{file.split(".")[-1]}'
        folders = os.listdir(path)
        if extension not in folders:
            os.mkdir(join(path, extension))
        shutil.move(join(path, file), join(join(path, extension), file))
        print(f'Moved {file} to {extension}/{file}')


def main():
    path = input('Enter the path of the folder you want to watch: ')
    if '"' in path:
        path = path.strip('"')
    while True:
        sort(watch_folder(path), path)


if __name__ == "__main__":
    main()
