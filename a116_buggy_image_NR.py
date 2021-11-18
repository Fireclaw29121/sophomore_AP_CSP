#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()

#Draw spider body
spider.goto(0, -20)
spider.pensize(40)
spider.circle(20)

# Configure spider legs
legs = 8
length = 70
rotation = 320 / legs
spider.pensize(5)


# Draw spider legs

# Left side
iter = 0
while (iter < int(legs/2)):
    spider.goto(0,0)
    spider.setheading(rotation*iter+110)
    spider.forward((4*length)/5)
    spider.left(20)
    spider.forward(length/5)
    iter+=1

# Right side
iter=0
while (iter < int(legs/2)):
    spider.goto(0,0)
    spider.setheading(-rotation*iter+70)
    spider.forward((4*length)/5)
    spider.right(20)
    spider.forward(length/5)
    iter+=1

# Eyes
xpos = -15
for eye in range(2):
    spider.pencolor("magenta")
    spider.penup()
    spider.goto(xpos, -30)
    spider.pendown()
    spider.circle(5)
    xpos+=20

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()