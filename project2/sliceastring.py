# returniong a portion of a string
# b = "Hello, World!"
# print(b[1:5]) # a:b a is staring and b is ending indexes for 
# slicing from statrt a will be nul

# # Using reverse indexes to print the last character of the string
# b = "Hello, World!"
# print(b[-3:-1]) 

# CONVERT STRINGS TO UPPER CASE
# a = "Hello, World!"
# print(a.upper())
# for lower
# a = "Hello, World!"
# print(a.lower())
# for removing white spaces
# a = " Hello, World! "
# print(a.strip()) 

# Replace in strings
# a = "Hello, World!"
# print(a.replace("He", "Jimmy"))

# Split in strings on instance of seprator 
# a = "Hello, World!"
# print(a.split(","))

# # CONCATINATION OF A STRING
# a = "Hello"
# b = "World"
# c = a + b
# print(c)

# # With a space between 
# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)


# FORMATING STRINGS AND CONCATINATING VARIABLES INT AND FLOAT WITH IT
# age = 36
# txt = f"My name is John, I am {age}"
# print(txt)
# DISPLAY PRICE WITH 2 DECIMAL PLACES
# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)
# perform maths operation in string
# txt = f"The price is {20 * 59} dollars"
# print(txt)


# Using escape characters to insert illegal characters in strings
# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)

# for inserting illegal single qoutes in a string
# txt = 'It\'s alright.'
# print(txt) 

# for insering a back slash in a string
# txt = "This will insert one \\ (backslash)."
# print(txt) 

# for new line 
# txt = "Hello\nWorld!"
# print(txt)

# txt = "Hello\r World!h"
# print(txt) 
#Example of \r
# import time
# # Loop to simulate a countdown
# for i in range(10, 0, -1):
#     # Print the countdown on the same line using \r
#     print(f"Countdown: {i}", end='\r')
#     # Wait for 1 second before the next iteration
#     time.sleep(1)
# # Print a message after the countdown is complete
# print("\nBlast off!")

# # Example of \t
# txt = "Hello\tWorld!"
# print(txt) 

# #EXAMPLE OF \b
#This example erases one character (backspace):
# txt = "Hello \b\bWorld!"
# print(txt) 

#A backslash followed by three integers will result in a octal value:
# txt = "\110"
# print(txt) 


#A backslash followed by an 'x' and a hex number represents a hex value:
# txt = "\x48\x65\x6c\x6c\x6f"
# print(txt) 



