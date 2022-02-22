from turtle import *
import turtle as t
import random


height = 2000
width = 2000
screen = Screen()
screen.screensize(width, height)


t.speed(10)
t.penup()
t.goto(400, -400)
t.pendown()
screen = t.Screen()
screen.bgcolor('Grey')
t.color('Teal')

# This list will contain the coordinates of the three points
li = []

# Creating the equilateral triangle
for i in range(3):
    t.dot(10)
    li.append(t.pos())   # Adding the points coordinates to the list
    t.right(240)
    t.penup()
    t.forward(900)
    t.pendown()



while True:
    # Choosing a random point on triangle
    spot = random.choice(li)
    # Find the angle need to make to point to next point
    ang = t.towards(spot)
    # Find the distance between the two points
    dis = t.distance(spot)

    # Changing the heading towards the next point
    t.setheading(ang)
    t.penup()
    # Turtle goes half the distance between the two points
    t.forward(0.5*dis)
    t.pendown()
    t.dot(10)


t.done()
