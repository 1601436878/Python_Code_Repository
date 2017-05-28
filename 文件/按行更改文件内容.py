#

import os


def main():
    filein = open("test1", "r")
    fileout = open("test1", "w")

    for i in filein:
        i = i + "#"
        print(i)
        fileout.write(i)

    filein.close()
    fileout.close()


main()
