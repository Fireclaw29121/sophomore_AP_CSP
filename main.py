#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic('background.gif')

apple = trtl.Turtle()

#Vars
groundheight = -165
xoffset = 13
yoffset = 32

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letters_assigner = letters
active_letters = []
inactive_letters = []
apples = []


#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
number_of_apples = 26
for i in range(number_of_apples):
    active_apple = trtl.Turtle()
    active_apple.ht()
    active_apple.penup()
    #Make a letter to associate it with here.
    num = rand.randint(0, (len(letters_assigner)-1))
    if i < 5:
      key =  letters_assigner[num]
      active_letters.append(key)
    else:
       key =  letters_assigner[num]
       inactive_letters.append(key)
    
    letters_assigner.pop(num)
    apples.append(active_apple) #apples is a list of format [active_apple.Turtle(), "a", active_apple.Turtle(), "b", etc....]
    apples.append(key)
#-----functions-----


# given a turtle and letter corresponding, drop it, hide the turtle, and pop both from the list(s)

def drop_apple(active_apple, key_press):
  global apples
  global active_letters
  global letters 

  #Falls
  active_apple.clear()
  wn.tracer(True)
  active_apple.goto(active_apple.xcor(), groundheight)

  #Remove from lists - due to the method we're using we can't hardcode anything so index() is our function of choice, 
  # as it finds where a letter is located in a list (the first occurence of it, but as it's also the only occurence, this works.)
  active_num = active_letters.index(key_press)
  apple_num = apples.index(key_press)

  apples.pop(apple_num)
  apples.pop(apple_num-1)
  active_letters.pop(active_num)

  # Hide turtle.
  active_apple.ht()


# Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and draws that letter on that turtle (apple)
def draw_letter(active_apple, key_press):
  wn.tracer(False)
  x_coord = active_apple.xcor()-xoffset
  y_coord = active_apple.ycor()-yoffset

  # Place a white letter over the center to show what you must type.
  active_apple.goto(x_coord, y_coord)
  active_apple.color("white")
  active_apple.write(key_press.upper(), font=("Arial", 36, "bold"))
  active_apple.goto((x_coord+xoffset), (y_coord+yoffset))
  wn.update()
  wn.tracer(True)

#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen
def draw_apple(active_apple, key_press):
  active_apple.shape(apple_image)
  draw_letter(active_apple, key_press)

#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. Associate the 
# turtle with a new letter selected at random from the list of letters


# This was slightly disobeyed, as there is turtle-per-letter, so no input is needed.
# Reposition chooses a random letter to put on the tree, and therefore needs nothing. 
# It gets it out of the inactive list and puts it on the active one, and then puts it on the tree.
def reposition():
  global inactive_letters
  global apples
  global active_letters

  if inactive_letters == []:
    if len(active_letters) == 0:
      print("Yay!")
      ender = trtl.Turtle()
      ender.ht()
      ender.penup()
      ender.goto(-300, -300)
      ender.write("You did it! Click on the screen to exit...", font=("Arial", 36, "bold"))
      trtl.exitonclick()
  else:
  #Choose a random letter and its corresponding apple.
    num = rand.randint(0, (len(inactive_letters)-1))
    key = inactive_letters[num]

    inactive_letters.pop(num)
    active_letters.append(key)

    apples_index = apples.index(key)
    active_apple = apples[apples_index-1]

  # Move them, draw
    x_coord = rand.randint(-150, 150)
    y_coord = rand.randint(0, 150)
    active_apple.goto(x_coord, y_coord)
    active_apple.st()
    draw_apple(active_apple, key)

# Creates a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the 
# apple and letter have dropped, call the apple reseting function.
def find_apple(key):

  apples_index = apples.index(key)
  active_apple = apples[apples_index-1]

  drop_apple(active_apple, key)
  reposition()



# Defines a set of functions per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.

def a_apple():
  global active_letters
  global inactive_letters
  if "a" in active_letters:
    find_apple("a")


def b_apple():
  global active_letters
  global inactive_letters
  if "b" in active_letters:
    find_apple("b")

def c_apple():
  global active_letters
  global inactive_letters
  if "c" in active_letters:
    find_apple("c")

