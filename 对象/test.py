class Stu:
    def __init__(self):
        print("创建Stu对象")

    def __del__(self):
        print("销毁Stu对象")

    def fun(self):
        print("This is Funciotn fun")


tom = Stu()
tom.fun()
