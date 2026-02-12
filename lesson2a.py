#Pytho Lists
# A list in python is a collection of items ordered in a certain way
# A list is introduced by use of the squared brackets.
#The items of a list are stored inside of indexes: 
#Note that in programming we start counting from index zero[0]
#A list is mutable i.e the contnts of the list can be changed.


cars =["BMW", "benz", "Hiance", "Prado", "Probox", "Mercedes", "Range", "Mclaren"]
print(cars)
print(type(cars))

#Accessing the items of a list
print(cars[2])
print("The cars on index four: ",(cars[4]))

#List slicing
#-This is creating a list from given  bigger list

print(cars[4:])

#Printing from index 0 to 3
print(cars[:3])

#Printing fronm hiance to probox
print(cars[2:5])


#List Mutability
#We use the function append to add an item at the end of a list
cars.append("Lexus")
print(cars)

cars.append("subaru")
print(cars)

#We use a pop function to remove an item of the list
cars.pop()
print(cars)

#We can use an index to add items on a list
cars[5] = "Pajero"
print(cars)


# We can use the sort function to soort out the items in alphabetical order
cars.sort(reverse=True)
print(cars)

cars.pop(2)
print(cars)