def d_apple():
  global active_letters
  global inactive_letters
  if "d" in active_letters:
    find_apple("d")


def e_apple():
  global active_letters
  global inactive_letters
  if "e" in active_letters:
    find_apple("e")


def f_apple():
  global active_letters
  global inactive_letters
  if "f" in active_letters:
    find_apple("f")


def g_apple():
  global active_letters
  global inactive_letters
  if "g" in active_letters:
    find_apple("g")


def h_apple():
  global active_letters
  global inactive_letters
  if "h" in active_letters:
    find_apple("h")


def i_apple():
  global active_letters
  global inactive_letters
  if "i" in active_letters:
    find_apple("i")


def j_apple():
  global active_letters
  global inactive_letters
  if "j" in active_letters:
    find_apple("j")


def k_apple():
  global active_letters
  global inactive_letters
  if "k" in active_letters:
    find_apple("k")


def l_apple():
  global active_letters
  global inactive_letters
  if "l" in active_letters:
    find_apple("l")


def m_apple():
  global active_letters
  global inactive_letters
  if "m" in active_letters:
    find_apple("m")


def n_apple():
  global active_letters
  global inactive_letters
  if "n" in active_letters:
    find_apple("n")


def o_apple():
  global active_letters
  global inactive_letters
  if "o" in active_letters:
    find_apple("o")


def p_apple():
  global active_letters
  global inactive_letters
  if "p" in active_letters:
    find_apple("p")


def q_apple():
  global active_letters
  global inactive_letters
  if "q" in active_letters:
    find_apple("q")


def r_apple():
  global active_letters
  global inactive_letters
  if "r" in active_letters:
    find_apple("r")


def s_apple():
  global active_letters
  global inactive_letters
  if "s" in active_letters:
    find_apple("s")


def t_apple():
  global active_letters
  global inactive_letters
  if "t" in active_letters:
    find_apple("t")

def u_apple():
  global active_letters
  global inactive_letters
  if "u" in active_letters:
    find_apple("u")


def v_apple():
  global active_letters
  global inactive_letters
  if "v" in active_letters:
    find_apple("v")


def w_apple():
  global active_letters
  global inactive_letters
  if "w" in active_letters:
    find_apple("w")


def x_apple():
  global active_letters
  global inactive_letters
  if "x" in active_letters:
    find_apple("x")


def y_apple():
  global active_letters
  global inactive_letters
  if "y" in active_letters:
    find_apple("y")


def z_apple():
  global active_letters
  global inactive_letters
  if "z" in active_letters:
    find_apple("z")

#-----function calls-----
#Setup game with the first few apples
for key in active_letters:
  #find its specific apple!
  apples_index = apples.index(key)
  active_apple = apples[apples_index-1]  

  #Use the final part of reposition for the first 5!
  x_coord = rand.randint(-150, 150)
  y_coord = rand.randint(0, 150)
  active_apple.goto(x_coord, y_coord)
  active_apple.st()

  draw_apple(active_apple, key)

  
# Listen for each key
wn.onkeypress(a_apple, "a")
wn.onkeypress(b_apple, "b")
wn.onkeypress(c_apple, "c")
wn.onkeypress(d_apple, "d")
wn.onkeypress(e_apple, "e")
wn.onkeypress(f_apple, "f")
wn.onkeypress(g_apple, "g")
wn.onkeypress(h_apple, "h")
wn.onkeypress(i_apple, "i")
wn.onkeypress(j_apple, "j")
wn.onkeypress(k_apple, "k")
wn.onkeypress(l_apple, "l")
wn.onkeypress(m_apple, "m")
wn.onkeypress(n_apple, "n")
wn.onkeypress(o_apple, "o")
wn.onkeypress(p_apple, "p")
wn.onkeypress(q_apple, "q")
wn.onkeypress(r_apple, "r")
wn.onkeypress(s_apple, "s")
wn.onkeypress(t_apple, "t")
wn.onkeypress(u_apple, "u")
wn.onkeypress(v_apple, "v")
wn.onkeypress(w_apple, "w")
wn.onkeypress(x_apple, "x")
wn.onkeypress(y_apple, "y")
wn.onkeypress(z_apple, "z")

wn.listen()
wn.mainloop()