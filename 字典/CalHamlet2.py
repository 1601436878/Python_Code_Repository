# 计算哈姆雷特中单词的频率
def getText():
    file = open("hamlet.txt", "r")
    data = file.read().lower()
    for ch in data:
        if ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
            data = data.replace("ch", " ")
    return data


text = getText()
counts = {}
word = text.split()
for i in word:
    counts[i] = counts.get(i, 0) + 1

listdata = list(counts.items())
listdata.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    a, b = listdata[i]
    print("{0:<10}{1:>10}".format(a, b))
