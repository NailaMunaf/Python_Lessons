a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
d = int(input("enter fourth number:"))

if(a >= b and a >= c and a >= d):
    print("greatest number is:" , a)
elif( b >= c and b >= d):
    print("greatest number is:" , b)
elif(c >= d):
    print("greatest number is:" , c)
else:
    print("greatest number is:" , d)
