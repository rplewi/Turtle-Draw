from turtle import Turtle, Screen, sys, math

proceed = False
while not proceed:
    textFile = input("Please input the name of the text file: ").strip()
    try:
        TESTFILE = open(textFile, 'r')
        proceed = True
    except:
        print("File does not exist")


TESTFILE = textFile
drawArea = Screen()
drawArea.bgcolor('white')
drawArea.setup(height = 450, width = 450)

TOTAL = 0 
Sam = Turtle()
Sam.speed(0)
Sam.penup()
TESTFILE = open(textFile, 'r')

for line in TESTFILE:
    print(line)
    parts = line.split(' ')
    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])
        totalDist = 

        '''
        print(Sam.distance(x,y))
        totalxy = Sam.distance(x,y)
        TOTAL += totalxy
        '''
        Sam.color(color)
        Sam.goto(x,y)
        
        Sam.pendown()
    elif (len(parts) == 1):
        Sam.penup()
print(TOTAL)

def close_window():
    drawArea.bye()

drawArea.listen()
drawArea.onkey(close_window, "Return")
drawArea.mainloop()
TESTFILE.close()