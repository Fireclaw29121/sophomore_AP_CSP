# a121_catch_a_turtle.py

#-----import statements-----
import random as rand
import turtle as turt

#-----game configuration----


#-----initialize turtle-----
thorn = turt.Turtle("circle")
thorn.shapesize(2, 2, 1)
thorn.color("black")
thorn.fillcolor("#2B5C38")
thorn.penup()

#-----game functions--------
def thorn_clicked(x, y):
    print("Found me, aw man...")

#-----events----------------
thorn.onclick(thorn_clicked)

wn = turt.Screen()
wn.mainloop()