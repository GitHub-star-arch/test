import os
import shutil

p = './starting/file.txt'
root = os.path.splitext(p)

print(root)

p = './destination/'
print('bcf')
print(os.listdir(p))

source = './starting/file.txt'
destination = './destination/'
shutil.move(source, destination)
print('acf')
print(os.listdir(p))
source2 = './destination/file.txt'
destination = './starting/'
shutil.move(source2, destination)