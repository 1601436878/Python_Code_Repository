# pi.py
'''
from random import random
from math import sqrt
from time import clock
DARTS = 12000000
hits = 0
clock()
for i in range(1,DARTS):
    x, y = random(), random()
    dist = sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print("Pi的值是 %s" % pi)
print("程序运行时间是 %-5.5ss" % clock())


import math
import time
import random
hit = 0
# x , y = 0, 0
count = 100000000
time.clock()
for i in range(count):
    x, y = random.random(),random.random()
    r = math.sqrt(x**2+y**2)
    if r <= 1:
        hit+=1

pi = (hit / count) * 4
print (pi)
print("时间是: ",time.clock())
'''

# 2017 5 - 14
import math
import random
import time

count = 1000
hit = 0
time.clock()
x = 0

for i in range(count):
    x = random.random()
    y = random.random()
    rad = x ** 2 + y ** 2
    rad = math.sqrt(rad)
    if rad <= 1:
        hit += 1

r = (hit / count) * 4
print("pi的值为", r)
print("使用的时间：", time.clock())
print(x)
