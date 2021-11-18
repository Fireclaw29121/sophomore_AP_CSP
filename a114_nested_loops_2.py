#   a114_nested_loops_2.py 
import turtle as trtl

painter = trtl.Turtle()
painter.shape("circle")
painter.hideturtle()
painter.penup()
painter.speed(0)


while True:
    y = -200
    while (y < 200):
        y+=50
        x=-200 
        while (x < 200):
            x+=50
            painter.goto(x,y)
            painter.color("black")
            painter.stamp()
        
    x = -200
    while (x < 200):
        x+=50
        y=-200 
        while (y < 200):
            y+=50
            painter.goto(x,y)
            painter.color("navyblue")
            painter.stamp()
            

wn = trtl.Screen()
wn.mainloop()