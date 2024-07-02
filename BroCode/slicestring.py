#slicing is making a substring by extracting elements from another string
#   indexing[] or slice()
#   [start:stop:step]
name="Hamza Nisar"

first_name=name[:5]#if we leave start empty its starts from 0 
last_name=name[6:]#if we leave last stop empty it goes to end starts from in dex 5 and goes to end 
funcky_name=name[3:8:2]#if we slice with step 1 it will retrun all the characters other wise if 2 then the first and evry second
reversed=name[::-1]
print(first_name)
print(last_name)
print(funcky_name)
print(reversed)
#USING SLICE FUNCTIONS 
website="https://www.google.com/"
website1="https://www.wikipedia.org/"
slice=slice(12,-5)#slicing through slice function 1st is starting index 2nd is stoping index
print(website[slice])
print(website1[slice])
