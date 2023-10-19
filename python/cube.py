import turtle

# Create a Turtle object
t = turtle.Turtle()
t.speed(0)  # Set the drawing speed to the fastest

# Set colors
t.fillcolor("#306998")  # Python blue
t.pensize(3)
t.pencolor("#306998")

# Draw the snake's head
t.begin_fill()
t.circle(100, 90)  # Draw a quarter-circle
t.circle(100, 90)
t.end_fill()

# Draw the snake's eye
t.fillcolor("#FFD43B")  # Yellow
t.penup()
t.goto(20, 120)
t.pendown()
t.begin_fill()
t.circle(15)
t.end_fill()

# Hide the turtle
t.hideturtle()

# Close the turtle graphics window on click
turtle.exitonclick()
