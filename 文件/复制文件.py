# 拷贝文件

# import os


def main():
    namein = "test1"
    nameout = "test2"

    filein = open(namein, "r")
    fileout = open(nameout, "w")

    linecount = charcount = 0
    for i in filein:
        linecount += 1
        charcount += len(i)
        fileout.write(i)
    print("共有", linecount, "行被写入,共有", charcount, "个字符被写入")


main()
