# 测试布尔值
'''
ans = input("请输入[Tom]:")
if ans != "":
    print("你输入的值为：",ans)
else :
    ans = "Tom"
    print("自动补全为：",ans)


ans = input("请输入[Tom]:")
if ans:
    print("你输入的值为：",ans)
else :
    ans = "Tom"
    print("自动补全为：",ans)
'''

ans = input("请输入[Tom]:")
flavor = False or "Tom"
print(flavor)
