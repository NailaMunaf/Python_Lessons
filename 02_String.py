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

################################

str = "im eating Apple" 
str = str.capitalize()
print (str) #Im eating apple

###################

str = "im eating Apple" 
print(str.endswith("ple")) #True

##########################

str = "im eating Apple" 
print (str.find("Apple")) #10
#A is at 11th number

############################

str = "im eating Apple" 
print (str.replace("Apple" , "Mango")) #im eating Mango

###########################

str = "im$am$naila"
print(str.count("$")) #2

########################

str = input("enter your first name:")
print(len(str))

#########################