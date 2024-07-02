#in this we will learn about if statement and if statement executes if the condition ini it is true
age=int(input("What is your age?:"))
if age==100:
    print("You are a century old!")
elif age>=18:
    print("you are an adult!")
elif age<=0:
    print("You havent been born yet!") 
else:
    print("You are a child")   
