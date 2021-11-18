# a121_catch_a_turtle.py

#-----import statements-----
import random as rand
import turtle as turt

#-----game configuration----
score = 0

#-----initialize turtle-----
thorn = turt.Turtle("circle")
thorn.shapesize(2, 2, 1)
thorn.color("black")
thorn.fillcolor("#2B5C38")
thorn.penup()

#-----game functions--------
def thorn_clicked(x, y):
    print("Found me, aw man...")
    update_score()
    change_position()

def update_score():
    global score
    score += 1
    text = "Score: "+str(score)
    print(text)

def change_position():
    xcoord = rand.randint(-400, 400)
    ycoord = rand.randint(-300, 300)
    thorn.ht()
    thorn.goto(xcoord, ycoord)
    thorn.st()


#-----events----------------
thorn.onclick(thorn_clicked)

wn = turt.Screen()
wn.mainloop()