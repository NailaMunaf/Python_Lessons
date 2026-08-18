nam1 = input("enter 1st name")
nam2 = input("enter 2nd name")
nam3 = input("enter 3rd name")

names = []
names.append(nam1)
names.append(nam2)
names.append(nam3)

print(names) #['naila', 'abdul', 'manaf']
# explore few more functions for list

###############################
####READS SAME FROM END########
###############################

list = [1, "abc", "abc", 1]
lc = list.copy()
list.reverse()
if(lc == list):
    print("True")
else:
    print("false")

##############################

list = [1, "abc", "abc", 1]
list.insert(1,5) #insert(ind, el)
print(list) #[1, 5, 'abc', 'abc', 1]

###############################

numbers = [10, 20, 30]
print(numbers.index(20)) #1

##############################

list = [20, 10, 20, 30, 40]
list.remove(20) # #removes first occurrence of element
print(list) #[10, 20, 30, 40] 

##########################

list.pop(3) #pop(indx) removes element at idx 
print(list) #[10, 20, 30]

###########################

list = ["C", "D", "A", "A", "B", "B", "A"]
list.sort()
print(list) #['A', 'A', 'A', 'B', 'B', 'C', 'D']

############ removing duplicates ########

numbers = [10, 20, 10, 30, 20, 40, 10]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)
