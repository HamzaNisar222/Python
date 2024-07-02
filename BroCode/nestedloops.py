#nested loops in the inner loop will finish all its iterations before the outer one finishes its one iteration

rows=int(input("How many rows do you want?:")) #input for rows
columns=int(input("How many columns do you want?:"))#input for columns
symbol=input("What symbol do you want?:")#input for synbol
for i in range(rows):#Loop responsible for rows 
    for j in range(columns):#lopp responsible for columns
        print(symbol,end="")
    print()
    
 
for i in range(rows):#Loop responsible for rows 
 for j in range(i+1):#lopp responsible for columns
        print(symbol,end="")
 print()
           
