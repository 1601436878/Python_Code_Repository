# 递归
# 翻转字符串


def reverse(str):
    if str == "":
        return ""
    data = reverse(str[1:]) + str[0]
    print("#", data)
    return data


r = reverse("Hello")
print(r)
