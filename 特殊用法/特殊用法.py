def fun():
    # 三目运算符
    a = a if 1 > 2 else 4  # 不存在这种用法：  a = a>2?3:4

    list = [1, 2, 3, 4, 5]
    list = [i + 1 for i in list]  # 列表解析
    print(list)


def add(a):
    return a + 1


def lambdatest():  # lambda相当于一个匿名函数，:前面是形参，后面是对形参的操作
    dic = {"001": "name", "002": "sex"}
    listdata = list(dic.items())
    data = lambda x: x[0]
    print(data(listdata))


def replacetest():
    str = "aaaaabbccc"
    str = str.replace("a", "#")  # 替换了所有的a
    print(str)


def cmps(x):
    y = 0
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0


def sorttest():
    listtest = [1, 2, 3, 7, 6, 5, 4, 3]
    listtest.sort(key=lambda x: x)
    print(listtest)


def dictest():
    dic = {(1, 2, 3): "123"}  # 字典的键不可以是列表
    print(dic)


# with ... as
'''
  执行with后面的语句
'''

dictest()
