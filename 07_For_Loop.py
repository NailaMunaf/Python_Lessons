n = 5
fact = 1

for i in range(1, n+1): #last number is not included
    fact *= i
print("factorial = ", fact)

'''
Factorial of 5
i = 1, fact = 1
i = 2, fact = 2
i = 3, fact = 6
i = 4, fact = 24
i = 5, fact = 120
'''

###############################
### Find element in the list###
###############################

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("enter number"))

for el in tup:
    if(el == x):
        print(el, "is in the list")
print("not in list") #it executes where el in in list or not

###################################
###Continue########################
###################################

list = [1, 2, 3, 4]

for el in list:
    if(el == 3):
       continue    #it doesnt print el
    print(el)
else:
    print("END") #it is printed without any condition

##########################################
###############pass######################
########################################

for i in range(1, 11):
    pass #moves forward
print("end of loop") #this is printed once at the end of loop

i = 0
if(i == 5):
    pass
print("end") #this is printed once also

#########################################

fruits = ["apple", "banana", "mango", "orange"]

for fruit in fruits:
    position = fruits.index(fruit)
    print(fruit, position)

########################

numbers = [1, 2, 3]

for i in numbers:
    for j in numbers:
        print(i, j)