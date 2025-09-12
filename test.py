import turtle
from turtle import *
t = Turtle()


t.shape('turtle')
t.speed(10)


def square(x,y):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)


def equal(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
equal(90)

def right():
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(135)
    t.forward(142)





def rectangle(x,y):
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(y)
rectangle(125,100)



name = input("what is your name?")
#use F string 
print(f"His name is {name}")


#inputs output strings

# integers numbers

a = int('5')
bill = input("How much was the bill?")
print(int(bill) * .15)