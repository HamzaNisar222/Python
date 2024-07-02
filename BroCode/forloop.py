#For loop is ude to execute its block of code for a limited time of iterations
# while = unlimited
# while = limited
import time

for i in range(0,10+1):
    print(i)
    
for i in range(50,100+1,2):
    print(i)

for i in "Hamza Nisar":
    print(i)

for second in range(10,0,-1):
    time.sleep(1)
    print(second)
print("Happy New Year")
