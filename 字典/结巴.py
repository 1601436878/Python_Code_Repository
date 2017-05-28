import jieba

str = "中国是一个伟大的国家"
data = jieba.lcut(str)
print(data)
