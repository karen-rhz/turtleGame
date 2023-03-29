import turtle
from turtle import Turtle, Screen
import random

colors = ["lime green", "royal blue", "crimson", "gold", "dark orchid",
          "dark orange"]

screen = Screen()
screen.screensize(canvwidth=50, canvheight=300)


# green_turtle = Turtle("turtle")
# green_turtle.color("lime green")
# green_turtle.goto(x=-300, y=-200)

# user_choice = turtle.textinput(title="Pick your winner",
#                                prompt="Choose your turtle color: green / blue / red / yellow / purple / orange \n ")


# blue_turtle.goto(-300, -150)
#
# red_turtle.goto(-300, -100)
#
# yellow_turtle.goto(-300, -50)
#
# purple_turtle.goto(-300, 0)
#
# orange_turtle.goto(-300, 50)

# def turtles_in_race(racer_color, position_x, position_y):
#     racing_turtle = Turtle("turtle")
#     racing_turtle.penup()
#     racer_color = racing_turtle.color(random.choice(colors))
#     return turtles_in_race()


for color in colors:
    racer_turtle = Turtle("turtle")
    racer_turtle.color(color)
    racer_turtle.goto(x=(-300 * 10), y=(-200 * 10))

screen.exitonclick()