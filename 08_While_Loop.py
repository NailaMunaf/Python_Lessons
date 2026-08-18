i = 1

while i <= 10:
    print(i*i)  #Squaring
    i += 1

#########################

n = int(input("enter n: "))
i = 0
x = 0

while i <= n:
    x = x + i
    i += 1
print("sum is: " , x) #sum of n numbers is printed


###################################

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100 )

x = int(input("enter x:"))
i = 0

while (i < (len(tup))):
    if(x == tup[i]):
        print(x, "lies in list")
    else:
        print(x, "is not in the list") #prints for every el not in the list
    i += 1

######################################

i = 1

while i <= 10:
    if i == 6:
        break #breaks the loop
    print(i) # 1-5 printed
    i += 1
##############################

number = 0

while number != 5:
    number = int(input("Enter 5: "))

print("Correct!")

####### Changes even nums #########

numbers = [2, 5, 8, 11, 14]

i = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        numbers[i] = numbers[i] * 2

    i += 1

print(numbers)