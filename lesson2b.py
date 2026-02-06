#Pytho tuple
#It is an immutable type of a list(It cannot change)
#To come up with a tuple we use parenthesis()


counties = ("Nairobi", "Mombasa", "Nakuru", "Eldoret", "Kajiado", "Kisii")
print(counties)
print(type(counties))

#Slicing tuple
print(counties[3:1])

#Accessing the items of a tuple by use of the indexes
print(counties[5])

#Note -Below will generate an error
counties.append("Machakos")
print(counties)