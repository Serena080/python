#Python Modules
#A python module is a file that contains python definitions,python statements or functions.


def add():
     num1 = 35
     num2 = 49
     sum = num1 + num2
     print("The answer is: ", sum)


def subtract():
     x = 36
     y = 26
     difference = x - y
     print("The difference is: ", difference)

#    Thes functions defined above on this particular file can be called into another file


def rectangleArea():
     length = int(input("Enter the length:"))
     width = int(input("Enter the width:"))

     area = length * width
     print("The area of the rectangle is: ", area)
