#   a114_guess.py
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.penup()
painter.color("salmon")
painter.pensize(2)
painter.hideturtle()

spiral_space = 0



while True:
    spiral_space=0
    while (spiral_space < 75): 
        painter.goto(0,0)
        painter.right(20)
        painter.forward(spiral_space**2/17)
        painter.pendown()
        painter.circle(spiral_space)
        painter.penup()
        spiral_space = spiral_space + 1
        if (spiral_space % 5 == 0):
            painter.color("navy")
        if (spiral_space % 10 == 0):
            painter.color("salmon")
    painter.clear()