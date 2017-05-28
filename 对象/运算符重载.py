# 运算幅度重载

class Person:
    num = 0

    def __init__(self, num):
        self.num = num
        print("创建一个Person类")

    def __add__(self, other):
        return self.num + other.num


tom = Person(10)
tim = Person(20)
print(tom + tim + Jimmy)  # 重载了加运算符
