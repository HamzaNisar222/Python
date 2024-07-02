#Logical operators and,or,not are used to check if two or more conditions are true or not 

temp=int(input("What is the temperature outside?:"))

if not(temp>=0 and temp<=30): #both conditions need to be true
    print("Temperature is bad outside.")
    print("stay inside!")
elif not(temp<0 or temp > 30): #atleast one needs to be true
    print("Temperature is good.")
    print("go outside!")

# NOTE The not operator reverse the false to ture and vise versa