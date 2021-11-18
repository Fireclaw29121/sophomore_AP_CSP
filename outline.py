#   a123_apple_and_letters.py

import random as rand
import turtle

#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. 
def reposition_apple(active_apple):
    global letters
    if letters != []:
        x_coord = rand.randint(-150, 150)
        y_coord = rand.randint(0, 150)
        active_apple.goto(x_coord, y_coord)
        active_apple.st()
        wn.tracer(False)

#TODO Create a function that draws a new letter from the letter list.
def choose_letter():
    global letters
    global key_press
    num = rand.randint(0, (len(letters)-1))
    key_press = letters[num]
    letters.pop(num)

#TODO Create a function that takes a turtle (apple) as its parameter
# and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

def draw_apple(active_apple, key_press):
  active_apple.shape(apple_image)
  wn.update()

  wn.tracer(False)
  x_coord = active_apple.xcor()-13
  y_coord = active_apple.ycor()-36

  # Place a white A over the center to show what you must type.
  active_apple.goto(x_coord, y_coord)
  active_apple.color("white")
  active_apple.write(key_press.upper(), font=("Arial", 36, "bold"))
  wn.update()

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
number_of_apples = 26
apples = []
for i in range(number_of_apples):
    active_apple = trtl.Turtle()
    reposition_apple(active_apple)
    choose_letter()
    draw_apple(active_apple, key_press)
    apples.append(active_apple)

  

#TODO Create a function that takes a letter as its parameter, retrieve a
# random turtle (apple) and causes the turtle (apple) to drop from the tree and the letter 
# to disappear. Call the apple resetting function.

def drop_apple(key_press):

  global apples
  #select random apple


  #Flash a blue letter to signify that you've typed the right letter.
  wn.tracer(False)
  active_apple.clear()
  active_apple.color("blue")
  active_apple.goto(active_apple.xcor()-13, (active_apple.ycor()-36))
  active_apple.write(key_press.upper(), font=("Arial", 36, "bold"))
  active_apple.goto(active_apple.xcor()+13, (active_apple.ycor()+36))
  wn.update()
  active_apple.clear()

  #Falls
  wn.tracer(True)
  active_apple.goto(0, groundheight)


  wn.tracer(False)
  active_apple.goto(active_apple.xcor()-13, (groundheight-36))
  active_apple.color("white")
  active_apple.write(key_press.upper(), font=("Arial", 36, "bold"))
  active_apple.goto(active_apple.xcor()+13, (active_apple.ycor()+36))
  wn.update()

  active_apple.clear()
  active_apple.ht()
  


#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop an apple at random.

#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.

wn.listen()
trtl.mainloop()




'''
Repositioning apples: a guide

1. Create an apple.
2. Assign a letter
3. Choose a position.
4. Go to position. Show letter.
5. Wait for typing
6. Choose a random apple and drop it, regardless of what letter is, in fact, on the apple. 

'''