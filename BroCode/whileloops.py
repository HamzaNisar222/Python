# while loop is a block of code that will run as long as its condition remains true
name=""
while len(name) == 0:
    name = input("What is you name?:")
print("Hello " + name)

name=None
while not(name):
    name = input("What is you name?:")
print("Hello " + name)
