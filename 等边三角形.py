# 绘制一个等边三角形
import turtle

len = 200
turtle.setup(800, 600, 100, 100)
turtle.pensize(5)
turtle.pencolor("blue")
turtle.seth(0)
turtle.fd(len)
turtle.seth(120)
turtle.fd(len)
turtle.seth(-120)
turtle.fd(len)
