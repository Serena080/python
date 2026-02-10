#Functions with parameters
#PARAMETERS ARE VALUES THAT GET PASSED AS ARGUEMENTS GIVEN TO A FUNCTION INSIDE OFA PARENTHESIS



def greeting(name):
     print(f"{name},how are you?Hope everything is fine.")

greeting("Serena")   
greeting("Gavin")  

print("====================================================================")

def message(names):
     print(f"Hello,{names}.We shall be having a genral meeting on date____________.Please avail yourself.")

message("Hope") 
message("Ivy")   
message("Brandon") 


print("====================================================================")
#Create function that accepts parameters to add two numbers

def addition(x, y):
     sum = x + y
     print("The sum of the numbers is: ", sum)
addition(30, 40)
addition(45, 50)

 


