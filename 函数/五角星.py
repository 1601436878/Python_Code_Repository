# 绘画五角星
import turtle

p = turtle.Turtle()
p.hideturtle()
p.penup()
p.setx(-100)
p.sety(100)
p.pendown()
p.speed(1)
p.pensize(5)
p.color("black", "yellow")  # Return or set the pencolor and fillcolor.
p.begin_fill()
for i in range(5):
    p.forward(200)
    p.right(144)
p.end_fill()
