from turtle import Turtle, Screen
import random

is_race_on = False  # gets hold of the start of the race
screen = Screen()
screen.setup(width=500, height=400)  # sets the screen dimensions
colors = ["red", "orange", "yellow", "green", "blue", "purple"]  # colors of our turtles
turtles_list = []  # The list that is going to contain the turtles
y = 100  # starting(reference) y coordinate to help align the turtles
for i in range(6):  # Using for loop to set the properties of the turtles and append the turtles to the turtles_list
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    turtles_list.append(new_turtle)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    y -= 50
# Triggers the popup window to ask the user for the guess
user_guess = screen.textinput(title="Make your guess", prompt="Which turtle will win the race? Enter a color:")
if user_guess in colors:  # checking if the user's input is valid
    is_race_on = True  # start the race

winning_turtle = None  # variable to store the winning turtle
while is_race_on:
    for i in range(6):  # Keep iterating through the turtles_list and move the turtles with random distances
        rand_distance = random.randint(5, 15)
        turtles_list[i].forward(rand_distance)
        if turtles_list[i].xcor() > 230:  # Stop the iteration once a turtle reaches the end of the race
            is_race_on = False
            winning_turtle = turtles_list[i]  # store the winning turtle

if winning_turtle.color()[0] == user_guess.lower():  # check if the user won
    print(f"YOU WIN! The {winning_turtle.color()[0]} turtle is the winner!")
else:
    print(f"YOU LOSE! The {winning_turtle.color()[0]} turtle is the winner!")
screen.exitonclick()

