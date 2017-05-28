###
import turtle


def main():
    p = turtle.Turtle()
    p.color("green")
    p.pensize(1)
    p.speed(0)
    p.seth(90)
    p.hideturtle()

    p.penup()
    p.goto(0, -200)
    p.pendown()

    t = tree([p], 200, 65, 0.6375)


def tree(list, len, angle, rate):
    if len >= 2:
        list2 = []
        for p in list:
            p.fd(len)
            q = p.clone()
            q.left(angle)
            p.right(angle)
            list2.append(q)
            list2.append(p)
        tree(list2, len * rate, angle, rate)


main()
