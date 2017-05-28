# 课后习题

# 直接读取
def read1():
    file = open("test.txt", "r")
    data = file.read()
    print(data)


def read2():
    file = open("test.txt", "rb")
    data = file.read()
    print(str(data.decode("GBK")))


read2()
