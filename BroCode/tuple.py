# Tuple is similar to the list butt its ordered and unchangeable used group together related data 

student=("Hamza",25,"male")
print(student.count("Hamza"))
print(student.index("male"))
# (name,*age,gender)=student
# print(name)
# print(age)
# print(gender)#UNPACKING

for x in student:
    print(x)

if "Awais" in student:
    print("Awais is here!")
elif "Hamza" in student:
    print("Hamza is here!")
else:
    print("bangan!")