# a121_catch_a_turtle.py

#-----import statements-----
import random as rand
import turtle as turt
import leaderboard as lb

#-----game configuration----
score = 0
started = False
colors = ["gold", "orange", "red", "green", "blue", "purple", "gray", "black", "white"]
sizes = [3, 2.5, 2, 1.5, 1, 0.5]

# leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("Please enter your name: ")

#-----initialize turtle-----
font_setup = ("Arial", 20, "normal")

score_writer = turt.Turtle()
score_writer.ht()
score_writer.penup()
score_writer.goto(-300, -300)

thorn = turt.Turtle("circle")
thorn.shapesize(2, 2, 1)
thorn.color("black")
thorn.fillcolor("#2B5C38")
thorn.penup()
thorn.write("Click here to start!", align="center", font=font_setup)
thorn.goto(0, -20)

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
    thorn.clear()
    thorn.goto(0, 0)
    started = True

def thorn_clicked(x, y):
    if not started:
        start_game()
    else:
        if not timer_up:
            update_score()
            change_position()
        else:
            thorn.ht()

def color_and_size():
    thorn.fillcolor(rand.choice(colors))
    size_shape = rand.choice(sizes)
    thorn.stamp()
    thorn.shapesize(size_shape, size_shape, 1)
    thorn.fillcolor("#2B5C38")

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
    thorn.ht()
    thorn.goto(xcoord, ycoord)
    thorn.st()

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up!", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
    global leader_scores_list
    global leader_names_list
    global score
    global thorn

    # load all the leaderboard records into the lists
    lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

    # TODO
    if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
        lb.draw_leaderboard(leader_names_list, leader_scores_list, True, thorn, score)

    else:
        lb.draw_leaderboard(leader_names_list, leader_scores_list, False, thorn, score)



#-----events----------------

thorn.onclick(thorn_clicked)
    
wn = turt.Screen()
wn.bgcolor("yellow")
wn.ontimer(countdown, counter_interval)
wn.mainloop()