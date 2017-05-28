# 2017-5-21
import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        result = requests.get(url, timeout=30)
        result.raise_for_status()
        result.encoding = result.apparent_encoding
        return result.text
    except:
        return ""


def fillUnivList(uList, HTMLText):
    soup = BeautifulSoup(HTMLText, "html.parser")
    trs = soup.tbody.children
    for tr in trs:
        if isinstance(tr, bs4.element.Tag):
            tds = tr.find_all("td")
            uList.append([tds[0].string, tds[1].string, tds[3].string])


def printUnivList(uList, num):
    mod = "{0:{3}^10}{1:{3}^10}{2:{3}^10}"
    print(mod.format("排名", "学校名称", "总分", chr(12288)))
    for list in range(num):
        i = uList[list]
        print(mod.format(i[0], i[1], i[2], chr(12288)))


def main():
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    uinfo = []
    HTMLText = getHTMLText(url)
    fillUnivList(uinfo, HTMLText)
    printUnivList(uinfo, 20)


if __name__ == "__main__":
    main()
