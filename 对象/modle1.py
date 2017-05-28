def fun():
    print("fun函数")


if __name__ == "__main__":
    fun()
else:
    print("我来自另一个模块")
    print("#", __name__)
