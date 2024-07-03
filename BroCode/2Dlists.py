# 2D list is a list of lists 
drinks=["coke","pepsi","fanta","sprite"]
dinner=["Rosh","Biryani","Paye","Nihari"]
desert=["Kheer","Firni","Cake"]

food=[drinks,dinner,desert]

drinks.insert(4,"Seven up")
print(food)
print(food[0])
print(food[0][0])

for i in range(len(food)):
    for j in range(len(food[i])):
        print(food[i][j])
    print()