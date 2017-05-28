# 递归 -- 阶乘


def dat(num):
    if num == 0:
        return 1
    return num * dat(num - 1)


print(dat(4))
