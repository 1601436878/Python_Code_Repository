n = eval(input("请输入数字的数量："))
num = eval(input("请输入数字："))
max = num

for i in range(n - 1):
    num = eval(input("请输入数字："))
    if num > max:
        max = num
    print("目前的最大值是：", max)

print("最大值是：", max)
