set1 = set() #empty set
set1.add(1)
set1.add(2)
set1.add(2)
set1.add("naila")
set1.add(("a", "B", "c"))
print(set1) #{1, 2, 'naila', ('a', 'B', 'c')}
set1.remove(2) #it will remove 2 from set
print(set1) #{1, 'naila', ('a', 'B', 'c')}

#########################

set1.pop() # removes a random value 
print(set1) # {('a', 'B', 'c'), 'naila'}

#############################
###storing 9 and 9.0 in set##
#############################

# set = {9, "9.0"}
set = {("int", 9), ("float", 9.0)}
print(set)

############################

set1 = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C" }
print("number of classrooms:", len(set1))

###############################

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))  #{1, 2, 3, 4, 5}
