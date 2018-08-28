from os import listdir, sep
from os.path import abspath, basename, isdir

def tree(dir, padding):
    print padding[:-1] + '+-' + basename(abspath(dir)) + '/'
    padding = padding + ' '
    files = []

    files = [x for x in listdir(dir) if isdir(dir + sep + x)]
    count = 0
    for file in files:
        count += 1
        print padding + '|'
        path = dir + sep + file
        if isdir(path):
            if count == len(files):
                tree(path, padding + ' ')
            else:
                tree(path, padding + '|')
        else:
            print padding + '+-' + file