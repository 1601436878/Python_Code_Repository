# 分行读取文件 readline()

import os


# readline()
def readfile():
    path = "分行读取.py"
    filein = open(path, "r")
    for i in range(10):
        data = filein.readline()[:-1]  # 默认会在每行后加上换行，用[:-1]去除换行符
        print(data)


# readlines()
def readfilelines():
    path = "分行读取.py"
    filein = open(path, "r")
    data = filein.readlines()
    for i in data:
        print(i[:-1])


readfilelines()
