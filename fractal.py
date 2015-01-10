import turtle
import random

# draws a fractal tree
def tree(size, origsize):
    if size > 0:
        turtle.forward(size)
        r = random.randint(12, 30) if origsize < size else 24
        l = random.randint(12, 30) if origsize < size else 24
        turtle.right(r)
        tree(size - random.randint(7, 10), origsize)
        turtle.left(r + l)
        tree(size - random.randint(7, 10), origsize)
        turtle.right(l)
        turtle.backward(size)

# draws one side of the koch snowflake
def koch(size, order):
    x = size / 3.0
    if order > 0:
        koch(x, order - 1)
        turtle.left(60)
        koch(x, order - 1)
        turtle.right(120)
        koch(x, order - 1)
        turtle.left(60)
        koch(x, order - 1)
    else:
        turtle.forward(size)

# draw tree
turtle.speed(0)
turtle.penup()
turtle.ht()
turtle.left(90)
turtle.backward(140)
turtle.pendown()

tree(64, 64)

# draw snowflake
turtle.penup()
turtle.forward(30)
turtle.left(45)
turtle.forward(382)
turtle.right(135)
turtle.pendown()

for i in range(3):
    koch(540, 5)
    turtle.right(120)

turtle.exitonclick()