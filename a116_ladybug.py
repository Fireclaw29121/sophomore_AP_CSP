#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

#draw & configure legs
num_legs = 8
length = 70
rotation = 360 / num_legs
ladybug.pensize(5)
ladybug.penup()

for x in range(num_legs):
    if x+1 == 3 or x+1 == 7:
        continue
    else:
        ladybug.goto(0,-40)
        ladybug.pendown()
        ladybug.setheading(rotation*x)
        ladybug.forward((4*length)/5)
        ladybug.penup()

# and body
ladybug.setheading(0)
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1


# Eyes
ladybug.pensize(2)
xpos = -15
for eye in range(2):
    ladybug.pencolor("white")
    ladybug.penup()
    ladybug.goto(xpos, 20)
    ladybug.pendown()
    ladybug.circle(5)
    xpos+=20


    


ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()