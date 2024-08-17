import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
eye_drawer = turtle.Turtle()
eye_drawer.speed(3)

def draw_circle(color, radius, x, y):
    eye_drawer.penup()
    eye_drawer.goto(x, y)
    eye_drawer.pendown()
    eye_drawer.color(color)
    eye_drawer.begin_fill()
    eye_drawer.circle(radius)
    eye_drawer.end_fill()

# Draw the outer eye (white part)
draw_circle("white", 100, 0, -100)

# Draw the iris (colored part)
draw_circle("blue", 50, 0, -50)

# Draw the pupil (black part)
draw_circle("black", 25, 0, -25)

# Draw the reflection in the eye (white part)
draw_circle("white", 10, -15, -15)

# Hide the turtle and display the window
eye_drawer.hideturtle()
turtle.done()
