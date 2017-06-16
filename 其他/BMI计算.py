# 计算BMI
'''
BMI = 体重（kg） 身高 2（m2）
'''


def nation(BMI):
    if BMI < 18.5:
        result = "偏瘦"
    elif BMI < 25:
        result = "正常"
    elif BMI < 30:
        result = "偏胖"
    else:
        result = "肥胖"
    return result


def local(BMI):
    if BMI < 18.5:
        result = "偏瘦"
    elif BMI < 24:
        result = "正常"
    elif BMI < 28:
        result = "偏胖"
    else:
        result = "肥胖"
    return result


def main():
    weight = input("请输入体重: ")
    height = input("请输入身高: ")
    weight = float(weight)
    height = float(height)
    BMI = eval("weight / (height**2)")
    #  BMI = weight / height**2
    print("BMI:", BMI)
    print("国内标准: ", local(BMI))
    print("国际标准: ", nation(BMI))


main()
