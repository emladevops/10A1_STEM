import turtle

# Create a new Turtle object
t = turtle.Turtle()

# Set the turtle's speed to 0
t.speed(0)

# Set the fill color to black
t.fillcolor("black")

# Start drawing the spiral
t.penup()
t.goto(0, 0)
t.pendown()
t.begin_fill()

# Draw a circle with a radius of 100
t.circle(100)

# Fill in the circle
t.end_fill()

# Pick up the pen and move to the center of the spiral
t.penup()
t.goto(0, 0)
t.pendown()

# Draw a white circle with a radius of 50
t.fillcolor("white")
t.begin_fill()
t.circle(50)
t.end_fill()

# Pick up the pen and move to the outside of the spiral
t.penup()
t.goto(100, 0)
t.pendown()

# Draw a black line to connect the two circles
t.fillcolor("black")
t.begin_fill()
t.lineto(0, 50)
t.end_fill()

# Keep the window open until it is closed manually
turtle.done()
