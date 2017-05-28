import requests

'''
try :
    page = requests.get("https://item.jd.com/3245058.html")
    page.raise_for_status()
    page.encoding = page.apparent_encoding
    print(page.text)
except:
    print("错误")

'''


# 爬取亚马逊
def fun():
    try:
        url = "https://www.amazon.cn/dp/B00JZ96ZI8/ref=gwgfloorv1_BMVD_a_1?pf_rd_p=3399e1ca-b03f-4b01-8455-0c17dcc9273a&pf_rd_s=desktop-8&pf_rd_t=36701&pf_rd_i=desktop&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=8CGDKM3NHWQ8VABYKYXV&pf_rd_r=8CGDKM3NHWQ8VABYKYXV&pf_rd_p=3399e1ca-b03f-4b01-8455-0c17dcc9273a"
        page = requests.get(url)
        page.raise_for_status()
        page.encoding = page.apparent_encoding
        return page.text
    except:
        print("错误")


def fun3():
    url = "http://www.baidu.com/s"
    kv = {"wd": "Python"}
    result = requests.get(url, params=kv)
    print(result.text)


fun3()
