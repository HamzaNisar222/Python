# Types of number in pyhton
# There are three numeric types in Python:

# int
# float
# complex

# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# print(type(x))
# print(type(y))
# print(type(z))

# # TYPE INTEGER INT
# stores whole numbers that range from -2,147,483,647 to 
# 2,147,483,647 for 9 or 10 digits of precision. 
# x=12312348347634683792839
# y=2
# z=-3443453546345345
# print(type(x))
# print(type(y))
# print(type(z))

# # FLOAT DATA TYPE
# x = 1.10
# y = 1.0
# z = -35.59

# print(type(x))
# print(type(y))
# print(type(z))

# # E e is scientific number with "e" as the power of 10 is also float
# x = 35e3
# y = 12E4
# z = -87.7e100

# print(type(x))
# print(type(y))
# print(type(z))

# # COMPLEX DATA TYPE
# x = 3+5j
# y = 5j
# z = -5j

# print(type(x))
# print(type(y))
# print(type(z))

# # WE CAN CONVERT FROM ONE TYPE TO ANOTHER WITH THE INT(), FLOAT() AND COMPLEX() METHODS
# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# #convert from int to float:
# a = float(x)

# #convert from float to int:
# b = int(y)

# #convert from int to complex:
# c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))

# # GENERATING A RANDOM NUMBER 
# import random

# # between 1,1000 but not including 1000
# print(random.randrange(1, 1000))
# # between 1,10 but including 10
# print(random.randint(1,10))

# # CASTING
# x="3.14"
# y=float(x)
# print(y)