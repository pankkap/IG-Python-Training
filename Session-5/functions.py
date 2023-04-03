# There are two types of  Function
# 1. System defined Function
# eg. print(), len(), list()

# 2. User defined Functions

# 1. Function defination: We need to defined the function, what task function eed to perform
# 2. Function Call: To execute the function


# FUNCTION DEF
# def funName():
#     statement-1
#     statement-2
#     statement-3

# funName()   # FUNCTION CALL


# def add():
#     x = 10
#     y = 20
#     print("Sum of Numbers :",x+y)

# add()
# add()
# add()

# Function that takes input

# def sub(x,y):
#     z = x - y
#     print("Subtraction :",z)

# x =int( input("Enter number"))
# y =int( input("Enter number"))
# sub(x,y)
# sub(100,95)
# sub(50,9)


# Function that return the result back to called function
# def multiply(x,y):
#     z = x * y
#     return z

# r = float(multiply(5,4))
# print(r*r)

# Default Argument
# def sayHello(fname=" ",lname=" "):
#     print("Hello "+fname+" "+lname)

# sayHello("Sachin")
# sayHello("Sachin", "Yadav")
# sayHello()


# def sayHi(*x):
    
#     for i in x:
#         print(i)

# sayHi(10,5,15,1,3,4,5,6,7)


# def handleData (x):
#     print(x)
#     pass 

# data = ["sachin", "manish", 1, 2, 4] 
# handleData(data)
# print("hi")

def data(**data):
    print(data["y"])

data(x=123, y = 456)    

