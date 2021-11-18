#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  color_use = turtle_colors.pop()
  t.color(color_use)
  my_turtles.append(t)

#  
startx = 0
starty = 0
heading = 0
turn = 40
#
for t in my_turtles:
    t.setheading(heading*turn)
    t.goto(startx, starty)
    t.pendown()
    t.forward(50+20*heading)
    
    heading+=1  

#	
    startx = t.xcor()
    starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()