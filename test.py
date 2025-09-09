import turtle
from turtle import *
t = Turtle()


t.shape('turtle')



def message(input):
    print(input)
    message("Hello Class")
def square(x):
    t.forward(x)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(100)
    t.left(90)
    square(125)

def equal(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
    equal(90)

def right ():
    t.forward(100)
    t.lefft(90)
    t.forward(100)
    t.left(135)
    t.forward(142)
right()


