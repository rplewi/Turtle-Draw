from turtle import Turtle, Screen

win=Screen()
win.bgcolor("white")
win.setup(450,450,450,450)

sam=Turtle()
sam.pendown()
sam.speed(10)
sam.color("red")
sam.goto(10,19)
win.exitonclick()