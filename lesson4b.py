#Loops->  
#Sometimes we may need to do a piece of work a number of times repeatedly, such cases we may use loops
#A loop is a control structre that allows us to execute a block of code repeatedly until a certain codition is met.

#Tere are two types of loops i.e the follow and the while loop.
#    Below is the syntax of a for loop in python

"""
For variable i range (n)
#The block of code to be executed
"""

print("Hello Moses")
print("Hello Moses")
print("Hello Moses")
print("Hello Moses")


for greeting in range(10):
     print("Hello Susan", greeting)


print("===================================================================")    

for number in range(10,20) :
    print(number)


print("===================================================================")    

#Find the even numbers in the range of 50 to 71

for number in range(50, 71, 2):
     print(number)


print("===================================================================")    
#Creatte a python program that prints the odd numbers from 100 t0 150

for number in range(101, 150, 2):
     print(number)



print("===================================================================")    
#Create a program that reads the multiples of 3 from 201 to 150
for number in range(201, 148, -3):
     print(number)

print("===================================================================")
#  create a python program that   prints leap years between 200 and 2024

for number in range(2000, 2025, 4):
     print(number)


#Reasearch how you create a program that tests whether a year was a leap year and its validity