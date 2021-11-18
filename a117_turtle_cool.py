#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
from math import sqrt
import turtle as trtl
import random
import os
trtl.colormode(255)

# create an empty list of turtles
my_turtles = []

# use interesting shapes
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]

# Ask for number of sides
num_sides = int(input("How many sides does this shape have?\n"))
length = int(input("How long is a side?\n"))
width = float(input("How wide is the pen?\n"))

if num_sides >= 30:
    speedflag = True



for turt in range(num_sides):

    # This code picks a random shape from the list above and picks random (r, g, b) for color.
    t_shape = turtle_shapes[random.randint(0, 5)]

    t_color_part1 = int(random.uniform(0.0, 255.0))
    t_color_part2 = int(random.uniform(0.0, 255.0))
    t_color_part3 = int(random.uniform(0.0, 255.0))
    t_color = (t_color_part1, t_color_part2, t_color_part3)


    t = trtl.Turtle(shape=t_shape)
    t.ht()
    t.color(t_color)

    # This code sets the pensize and turtle size accordingly. 
    # It also makes the turtle faster, if needed.
    t.pensize(width)
    size = int(sqrt(width))
    t.turtlesize(size, size, 1)
    if speedflag:
        t.speed(0)

    # Adds this turtle to the list
    my_turtles.append(t)

#  Initial Position
startx = -100
starty = 200
turn = 0
iter = 1
# Draws with each turtle
for t in my_turtles:
    t.penup()
    t.goto(startx, starty)
    t.right(turn)
    t.pendown()
    t.st()
     
    # Move turtle, turn for the next turtle. 
    t.forward(length*iter)
    turn+=(360/num_sides)

    #iter+=1 (This variable used to increase, but I dummied it out.)

    # Assigning start for the next turtle.
    startx = t.xcor()
    starty = t.ycor()


os.system('clear')
wn = trtl.Screen()
wn.mainloop()