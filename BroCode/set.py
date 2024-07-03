# Set is a collection which is unorder un indexed and dont allow duplicate values

utensils={"Spoon","Fork","Knife","Butter Knife"}
dishes={"bowl","plate","tray","Knife"}
utensils.add("Napkin") #to ad to a set 
utensils.remove("Knife") #to remove from set
# utensils.clear()#to clear the set all values 
utensils.update(dishes)#add a set to another
dinner_table=utensils.union(dishes)#combining two sets to make a new one
print(dinner_table)
print(utensils.difference(dishes))#find difference of sets
print(dishes.difference(utensils))



for x in utensils:
    print(x)