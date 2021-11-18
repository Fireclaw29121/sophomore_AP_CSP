#   a114_nested_loops_4.py 
import turtle as trtl
import time

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(3)

painter.penup()
painter.goto(0, -200)
painter.pendown()
painter.circle(200)

numiter=0
while True:
    painter.penup()
    painter.goto(0, -200)
    painter.pendown()
    painter.circle(200)

    if numiter%2 == 0:
        painter.color("black", "black")
        painter.begin_fill()
    else:
        painter.color("red", "red")
        painter.begin_fill()

    painter.penup()
    painter.goto(-200, 0)
    painter.pendown()
    x = -200
    y = 0
    move_x = 1
    move_y = 1
    while (x < 200):

        while (y < 100):
            x = x + move_x
            y = y + move_y
            painter.goto(x,y)
        move_y = -1
    
        while (y > 0):
            x = x + move_x
            y = y + move_y
            painter.goto(x,y)
        move_y = 1

    painter.penup()
    painter.goto(-200, 0)
    painter.pendown()
    x = -200
    y = 0
    move_x = 1
    move_y = 1

    while (x < 200):

        while (y > -100):
            x = x + move_x
            y = y - move_y
            painter.goto(x,y)
        move_y = -1
    
        while (y < 0):
            x = x + move_x
            y = y - move_y
            painter.goto(x,y)
        move_y = 1

    
    painter.end_fill()
    time.sleep(3)
    numiter+=1

wn = trtl.Screen()
wn.mainloop()