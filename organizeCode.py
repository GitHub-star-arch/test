import os
import shutil

path = input('Please, enter the name of the directory to be sorted: ')
list_files = os.listdir(path)
print(list_files)

for i in list_files:
    name, ext = os.path.splitext(i)
    print(name, ext)
    ext = ext[1:]
    if os.path.exists(path + '/' + ext):
        shutil.move(path + '/' + i, path + '/' + ext + '/' + i)
    else:
        os.mkdir(path + '/' + ext)
        shutil.move(path + '/' + i, path + '/' + ext + '/' + i)