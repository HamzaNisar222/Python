# keyword arguments are arguments preceeded by an identifier when we passs them to the function 
# the order of the arrguments does not matter unlike positional arguments python knows the names
# of the arrguments that our function recieves
def hello(first, middle , last):
    print("hello "+ first + " " + middle + " " + last)
    
hello(last="Ahmed",first="Hamza",middle="Nisar")