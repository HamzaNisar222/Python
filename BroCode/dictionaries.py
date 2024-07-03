# a dictionary is a collection of changeable unordered collection of unique key value pairs Fast as they use hashing and allows us to access the value fast

capitals={
   "USA":"Washington DC",
   "China":"Beiging",
   "India":"New Delhi",
   "Russia":"Moscow"
   
} 

capitals.update({"Germany":"Berlin"})#add a new key value to dic using update
capitals.update({"USA":"Las Vegas"})#updating an existing one 
capitals.pop("Russia")#for removing a key value pair
capitals.clear()

print(capitals["China"])#print the value by key 
print(capitals.get("USA"))#get the value by key safer way
print(capitals.keys())# for printing keys only 
print(capitals.values())#for priniting values only 
print(capitals.items())#for displaying all the dictionary

for x,y in capitals.items():
    print(x,y)