#Nested IF stetements
#Nested If statement- an if statement contained inside another if statement 


age = 20
weight = 60
bloodtype = "A"

if age > 15 :
     if weight > 50 :
          print("You can donate blood")

          if bloodtype == "A" :
             print("You can donate to blood types A and AB")

     else:
          print("You cannot donate blood because of weight")   
else:
     print("You cannot donate blood because of age")           