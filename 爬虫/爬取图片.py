# 获取一张图片URL的文件
import requests
import os

'''
url = "https://imgsa.baidu.com/news/q%3D100/sign=a450d57e2aa4462378caa162a8237246/902397dda144ad3490f02883daa20cf431ad8563.jpg"
result = requests.get(url)
print(result.status_code)
path = "/home/twilight/桌面/Python/"+url.split("/")[-1]
with open(path, "wb") as f :
    f.write(result.content)
    f.close()
    print("文件保存成功")
'''


def getName(url):
    str = url.split("/")[-1]
    print(str)
    return "D:/" + str


def getImg(url):
    try:
        results = requests.get(url)
        results.raise_for_status()
        with open(getName(url), "wb") as file:
            file.write(results.content)
            file.close()
            print("保存成功")

    except:
        print("保存文件失败")


getImg(
    "https://imgsa.baidu.com/news/q%3D100/sign=a450d57e2aa4462378caa162a8237246/902397dda144ad3490f02883daa20cf431ad8563.jpg")
