# 用read()一次读取文件内容

import os

pathname = "读取文件.py"
filein = open(pathname, "r")
print(filein.read())
