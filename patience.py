
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10487697
#    Student name: Lachlan Gilbert
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
# PATIENCE
#
# This assignment tests your skills at processing data stored in
# lists, creating reusable code and following instructions to display
# a complex visual image.  The incomplete Python program below is
# missing a crucial function, "deal_cards".  You are required to
# complete this function so that when the program is run it draws a
# game of Patience (also called Solitaire in the US), consisting of
# multiple stacks of cards in four suits.  See the instruction sheet
# accompanying this file for full details.
#
# Note that this assignment is in two parts, the second of which
# will be released only just before the final deadline.  This
# template file will be used for both parts and you will submit
# your final solution as a single Python 3 file, whether or not you
# complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must NOT rely on any non-standard Python
# modules that need to be installed separately, because the markers
# will not have access to such modules.

from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

# Constants defining the size of the card table
table_width = 1100 # width of the card table in pixels
table_height = 800 # height (actually depth) of the card table in pixels
canvas_border = 30 # border between playing area and window's edge in pixels
half_width = table_width // 2 # maximum x coordinate on table in either direction
half_height = table_height // 2 # maximum y coordinate on table in either direction

# Work out how wide some text is (in pixels)
def calculate_text_width(string, text_font = None):
    penup()
    home()
    write(string, align = 'left', move = True, font = text_font)
    text_width = xcor()
    undo() # write
    undo() # goto
    undo() # penup
    return text_width

# Constants used for drawing the coordinate axes
axis_font = ('Consolas', 10, 'normal') # font for drawing the axes
font_height = 14 # interline separation for text
tic_sep = 50 # gradations for the x and y scales shown on the screen
tics_width = calculate_text_width("-mmm -", axis_font) # width of y axis labels

# Constants defining the stacks of cards
stack_base = half_height - 25 # starting y coordinate for the stacks
num_stacks = 6 # how many locations there are for the stacks
stack_width = table_width / (num_stacks + 1) # max width of stacks
stack_gap = (table_width - num_stacks * stack_width) // (num_stacks + 1) # inter-stack gap
max_cards = 10 # maximum number of cards per stack

# Define the starting locations of each stack
stack_locations = [["Stack " + str(loc + 1),
                    [int(-half_width + (loc + 1) * stack_gap + loc * stack_width + stack_width / 2),
                     stack_base]] 
                    for loc in range(num_stacks)]

