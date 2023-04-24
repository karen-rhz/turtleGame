import turtle
from turtle import Turtle, Screen
import random

# Fixing the screen to make it easier on the eyes
screen = Screen()
screen.bgcolor("black")

# Add title to window
screen.title("Turtle Racing Game")

is_game_running = False

# Using a list for loop is much efficient
# Loop for colours
colors = ["green", "blue", "orange", "yellow", "purple",
          "red", "pink", "brown"]

# Coordinates for the other contestants
# Loop for the y position bc they all start at the same x
y_position = [-200, -150, -100, -50, 0, 50, 100, 150, 200]
# blue_turtle.goto(-300, -150)
# red_turtle.goto(-300, -100)
# yellow_turtle.goto(-300, -50)
# purple_turtle.goto(-300, 0)
# orange_turtle.goto(-300, 50)
all_turtle_racers = []

screen = Screen()
screen.screensize(canvwidth=300, canvheight=300)

# Asking the user for their bet
user_choice = turtle.textinput(title="Pick your winner",
                               prompt="Choose your turtle color: green, blue, orange, yellow, purple, red, pink, brown")


# Each turtle must be configured as such
# green_turtle = Turtle("turtle")
# green_turtle.penup()
# green_turtle.color("lime green")
# green_turtle.goto(x=-300, y=-200)

# Add a winner declaration text instead of displaying message on the console
def screen_message(message, text_y_cor):
    text = Turtle()
    text.hideturtle()
    text.color("white")
    text.penup()
    text.goto(0, text_y_cor)
    text.write(arg=message, align="center", font=('Arial', 15, 'bold'))


for n in range(8):
    turtle_racer = Turtle(shape="turtle")
    turtle_racer.penup()
    turtle_racer.color(colors[n])
    turtle_racer.goto(x=-350, y=y_position[n])
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
        if turtle_in_race.xcor() > 330:
            turtle_winner = turtle_in_race.pencolor()
            winner_message = f"The winner is the {turtle_winner} turtle."
            screen_message(winner_message, 280)
            if user_choice == turtle_winner:
                screen_message("Congratulations! Your turtle won 🎉", 250)
            else:
                screen_message("Your turtle lost the race.", 250)
            is_game_running = False

screen.exitonclick()
