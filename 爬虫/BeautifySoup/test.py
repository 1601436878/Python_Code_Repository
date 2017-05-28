import bs4
import requests

if __name__ == '__main__':
    result = requests.get("http://www.baidu.com")
    result.encoding = result.apparent_encoding
    soup = bs4.BeautifulSoup(result.text, "html.parser")
    soup.prettify()
