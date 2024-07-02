# FUNCTION FOR SUM
def myfunc(a, b):
  return a + b


print(myfunc(3, 4))


# FUNCTION FOR EVEN OR ODD
def evenOrOdd(a):
  if a % 2 == 0:
    print(f"The number {a} is even")
  else:
    print(f"The number {a} is odd")


evenOrOdd(10)


# FIND VOWELS IN A STRING
def findVowels(a):
  vowels = ["a", "e", "i", "o", "u"]
  for i in a:
    if i in vowels:
      print(i)


findVowels("Hello how are you")
