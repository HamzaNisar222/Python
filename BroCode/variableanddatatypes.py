#A bvariable is a reusable cotainer for storing a value
#a variable behaves as it were the value it contains
age=25
print ("You are" , age , "Years old") #giving variable and strings as seprate arrguments
print ("you are "+ str(age)+ " Years old") # converting var to string using str
print(f"you are {age} Years old")# using f string most popular and common way 

#INTEGERS
age=25
quantity=10
players=8

print(f"you are {age} years old Hamza")
print(f"there are {players} players online")
print(f"You want to buy {quantity} items")


#FLOATS
gpa=2.78
distance=2.9
price=10.99

print(f"your gpa is {gpa}")
print(f"you ran {distance} Kilometers")
print(f"price of this bracelet is {price}")

#STRINGS
name="Hamza"
food="Pizza"
email="Hamza@example.com"

print("Hello " + name)
print(f"You like {food}")
print(f"You email is {email}")

#BOOLEANS
online=True
for_sale=False
running=False

print(f"Are you Online?:{online}")
print(f"is this item for sale?:{for_sale}")
print(f"Is the game running?:{running}")

if running:
    print("Game is running")
else:
    print("Game is over")

#ASSIGNING VARIABLES
a=1
b=2
c=3
a,b,c=1,2,3
a=b=c=1