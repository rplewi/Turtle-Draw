from turtle import Turtle, Screen, sys, math

proceed = False
while not proceed:
    #textFile = input("Please input the name of the text file: ").strip()
    textFile = 'testfile.txt' #delete this before submit and uncomment the line above 
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
skipStop = False
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
        Sam.color(color)
        if not skipStop:
            print(f'Distance: {Sam.distance(x,y)}') #https://docs.python.org/3/tutorial/inputoutput.html
            TOTAL += Sam.distance(x,y)
        else:
            skipStop = False
        Sam.goto(x,y)
        Sam.pendown()
    elif (len(parts) == 1):
        skipStop = True
        Sam.penup()
print(f'Total: {TOTAL}')

def close_window():
    drawArea.bye()

drawArea.listen()
drawArea.onkey(close_window, "Return")
drawArea.mainloop()
TESTFILE.close()