# # 1 Capitalize() 
# #Converts first letter to uppercase and rest to lowercase
# txt="hello, and welcome to my world."
# x=txt.capitalize()
# print(x)


# # 2 casefold()
# # Converts string into lower case

# txt="Hello, AND Welcome To My World!"
# x=txt.casefold()
# print(x)

# # 3 center()	
# # Returns a centered string
# txt="banana"
# x=txt.center(20)
# print(x)
# text = "Python"
# centered_text = text.center(20, '*')
# print(centered_text)

# # 4 count()
# # Returns the number of times a specified value occurs in a string
# txt = "I love apples, apple are my favorite fruit"
# x = txt.count("apples")
# print(x)

# 5 encode() & decode()
# Returns an encoded version of the string
# txt = "My name is Ståle"
# x = txt.encode()
# y=x.decode()
# print(x)
# print(y)

# endswith()
# Returns true if the string ends with the specified value
# txt = "Hello, welcome to my world."
# x = txt.endswith(".")
# print(x)

# expandtabs()
# Sets the tab size of the string
# txt = "H\te\tl\tl\to"
# x =  txt.expandtabs(2)
# print(x)

# find()
# Searches the string for a specified value and returns the 
# position of where it was found
# txt = "Hello, welcome to my world."
# x = txt.find("welcome")
# print(x)

# # format()
# # Formats specified values in a string
# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))

# format_map()
# Formats specified values in a string
# my_dict = {"name": "John", "country": "Norway"}
# txt = "My name is {name} and I am from {country}"
# print(txt.format_map(my_dict))

# index()	
# Searches the string for a specified value and returns the 
# position of where it was found
# txt = "Hello, welcome to my world."
# x = txt.index("welcome")
# print(x)

# # isalnum()	
# # Returns True if all characters in the string are alphanumeric
# txt = "COMPANY"
# x = txt.isalnum() # check if alpha numeric
# y = txt.isalpha() # check if alphabet
# z = txt.isdigit() # check if digit
# a = txt.islower() # check if lower case
# b = txt.isupper() # check if upper case
# c = txt.isspace() # check if space
# d = txt.istitle() # check if title
# print(x)
# print(y)
# print(z)
# print(a)
# print(b)
# print(c)
# print(d)

# # join()
# # Joins the elements of an iterable to the end of the string
# myTuple = ("John", "Peter", "Vicky")
# x = " ".join(myTuple)
# print(x)

# ljust()
# Returns a left justified version of the string
# txt = "banana"
# x = txt.ljust(20,"*")
# y = txt.rjust(20,"*")
# print(x, "is my favorite fruit.")
# print(y, "is my favorite fruit.")

