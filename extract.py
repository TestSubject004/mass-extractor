import os
#from unrar import rarfile
from zipfile import ZipFile

obj = os.scandir()

for entry in obj:
    if entry.is_file() and entry.name.split('.')[1]=='zip':
        print(entry.name)
        os.mkdir(entry.name.split('.')[0])
        zip =ZipFile(entry.name)
        zip.extractall(entry.name.split('.')[0])
        zip.close()