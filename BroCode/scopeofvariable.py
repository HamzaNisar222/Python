# Scope is the region where a variable is recognised 
# a variable is only present in the region where it is created

name="Hamza Nisar" #global variable available in all the ways 

def display():
    name="Hamza" # local scope (only availabe inside this function)
    print(name)
display()
print(name)    