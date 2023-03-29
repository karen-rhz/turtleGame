# We are building a game that respond to commands on keyboard strokes
# We need use a method called .listen to be able to receive command from the user
from turtle import Turtle, Screen

# Add a turtle
genie = Turtle()
genie.shape("turtle")
genie.color("blue")

# Display the screen
screen = Screen()


# Define what does pressing a key will make the turtle do
def move_forward():
    genie.forward(10)


def turn_left():
    genie.left(15)


def turn_right():
    genie.right(15)


def move_backwards():
    genie.forward(-10)


def end():
    genie.home()
    genie.clear()


# Make the screen accept and listen to commands from the keyboard
screen.listen()


def turtle_commands():
    screen.onkey(move_forward, "w")
    screen.onkey(move_backwards, "s")
    screen.onkey(turn_left, "a")
    screen.onkey(turn_right, "d")
    screen.onkey(end, "c")


turtle_commands()
screen.exitonclick()