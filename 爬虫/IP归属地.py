# 查询一个ip的归属地
import requests

url = "http://www.ip138.com/ips138.asp"
kv = {'ip': '210.45.88.60'}
r = requests.get(url, params=kv)
r.encoding = r.apparent_encoding
print(r.status_code)
print(r.text)
