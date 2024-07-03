# *args are used to accept multiple positional arrguments as a tuple in the function 

def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum 

add(1,2,3,4,5)   