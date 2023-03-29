import turtle
from turtle import Turtle, Screen
import random


is_game_running = False

# Using a list for loop is much efficient
# Loop for colours
colors = ["lime green", "royal blue", "crimson", "gold", "dark orchid",
          "dark orange", "sienna", "hot pink", "dark blue", "rosy brown"]
# Loop for the y position bc they all start at the same x
y_position = [-200, -150, -100, -50, 0, 50, 100, 150, 200]
# blue_turtle.goto(-300, -150)
# red_turtle.goto(-300, -100)
# yellow_turtle.goto(-300, -50)
# purple_turtle.goto(-300, 0)
# orange_turtle.goto(-300, 50)
all_turtle_racers = []

screen = Screen()
screen.screensize(canvwidth=50, canvheight=300)

user_choice = turtle.textinput(title="Pick your winner",
                               prompt="Choose your turtle color: green / blue / red / yellow / purple / orange \n ")

# Each turtle must be configured as such
# green_turtle = Turtle("turtle")
# green_turtle.penup()
# green_turtle.color("lime green")
# green_turtle.goto(x=-300, y=-200)

# Coordinated for the other contestants
# blue_turtle.goto(-300, -150)
# red_turtle.goto(-300, -100)
# yellow_turtle.goto(-300, -50)
# purple_turtle.goto(-300, 0)
# orange_turtle.goto(-300, 50)

for n in range(9):
    turtle_racer = Turtle(shape="turtle")
    turtle_racer.penup()
    turtle_racer.color(colors[n])
    turtle_racer.goto(x=-300, y=y_position[n])
    # Adding each turtle to the race
    all_turtle_racers.append(turtle_racer)


# So that the race doesn't start before the user has made a bet
if user_choice:
    is_game_running = True

while is_game_running:
    for turtle_in_race in all_turtle_racers:
        # We will be letting the turtle go forward bits by bits randomly
        distance = random.randint(0, 10)
        turtle_in_race.forward(distance)
        if turtle_in_race.xcor() == 30:
            turtle_winner = turtle_in_race.pencolor()
            print(f"The winner is the {turtle_winner} turtle.")
            if user_choice == turtle_winner:
                print("You won!")
            else:
                print("Your turtle lost the race.")
            is_game_running = False






screen.exitonclick()