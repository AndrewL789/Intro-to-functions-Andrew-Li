import turtle
from turtle import *
t = Turtle()


t.shape('turtle')
t.speed(10)
""" 
t.forward(200)
 """
""" def message(input):
    print(input)
message("Hello Class") """

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



""" name = input("what is your name?")
#use F string 
print(f"His name is {name}")
 """

#inputs output strings

# integers numbers

""" a = int('5')
bill = input("How much was the bill?")
print(int(bill) * .15)

 """


""" #float - interger with decimals
bill = 3.14

students = ["Cadee", "Mason", "Andy"]
#lists are a collection of data

print(students[0]) # prints Cadee 
# can refrence each item in a list by their index

# add student
students.append("Alina")

# we can interate or loop troguh a list

for student in students:
    print(student) """

""" #BooLean true or false
x = True
y = False

#evaluations use double ='s 
if x == True:
    print("Hello Rodney")
else:
    print("Goodbye Rodney")
 """
""" 
students = ["Cadee", "Mason", "Andy"]
if "Alina" in students:
    print("Shes here")
else:
    students.append("Alina")
    print("We added Alina") """

""" x = 9
if x <10:
    print("Less")
elif x == 10:
    print("equal")
else:
    print("greater than 10")




 """

""" students = ["Cadee", "Mason", "Andy", "Alina"]
for student in students:
    found = False 
    if student == "Mason":
        print("Found Mason")
    found = True 
 """


""" name = "Cadee"
#print(name[0])
for letter in name:
    print(letter) """