# Same as Turtle's write command, but writes upside down
def write_upside_down(string, **named_params):
    named_params['angle'] = 180
    tk_canvas = getscreen().cv
    tk_canvas.create_text(xcor(), -ycor(), named_params, text = string)

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# create the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image.
# By default the coordinate axes displayed - call the function
# with False as the argument to prevent this.
def create_drawing_canvas(show_axes = True):

    # Set up the drawing canvas
    setup(table_width + tics_width + canvas_border * 2,
          table_height + font_height + canvas_border * 2)

    # Draw as fast as possible
    tracer(False)

    # Make the background felt green and the pen a lighter colour
    bgcolor('green')
    pencolor('light green')

    # Lift the pen while drawing the axes
    penup()

    # Optionally draw x coordinates along the bottom of the table
    if show_axes:
        for x_coord in range(-half_width + tic_sep, half_width, tic_sep):
            goto(x_coord, -half_height - font_height)
            write('| ' + str(x_coord), align = 'left', font = axis_font)

    # Optionally draw y coordinates to the left of the table
    if show_axes:
        max_tic = int(stack_base / tic_sep) * tic_sep
        for y_coord in range(-max_tic, max_tic + tic_sep, tic_sep):
            goto(-half_width, y_coord - font_height / 2)
            write(str(y_coord).rjust(4) + ' -', font = axis_font, align = 'right')

    # Optionally mark each of the starting points for the stacks
    if show_axes:
        for name, location in stack_locations:
            # Draw the central dot
            goto(location)
            color('light green')
            dot(7)
            # Draw the horizontal line
            pensize(2)
            goto(location[0] - (stack_width // 2), location[1])
            setheading(0)
            pendown()
            forward(stack_width)
            penup()
            goto(location[0] -  (stack_width // 2), location[1] + 4)
            # Write the coordinate
            write(name + ': ' + str(location), font = axis_font)

    #Draw a border around the entire table
    penup()
    pensize(3)
    goto(-half_width, half_height) # top left
    pendown()
    goto(half_width, half_height) # top
    goto(half_width, -half_height) # right
    goto(-half_width, -half_height) # bottom
    goto(-half_width, half_height) # left

    # Reset everything, ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas.
# By default the cursor (turtle) is hidden when the program
# ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any partial drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the deal_cards function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_game function appearing below.  Your
# program must work correctly for any data set that can be generated
# by the random_game function.
#

# Each of these fixed games draws just one card
fixed_game_0 = [['Stack 1', 'Suit A', 10, 7]]
fixed_game_1 = [['Stack 2', 'Suit B', 1, 0]]
fixed_game_2 = [['Stack 3', 'Suit C', 1, 0]]
fixed_game_3 = [['Stack 4', 'Suit D', 1, 0]]

# Each of these fixed games draws several copies of just one card
fixed_game_4 = [['Stack 2', 'Suit A', 4, 0]]
fixed_game_5 = [['Stack 3', 'Suit B', 3, 0]]
fixed_game_6 = [['Stack 4', 'Suit C', 2, 0]]
fixed_game_7 = [['Stack 5', 'Suit D', 5, 0]]

# This fixed game draws each of the four cards once
fixed_game_8 = [['Stack 1', 'Suit A', 1, 0],
                ['Stack 2', 'Suit B', 1, 0],
                ['Stack 3', 'Suit C', 1, 0],
                ['Stack 4', 'Suit D', 1, 0]]

# These fixed games each contain a non-zero "extra" value
fixed_game_9 = [['Stack 3', 'Suit D', 4, 4]]
fixed_game_10 = [['Stack 4', 'Suit C', 3, 2]]
fixed_game_11 = [['Stack 5', 'Suit B', 2, 1]]
fixed_game_12 = [['Stack 6', 'Suit A', 5, 5]]

# These fixed games describe some "typical" layouts with multiple
# cards and suits. You can create more such data sets yourself
# by calling function random_game in the shell window

fixed_game_13 = \
 [['Stack 6', 'Suit D', 9, 6],
  ['Stack 4', 'Suit B', 5, 0],
  ['Stack 5', 'Suit B', 1, 1],
  ['Stack 2', 'Suit C', 4, 0]]
 
fixed_game_14 = \
 [['Stack 1', 'Suit C', 1, 0],
  ['Stack 5', 'Suit D', 2, 1],
  ['Stack 3', 'Suit A', 2, 0],
  ['Stack 2', 'Suit A', 8, 5],
  ['Stack 6', 'Suit C', 10, 0]]

fixed_game_15 = \
 [['Stack 3', 'Suit D', 0, 0],
  ['Stack 6', 'Suit B', 2, 0],
  ['Stack 2', 'Suit D', 6, 0],
  ['Stack 1', 'Suit C', 1, 0],
  ['Stack 4', 'Suit B', 1, 1],
  ['Stack 5', 'Suit A', 3, 0]]

fixed_game_16 = \
 [['Stack 6', 'Suit C', 8, 0],
  ['Stack 2', 'Suit C', 4, 4],
  ['Stack 5', 'Suit A', 9, 3],
  ['Stack 4', 'Suit C', 0, 0],
  ['Stack 1', 'Suit A', 5, 0],
  ['Stack 3', 'Suit B', 5, 0]]

fixed_game_17 = \
 [['Stack 4', 'Suit A', 6, 0],
  ['Stack 6', 'Suit C', 1, 1],
  ['Stack 5', 'Suit C', 4, 0],
  ['Stack 1', 'Suit D', 10, 0],
  ['Stack 3', 'Suit B', 9, 0],
  ['Stack 2', 'Suit D', 2, 2]]
 
# The "full_game" dataset describes a random game
# containing the maximum number of cards
stacks = ['Stack ' + str(stack_num+1) for stack_num in range(num_stacks)]
shuffle(stacks)
suits = ['Suit ' + chr(ord('A')+suit_num) for suit_num in range(4)]
shuffle(suits)
full_game = [[stacks[stack], suits[stack % 4], max_cards, randint(0, max_cards)]
             for stack in range(num_stacks)]

#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to mark your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a game
# of Patience to be drawn.  Your program must work for any data set 
# returned by this function.  The results returned by calling this 
# function will be used as the argument to your deal_cards function 
# during marking. For convenience during code development and marking 
# this function also prints the game data to the shell window.
#
# Each of the data sets generated is a list specifying a set of
# card stacks to be drawn. Each specification consists of the
# following parts:
#
# a) Which stack is being described, from Stack 1 to num_stacks.
# b) The suit of cards in the stack, from 'A' to 'D'.
# c) The number of cards in the stack, from 0 to max_cards
# d) An "extra" value, from 0 to max_cards, whose purpose will be
#    revealed only in Part B of the assignment.  You should
#    ignore it while completing Part A.
#
# There will be up to num_stacks specifications, but sometimes fewer
# stacks will be described, so your code must work for any number
# of stack specifications.
#
def random_game(print_game = True):

    # Percent chance of the extra value being non-zero
    extra_probability = 20

    # Generate all the stack and suit names playable
    game_stacks = ['Stack ' + str(stack_num+1)
                   for stack_num in range(num_stacks)]
    game_suits = ['Suit ' + chr(ord('A')+suit_num)
                  for suit_num in range(4)]

    # Create a list of stack specifications
    game = []

    # Randomly order the stacks
    shuffle(game_stacks)

    # Create the individual stack specifications 
    for stack in game_stacks:
        # Choose the suit and number of cards
        suit = choice(game_suits)
        num_cards = randint(0, max_cards)
        # Choose the extra value
        if num_cards > 0 and randint(1, 100) <= extra_probability: 
            option = randint(1,num_cards)
        else:
            option = 0
        # Add the stack to the game, but if the number of cards
        # is zero we will usually choose to omit it entirely
        if num_cards != 0 or randint(1, 4) == 4:
            game.append([stack, suit, num_cards, option])
        
    # Optionally print the result to the shell window
    if print_game:
        print('\nCards to draw ' +
              '(stack, suit, no. cards, option):\n\n',
              str(game).replace('],', '],\n '))
    
    # Return the result to the student's deal_cards function
    return game

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "deal_cards" function.
#
#create a function to draw the outline of the cards
def outline():
    seth(0)
    forward(75)
    left(90)
    pensize(1)
    pendown()
    pencolor('black')
    fillcolor('beige')
    begin_fill()
    #for loop to draw sides simpler
    for sides in range (2):
        forward(100)
        left(90)
        forward(150)
        left(90)
        forward(100)
    end_fill()    
    penup()
    left(90)
    forward(75)

#define function to draw suit A (Captain America)
def card_Captain_America():
    #draw card outline
    outline()
    #draw outer ring
    color('red')
    dot(150)
    #draw next ring
    color('white')
    dot(125)
    #draw next ring
    color('red')
    dot(100)
    #draw inner circle
    color('blue')
    dot(75)
    #draw the star
    seth(90)
    color('white')
    forward(75/2)
    seth(-72)
    pendown()
    begin_fill()
    for star in range(5):
        forward(72)
        right(144)
    end_fill()
    penup()
    #return to centre
    seth(-90)
    forward(75/2)

#define function to draw suit B (Thor)
def card_Thor():
    #draw outline
    outline()
    #draw the head of the hammer
    seth(90)
    forward(20)
    fillcolor('grey')
    pencolor('black')
    left(90)
    pendown()
    begin_fill()
    forward(50)
    right(45)
    forward(4)
    right(45)
    forward(50)
    right(45)
    forward(4)
    right (45)
    forward(100)
    right(45)
    forward(4)
    right(45)
    forward(50)
    right(45)
    forward(4)
    right(45)
    forward(50)
    end_fill()
    penup()
    #draw the notch on top
    seth(90)
    forward(56)
    left(90)
    forward(20)
    right(90)
    pendown()
    begin_fill()
    forward(3)
    right(90)
    forward(40)
    right(90)
    forward(3)
    end_fill()
    penup()
    right(90)
    forward(20)
    seth(-90)
    forward(56)
    #draw the handle of the hammer
    pensize(15)
    color('brown')
    pendown()
    #draw nob at end of handle
    forward(80)
    color('grey')
    dot(20)
    #return to centre
    penup()
    seth(90)
    forward(60)

#define function to draw suit C (Deadpool)
def card_Deadpool():
    #draw outline
    outline()
    #draw outer ring
    color('red')
    dot(150)
    #fill the rest of the circle black
    color('black')
    dot(115)
    #draw line down the center of the circle
    seth(90)
    forward(65)
    color('red')
    pensize(15)
    seth(-90)
    pendown()
    forward(130)
    penup()
    seth(90)
    forward(80)
    seth(180)
    forward(50)
    #draw left eye
    color('white')
    pensize(1)
    pendown()
    begin_fill()
    seth(240)
    circle(20,180)
    left(90)
    forward(40)
    end_fill()
    penup()
    seth(0)
    forward(100)
    #draw right eye
    seth(-240)
    pendown()
    begin_fill()
    circle(20,-180)
    left(90)
    forward(40)
    end_fill()
    penup()
    #return to centre
    seth(180)
    forward(50)
    seth(-90)
    forward(15)

#define function to draw suit D (Professor X)
def card_Professor_X():
    #draw outline
    outline()
    #draw outer grey ring
    color('grey')
    dot(150)
    #draw centre black circle
    color('black')
    dot(120)
    seth(90)
    forward(60)
    color('grey')
    seth(180)
    circle(60, 45)
    left(90)
    #draw top left line of X
    pendown()
    pensize(20)
    forward(120)
    penup()
    seth(45)
    circle(60,90)
    left(90)
    #draw top right line of X
    pendown()
    forward(120)
    penup()
    #return to centre
    backward(60)

#define function to draw the Joker card (Thanos)
def card_Thanos():
    #draw the outline of the card
    outline()
    #draw the outline of the infinity gauntlet
    penup()
    seth(-90)
    forward(70)
    pencolor('black')
    fillcolor('gold')
    begin_fill()
    left(90)
    pendown()
    forward(40)
    left(100)
    forward(90)
    seth(90)
    forward(30)
    #draws the knuckles of the infinity gauntlet
    for knuckles in range (4):
        circle(6.1,180)
        seth(90)
    seth(-90)
    forward(30)
    seth(-100)
    forward(90)
    seth(0)
    forward(40)
    end_fill()
    penup()
    seth(90)
    forward(110)
    seth(180)
    forward(18.3)
    #draw the soul stone
    color('orange')
    seth(0)
    dot(10)
    forward(12.2)
    #draw the reality stone
    color('red')
    dot(10)
    forward(12.2)
    #draw the space stone
    color('blue')
    dot(10)
    forward(12.2)
    #draw the power stone
    color('purple')
    dot(10)
    seth(180)
    #draw the mind stone
    color('yellow')
    forward(18.3)
    seth(-90)
    forward(20)
    dot(15)
    #return to the center
    forward(20)

#define constants for stack location
location = [[-449,275],[-270,275],[-91,275], [88,275],[267,275],[446,275]]
card_values = ['K','Q','J','10', '9','8','7','6','5','4','3','2','A']

# Draw the card stacks as per the provided game specification

def number_cards (draw):
    #go to the top left coner of the card
    seth(90)
    forward(80)
    left(90)
    forward(70)
    #write the corisponding number from the list of card_values in the colour black
    color('black')
    write(card_values[draw])
    #go to the bottom right coner of the card
    left(180)
    forward(70)
    right(90)
    forward(80)
    forward(90)
    left(90)
    forward(60)
    #write the number of the card
    write(card_values[draw])
    left(180)
    forward(60)
    right(90)
    forward(90)

#define a function to draw cards
def deal_cards(input_details):
    #find stack to add it to
    for stack in input_details:
        #to see if the card will go in stack one 
        if stack[0] == 'Stack 1':
            #go to the first location in the locations list
            goto(location[0])
            #does the second value in the details list match suit A
            if stack[1] == 'Suit A':
                #decide if there is a joker in the stack
                if stack[3] == 0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                #does the second value in the details list match suit B
            elif stack[1] == 'Suit B':
                if stack[3]==0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Thor card
                        card_Thor()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
            #does the second value in the details list match suit C
            elif stack[1] == 'Suit C':
                if stack[3]==0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Deadpool card
                        card_Deadpool()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
            #does the second value in the details list match suit D
            elif stack[1] == 'Suit D':
                if stack[3]==0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Professor X card
                        card_Professor_X()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
        #to see if the card will go in stack two
        elif stack[0] == 'Stack 2':
            #go to the second location in the locations list
            goto(location[1])
            #does the second value in the details list match suit A
            if stack[1] == 'Suit A':
                #decide if there is a joker in the stack
                if stack[3] == 0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                #does the second value in the details list match suit B
            elif stack[1] == 'Suit B':
                if stack[3]==0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Thor card
                        card_Thor()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
            #does the second value in the details list match suit C
            elif stack[1] == 'Suit C':
                if stack[3]==0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Deadpool card
                        card_Deadpool()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
            #does the second value in the details list match suit D
            elif stack[1] == 'Suit D':
                if stack[3]==0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Professor X card
                        card_Professor_X()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
        #to see if the card will go in stack three
        elif stack[0] == 'Stack 3':
            goto(location[2])
            #does the second value in the details list match suit A
            if stack[1] == 'Suit A':
                #decide if there is a joker in the stack
                if stack[3] == 0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                #does the second value in the details list match suit B
            elif stack[1] == 'Suit B':
                if stack[3]==0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Thor card
                        card_Thor()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
            #does the second value in the details list match suit C
            elif stack[1] == 'Suit C':
                if stack[3]==0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Deadpool card
                        card_Deadpool()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
            #does the second value in the details list match suit D
            elif stack[1] == 'Suit D':
                if stack[3]==0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Professor X card
                        card_Professor_X()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
        #to see if the card will go in stack four
        elif stack[0] == 'Stack 4':
            #go to the fourth location in the locations list
            goto(location[3])
            #does the second value in the details list match suit A
            if stack[1] == 'Suit A':
                #decide if there is a joker in the stack
                if stack[3] == 0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                #does the second value in the details list match suit B
            elif stack[1] == 'Suit B':
                if stack[3]==0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Thor card
                        card_Thor()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
            #does the second value in the details list match suit C
            elif stack[1] == 'Suit C':
                if stack[3]==0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Deadpool card
                        card_Deadpool()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
            #does the second value in the details list match suit D
            elif stack[1] == 'Suit D':
                if stack[3]==0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Professor X card
                        card_Professor_X()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
        #to see if the card will go in stack five
        elif stack[0] == 'Stack 5':
            #go to the fifth location in the locations list
            goto(location[4])
            #does the second value in the details list match suit A
            if stack[1] == 'Suit A':
                #decide if there is a joker in the stack
                if stack[3] == 0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                #does the second value in the details list match suit B
            elif stack[1] == 'Suit B':
                if stack[3]==0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Thor card
                        card_Thor()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
            #does the second value in the details list match suit C
            elif stack[1] == 'Suit C':
                if stack[3]==0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Deadpool card
                        card_Deadpool()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
            #does the second value in the details list match suit D
            elif stack[1] == 'Suit D':
                if stack[3]==0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Professor X card
                        card_Professor_X()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
        #to see if the card will go in stack six
        elif stack[0] == 'Stack 6':
            #go to the sixth location in the locations list
            goto(location[5])
            #does the second value in the details list match suit A
            if stack[1] == 'Suit A':
                #decide if there is a joker in the stack
                if stack[3] == 0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                #does the second value in the details list match suit B
            elif stack[1] == 'Suit B':
                if stack[3]==0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Thor card
                        card_Thor()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
            #does the second value in the details list match suit C
            elif stack[1] == 'Suit C':
                if stack[3]==0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Deadpool card
                        card_Deadpool()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
            #does the second value in the details list match suit D
            elif stack[1] == 'Suit D':
                if stack[3]==0:
                    #repeat the segment the number of times in the third value of the input details
                    for draw in range(stack[2]):
                        #draw the Professor X card
                        card_Professor_X()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                else:
                    #repeat the card up until the joker must be drawn
                    for draw in range(stack[3]-1):
                        #draw the Captain America card
                        card_Captain_America()
                        #draw the number on the card
                        number_cards(draw)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
                    #draw the Thanos/joker card
                    card_Thanos()
                     #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                    seth(-90)
                    forward(60)
                    for draw in range(stack[2]-stack[3]):
                        card_Captain_America()
                        #draw the number on the card
                        number_cards((stack[3]+draw)-1)
                        #go down 60 pixels to draw the next card to ensure all cards are evenly overlaped
                        seth(-90)
                        forward(60)
    

#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing the card game.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the coordinates and stack locations
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your cards' theme
title("Lachlan Gilbert MARVEL Patience (Captain America, Thor, Deadpool, Professor X and Thanos)")

### Call the student's function to draw the game
### ***** While developing your program you can call the deal_cards
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_game()" as the
### ***** argument to the deal_cards function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_game function.
#deal_cards(fixed_game_0) # <-- used for code development only, not marking
#deal_cards(full_game) # <-- used for code development only, not marking
deal_cards(random_game()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#

