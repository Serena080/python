#Dictionary data type- It is a data type that stores data in terms of key-value pair
# It is introduced by curly braces {}
# The values stored inside a dictionary can be of any data type

#To access the values in a dictionary we use the keys

phonebook = {
     "Benson" : "254767983789",
     "Mary" : "2547367890",
     "Stephen" : "2543789890"
}

#Show the entire phonebook
print(phonebook)
print(type(phonebook))

#Printing out  Benson's number
print(phonebook["Benson"])

print("===============================================")
player = {
     "name" : "Messi",
     "age" : 41,
     "teams" : ["PSG", "Barcelona" , "Argentina"]

}
print("The second team played was: ",(player["teams"][1]))

