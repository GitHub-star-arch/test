import os
import shutil
import time

def remove_folder(path):
    if not os.remove(path):
        print('remove successfully')
    else:
        print('unable to delete')

def main():
    path = './project'
    days = 1
    seconds = time.time()-(days*24*60*60)
    if (os.path.exists(path)):
        for root, folder, files in os.walk(path):
            age = os.stat(root).st_ctime
            if (seconds>=age):
                remove_folder(root)
                break
            #else:
            #   loop files
            #   age1 = os.stat(files).st_ctime
            #   if (seconds>=age1):
            #       remove_folder(files)
            #       break
main()