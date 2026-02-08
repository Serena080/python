# Create a python program that determines whether a number entered is odd or even

# number = int(input("Enter your number here ,"))

# if number % 2 ==0 :
#      print("The number is even")

# else:
#      print("The number is odd")     


#Create a python program that is able to determine whether a person can donate blood based on the age and weight of a person...If the weight is greater than 50kgs the age above 18 yrs then the person can donate,else not possible

age = int(input("Enter age:"))

weight = float(input("Enter the weight of donor:"))

if age >= 18 and weight > 50:
  print("Can donate")
else:
  print("Cannot donate")