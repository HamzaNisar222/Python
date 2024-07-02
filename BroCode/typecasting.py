#Type casting means changing one datatype to another 
a=20 #int
b=2.0 #float
c="88" #string

print(a)
print(b) 
print(c*3)#cannot perform maths operation on a string

x=float(a)#change int to float
y=int(b)#change to int from float
z=int(c)#change from string to int

print(x)#return float instead of int 
print(y)#return int instead of float 
print(z*3)#maths on int change fro string
