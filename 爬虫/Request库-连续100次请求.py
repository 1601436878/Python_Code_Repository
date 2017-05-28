import requests
import time


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return "访问成功"
    except:
        return "产生异常"


def atime():
    statr = time.time()
    url = 'http://www.baidu.com'
    for i in range(100):
        getHTMLText(url)
    end = time.time()
    return end - statr


if __name__ == "__main__":
    # url = 'http://www.baidu.com'
    print(atime())
