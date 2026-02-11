#Qn 1: Function Without Parameters
#Create a function that:
#• Takes no parameters
# • Uses arithmetic operators to calculate the area of a rectangle
# • Prints the result

def area():
     length = 40
     width = 30
     area = length * width
     print("The area of the rectangle is: ", area)

area()    


# Qn 2: Function With Parameters
# Create a function that:
# • Accepts two numbers as parameters
# • Returns their sum, difference, product, and division

numeral1 = int(input("Enter the first number:"))
numeral2 = int(input("Enter the second number:"))

#Addition

addition = numeral1 + numeral2
print("The sum of two numbers: ",addition)

#Subtraction

difference = numeral1 - numeral2
print("The difference between two numbers: ",difference )

#multiplication

product = numeral1 * numeral2
print("The products of two numbers: ",product)

#Division

divident = numeral1 / numeral2
print("The divident of two numbers: ",divident)




# Qn 3: Control Statement (if...elif...else)
# Write a function that:
# • Accepts a number (use input function)
# • Checks whether the number is:
# • Positive
# • Negative
# • Zero

num1 = int(input("Enter the number:"))
if num1 == 0:
     print("This is a zero")

elif num1 < 0:
     print("This is a negative number")   

else:
     print("This is a positive number")       




# Qn 4: Loop with Arithmetic
# Write a function that:
# • Accepts a number n
# • Uses a for loop
# • Calculates the sum of numbers from 1 to n








# Qn 5: While Loop
# Write a function that:
# • Accepts a number (Use input() function)
# • Uses a while loop
# • Calculates the square of numbers from 1 up to that number

number1 = int(input("Enter the number:"))
while number1 >= 1:
     exponent = number1 ** 2
     print("The exponent of the number: ", exponent)
     


   


     
     