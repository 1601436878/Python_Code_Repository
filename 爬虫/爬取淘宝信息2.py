import requests
import re


def getHTMLText(url):
    try:
        result = requests.get(url)
        result.encoding = result.apparent_encoding
        result.raise_for_status()
        return result.text
    except:
        print("获取页面失败")


def parsePage(infoList, page):
    try:
        name = re.findall(r'\"raw_title\"\:\".*?\"',page)
        price = re.findall(r'\"view_price\"\:\"[\d\.]*\"',page)
        for i in range(len(name)):
            namedata = eval(name[i].split(":")[1])
            pricedata = eval(price[i].split(":")[1])
            infoList.append([namedata,pricedata])
    except:
        print("解析页面错误")


def printGoodList(infoList):
    tempStr = "{0:4}\t{1:{3}<40}\t{2:8}"
    print(tempStr.format("序号", "商品名称", "商品价格",chr(12288)))
    count = 0
    for i in infoList:
        count = count + 1
        print(tempStr.format(count, i[0], i[1], chr(12288)))


def main():
    goods = "书包"
    start_url =  'https://s.taobao.com/search?q=' + goods
    depth = 10
    infoList = []
    for i in range(depth):
        try:
            page = getHTMLText(start_url+"s="+str(44*i))
            parsePage(infoList, page)
        except:
            print("失败")

    printGoodList(infoList)


if __name__ == "__main__":
    main()