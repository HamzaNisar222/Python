#In this lesson we will learn how to take input from user and process it
# NOTE Remember that the user input taken from user is always of a string type and we need to type cast to process it 

name = input("What is your name?:")#getting input from user
age=int(input("what is your age?:"))#casting input ro int 
height=float(input("How tall are you?:"))#casting input to float
print("Your name is " + name)#concatinating string 
print(f"You are {age} years old")#using f string to output
print("You are " + str(height)+ " cm tall")#casting height as a string to concatinate directly

