# 测试全局变量和局部变量
num = 100


def fun():
    global num
    num += 100
    print("num:", num)


fun()
print(num)
