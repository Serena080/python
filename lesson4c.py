#A for loop can also be used to iterate through a list, a tuple, string or even a dictionary...

# name = "Serena"

# for letter in name :
#   if letter == "r":  
#      print(name,"This is letter R")
#   else:
#      print(letter)


print("=============================================")  
#Below is a list of counties

counties = ("Nairobi", "Mombasa", "Nakuru", "Eldoret", "Kajiado", "Kisii", "Kisumu", "Meru", "Embu")   
print(counties)

for county in counties:
   print(county)

print("=============================================")  
if county == "Eldoret":
   print("County not found")
else:
   print("County found")   

print("=============================================")  

for county in counties:
   if county == "Kisii":
      print("County is in the list")
      break
   else:
      print("county is not in the list")


print("=============================================")  
#For loop can also be used to iterate in a dictionary

player = {
   "name" : "Mbappe",
   "age" : 25,
   "teams" : ["PSG", "Monaco","France"],
   "nationality" : "French"}


for key in player:
   print(key)

print("=============================================")  

for values in player:
   print(player[values])   

print("=============================================")  
#Loop through the teams he has played for

for teams in player:
   print(player["teams"])

for team in player["teams"]: 
   print(team)