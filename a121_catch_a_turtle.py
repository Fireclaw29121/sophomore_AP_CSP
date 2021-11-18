# a121_catch_a_turtle.py

#-----import statements-----
import random as rand
import turtle as turt

#-----game configuration----
score = 0
started = False
sizes = [4]

wn = turt.Screen()
wn.addshape("Spamton_battle_static.gif")
wn.addshape("Spamton_battle_spared.gif")
#-----initialize turtle-----
font_setup = ("Arial", 20, "normal")

score_writer = turt.Turtle()
score_writer.ht()
score_writer.penup()
score_writer.goto(-300, -300)

spamton = turt.Turtle(shape="Spamton_battle_static.gif")
spamton.shapesize(2, 2, 1)
spamton.color("black")
spamton.fillcolor("#2B5C38")
spamton.penup()
spamton.write("Click here to start!", align="center", font=font_setup)
spamton.goto(0, -40)

counter =  turt.Turtle()
counter.ht()
counter.penup()
counter.goto(200, -300)

#-----It's the final countdown!-----
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----game functions--------
def start_game():
    global started
    spamton.clear()
    spamton.goto(0, 0)
    started = True

def spamton_clicked(x, y):
    if not started:
        start_game()
    else:
        if not timer_up:
            update_score()
            change_position()
            print("[[BIG SHOT]]")
        else:
            spamton.ht()

def color_and_size():
    spamton.shape("Spamton_battle_spared.gif")
    size_shape = rand.choice(sizes)
    spamton.stamp()
    spamton.shapesize(size_shape, size_shape, 1)
    spamton.shape("Spamton_battle_static.gif")

def update_score():
    global score
    score += 1
    text = "Score: "+str(score)
    score_writer.clear()
    score_writer.write(text, font=font_setup)

def change_position():
    xcoord = rand.randint(-200, 200)
    ycoord = rand.randint(-200, 200)
    color_and_size()
    spamton.ht()
    spamton.goto(xcoord, ycoord)
    spamton.st()

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up!", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)



#-----events---------------- 


wn.bgcolor("yellow")
spamton.onclick(spamton_clicked)
wn.ontimer(countdown, counter_interval)
wn.mainloop()