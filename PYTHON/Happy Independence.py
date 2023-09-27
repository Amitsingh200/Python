import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Happy Independence Day!")
screen.bgcolor("#FFFFFF")

# Create a turtle object
flag = turtle.Turtle()
flag.speed(3)
flag.penup()

# Move turtle to starting position
flag.goto(-240, 180)
flag.pendown()

# Draw saffron color
flag.color("#FF9933")
flag.begin_fill()
flag.forward(480)
flag.right(90)
flag.forward(80)
flag.right(90)
flag.forward(480)
flag.end_fill()

# Draw white color
flag.color("#FFFFFF")
flag.begin_fill()
flag.left(90)
flag.forward(80)
flag.left(90)
flag.forward(480)
flag.left(90)
flag.forward(80)
flag.left(90)
flag.forward(480)
flag.end_fill()

# Draw green color
flag.color("#138808")
flag.begin_fill()
flag.left(90)
flag.forward(80)
flag.left(90)
flag.forward(480)
flag.left(90)
flag.forward(80)
flag.left(90)
flag.forward(480)
flag.end_fill()

# Move turtle to write the message
flag.penup()
flag.goto(-200, 0)
flag.pendown()
flag.color("#000000")
flag.write("Happy Independence Day!", align="center", font=("Arial", 24, "bold"))

# Hide the turtle
flag.hideturtle()

# Exit on click
turtle.exitonclick()