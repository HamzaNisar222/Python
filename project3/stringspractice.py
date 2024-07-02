# Find String length 
def string_length(s):
    return len(s) #length of a string 
print(string_length("Hello How are you?")) # print string

# Reverse a string
def reverse_string(s):
    return s[::-1] 
print(reverse_string("Hello world"))

#Count vowels
def count_vowels(s):
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    count=0
    for char in s:
        if char in vowels:
            count += 1
            return count
print(count_vowels('Hamza Is a Young Man'))
