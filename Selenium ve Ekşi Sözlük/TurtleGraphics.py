import turtle

# Create a turtle screen
window = turtle.Screen()
window.bgcolor("white")

# Create a turtle
star = turtle.Turtle()
 
star.right(75)
star.forward(100)
 
for i in range(4):
    star.right(144)
    star.forward(100)
     
turtle.done()

window.exitonclick()