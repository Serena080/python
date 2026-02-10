#Python functions
#- They are a block of code/ statements hat performs a given task.They can be reused throughout the program to perform tasks.
#Function s are defined using (def) keyword
#We have two main types: 
# 1.Inbuilt fuctions- they come peinstalled with the interpreter i.e print(), pop(),range(),append()
#2. User defined functions- they are created by a programmer to solve a given task
# To define a fuction you need to give it a name followed by parenthesis
# For the functions, it is usually indented and to invoke a function we use the function name.

def greetings():
     print("Hello, how are you?")
#below we call the function by use of it's name
greetings()  


print("=============================================================================")
#Addition function

def addition():
     num1 = 40
     num2 = 50
     sum = num1 + num2
     print("The sum of the numbers is: ", sum)

addition()  

print("=============================================================================")
# create a function that  is able to multiply three values

def product():
     num3 = 15
     num4 = 4
     num5 = 7
     product = num3 * num4 * num5
     print("The product of the three numbers is: ", product)

product()   

print("=============================================================================")
#Below is a division function

def division():
     number1 = int(input("Enter the first number:"))
     number2 = int(input("Enter the second number:"))
     quotient = number1 / number2
     print("The answer is: ", quotient)

division()

print("=====================")
for function in range(3):
     division()

