# 统计单词数量
import turtle

worddata = {}
wordname = []
wordnum = []
xScale = 50
yScale = 16


def generate(line):
    list = line.split()
    for i in list:
        if i in worddata:
            worddata[i] += 1
        else:
            worddata[i] = 1


def drawLine(p, x1, y1, x2, y2):
    p.penup()
    p.goto(x1, y1)
    p.pendown()
    p.goto(x2, y2)


def replacePun(line):
    for ch in line:
        if ch in ",.":
            line.replace(ch, " ")


def drawText(p, x, y, text):  # 向页面中写字
    p.penup()
    p.goto(x, y)
    p.pendown()
    p.write(text)


def draw(pen):
    drawLine(pen, -100, -100, 300, -100)
    drawLine(pen, -100, 360, -100, -100)
    for i in range(len(wordname)):
        x = int(i * xScale) - 90
        y = -120
        print(x, y)
        drawText(pen, x, y, wordname[i])
        drawBar(pen, x, -100, wordnum[i])


def drawBar(p, x, y, num):
    height = int(num * yScale)
    height = y + height
    print("height", height)
    drawLine(p, x, y, x, height)
    drawLine(p, x, height, x + 10, height)
    drawLine(p, x + 10, height, x + 10, y)


def main():
    filein = open("单词统计文件", "r")
    filedata = filein.readlines()
    for line in filedata:
        replacePun(line)
        generate(line)

    print("#", filedata)
    print(worddata)

    for i in worddata.items():
        wordname.append(i[0])
        wordnum.append(i[1])

    print(wordname)
    print(wordnum)
    turtle.title("统计单词数量")
    pen = turtle.Turtle()
    pen.color("black")
    pen.hideturtle()
    pen.pensize(3)
    draw(pen)


main()
