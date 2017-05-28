#  写入文件操作 writelines()

import os


def writefile():
    path = "test1"
    fileout = open(path, "w")
    fileout.writelines(["hello", " ", "world"])
    fileout.close()


def readfile():
    path = "test1"
    filein = open(path, "r")
    data = filein.read()
    print(data)


writefile()  # hello world
readfile()  # hello world
