from turtle import Turtle, Screen


win=Screen()
win.bgcolor("White")
win.setup(450,450,450,450)

TEXTFILENAME = 'testfile.txt'

myTurtle = Turtle()
myTurtle.speed(10)
myTurtle.penup()

print('reading lines now')
f = open(TEXTFILENAME, 'r')
file_contents = f.readline()
while file_contents:
    print(file_contents, end='')
    parts = file_contents.split(' ')

    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        myTurtle.pendown()
        myTurtle.color(color)
        myTurtle.goto(x,y)

        myTurtle.color(color)
        myTurtle.goto(x,y)

        myTurtle.down()
        
    if (len(parts) == 1):
        myTurtle.up()
    
    file_contents = f.readline()
    
f.close()

print('/nEnd')