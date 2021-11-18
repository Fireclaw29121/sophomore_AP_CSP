'''
Flag of Norway
Date: 10.18.21
Author: Nino Roshi

This code draws the Flag of Norway using the colors and proportions specified on 
https://en.wikipedia.org/wiki/Flag_of_Norway.

If the user permits it, the code then goes on to recreate the famous "Wait, it's ALL Norway?" meme, outlining
and labeling the flags of Indonesia, Poland, France, Finland, and Thailand, all of which are present within the 
flag of Norway.
'''

import turtle

# Initialize 2 turtles: norway, which draws the flag, and labeler, which does the optional section. 
norway = turtle.Turtle()
labeler = turtle.Turtle()

norway.ht()
labeler.ht()
labeler.speed(6)
norway.speed(6)


# List of Countries
countries = ["Norway", "Indonesia", "Poland", "Finland", "France", "Thailand"]

'''
The Flag of Norway is in a 22:16 ratio, making the length 440 px and height 320 px. The flag is centered around
(0, 0), therefore the top-left corner is at (-220, 160) and the bottom-right at (220, -160)

The top goes in a 6:1:2:1:12 (length-wise) ratio, and the side in a 6:1:2:1:6 ratio. 

The colors are Red - in hex as #BA0C2F, and Blue in hex as #00205B
'''

norred = "#BA0C2F"
norblue = "#00205B"
norwhite = "#FFFFFF"

# Red Background
norway.color(norred, norred)
norway.penup()
norway.goto(-220, 160)
norway.setheading(0)
norway.pendown()

norway.begin_fill()

for x in range(2):
    norway.forward(440)
    norway.right(90)
    norway.forward(320)
    norway.right(90)

norway.end_fill()

# White Cross
norway.color(norwhite, norwhite)
norway.penup()
norway.goto(-220, 40)
norway.setheading(0)
norway.pendown()

norway.begin_fill()

# There is no efficient way of iterating through this, therefore it will be a block of statements.
norway.forward(120)
norway.left(90)
norway.forward(120)
norway.right(90)
norway.forward(80)
norway.right(90)
norway.forward(120)
norway.left(90)
norway.forward(240)
norway.right(90)
norway.forward(80)
norway.right(90)
norway.forward(240)
norway.left(90)
norway.forward(120)
norway.right(90)
norway.forward(80)
norway.right(90)
norway.forward(120)
norway.left(90)
norway.forward(120)
norway.right(90)
norway.forward(80)

norway.end_fill()


#Blue Cross
norway.color(norblue, norblue)
norway.penup()
norway.goto(-220, 20)
norway.setheading(0)
norway.pendown()

norway.begin_fill()

# There is no efficient way of iterating through this, therefore it will be a block of statements.
norway.forward(140)
norway.left(90)
norway.forward(140)
norway.right(90)
norway.forward(40)
norway.right(90)
norway.forward(140)
norway.left(90)
norway.forward(260)
norway.right(90)
norway.forward(40)
norway.right(90)
norway.forward(260)
norway.left(90)
norway.forward(140)
norway.right(90)
norway.forward(40)
norway.right(90)
norway.forward(140)
norway.left(90)
norway.forward(140)
norway.right(90)
norway.forward(40)

norway.end_fill()

# Outline
norway.pencolor("black")
norway.penup()
norway.goto(-220, 160)
norway.setheading(0)
norway.pendown()

for x in range(2):
    norway.forward(440)
    norway.right(90)
    norway.forward(320)
    norway.right(90)


#Remove Norway as it's now displayed.
countries.pop(0)


#Prompt user to continue
response = input("Do you want to see some other flags? \n(Type something and hit ENTER to continue. Otherwise, hit space and ENTER to quit.)\n")

if response != ' ':
    '''
    Drawing Flags

    A few flags need to be outlined. If you think of the whole flag as a 22x16 rectangle, then we have the following. 

    Indonesia's Flag is 2x3
    Poland's is 5x8 - as this doesn't fit it will be reduced to 2.5x4
    Finland's is 11x18 - however it will be adjested to 4x7
    France's and Thailand's are also 2:3
    Thailand's is technically 6:9 to fit its design.

    One unit is 20 pixels.
    
    '''
    labeler.pensize(4)

    # Poland
    labeler.penup()
    labeler.goto(-180, -20)
    labeler.setheading(0)
    labeler.pendown()

    for x in range(2):
        labeler.forward(60)
        labeler.right(90)
        labeler.forward(40)
        labeler.right(90)

    labeler.penup()
    labeler.goto(-180, -80)
    labeler.color("white")
    labeler.write("Poland")
    labeler.color("black")
    countries.pop(2)

    # Indonesia
    labeler.penup()
    labeler.goto(-184, 60)
    labeler.setheading(0)
    labeler.pendown()

    for x in range(2):
        labeler.forward(64)
        labeler.right(90)
        labeler.forward(40)
        labeler.right(90)

    labeler.penup()
    labeler.goto(-184, 60)
    labeler.color("white")
    labeler.write("Indonesia")
    labeler.color("black")
    countries.pop(1)

    # Finland
    labeler.penup()
    labeler.goto(-120, 40)
    labeler.setheading(0)
    labeler.pendown()

    for x in range(2):
        labeler.forward(140)
        labeler.right(90)
        labeler.forward(80)
        labeler.right(90)

    labeler.penup()
    labeler.goto(-15, 40)
    labeler.color("white")
    labeler.write("Finland")
    labeler.color("black")
    countries.pop(0)

    # Thailand
    labeler.penup()
    labeler.goto(40, 60)
    labeler.setheading(0)
    labeler.pendown()

    for x in range(2):
        labeler.forward(180)
        labeler.right(90)
        labeler.forward(120)
        labeler.right(90)

    labeler.penup()
    labeler.goto(40, 60)
    labeler.color("white")
    labeler.write("Thailand")
    labeler.color("black")
    countries.pop()

    # France
    labeler.penup()
    labeler.goto(-60, -60)
    labeler.setheading(0)
    labeler.pendown()

    for x in range(2):
        labeler.forward(60)
        labeler.right(90)
        labeler.forward(40)
        labeler.right(90)

    labeler.penup()
    labeler.goto(-15, -60)
    labeler.color("white")
    labeler.write("France")
    labeler.color("black")
    countries.pop()

    #Finish the joke
    labeler.setheading(0)
    labeler.penup()
    labeler.goto(-60, 200)
    labeler.write("Wait, it's ALL Norway?")
    labeler.goto(-65, 207)
    labeler.st()
    labeler.stamp()

    labeler.goto(-60, -200)
    labeler.write("Always has been.")
    labeler.goto(-65, -193)
    labeler.stamp()
    
    #Check for success
    if countries == []:
        print("All displayed. Please look at the new flags.")
else:
    print("You have chosen not to display", end=" ")
    for country in countries:
        if country == "Thailand":
            print("and "+country+".")
        else:
            print(country+",", end=" ")



# Screen object persists
wn = turtle.Screen()
wn.mainloop()