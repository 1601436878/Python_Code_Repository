# 使用turtle库绘制蟒蛇
import turtle


def drawSnake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.circle(rad, angle)  # 沿着半径为rad的圆转angle度
        turtle.circle(-rad, angle)  # rad为正逆时针向上，负数表示顺时针向下
    turtle.circle(rad, angle / 2)
    turtle.fd(rad)
    turtle.circle(neckrad + 1, 180)
    turtle.fd(rad * 2 / 3)


def main():
    turtle.setup(1300, 800, 0, 0)
    pythonsize = 30  # 蟒蛇的宽度
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")
    turtle.seth(-40)  # 设置开始绘制时的角度值，按照直角坐标的计算方式，从-40度开始
    drawSnake(40, 80, 5, pythonsize / 2)


main()

'''

turtle.setup(800,600,0,0)
turtle.pensize(10)
turtle.pencolor("blue")
turtle.seth(0)
turtle.circle(-150,360)
'''
