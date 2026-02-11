# On the try and except block:
# You run some codes or statements and if it is successful the try block will get executed otherwise the except block will be executed when there is anticipated error


try:
    number1 = 100

    answer =number1 / 0
    print("The answer is: ", answer)
except  Exception as e :
    print("There is an error: ", e) 



