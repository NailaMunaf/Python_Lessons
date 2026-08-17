def sum(n):
    x = 0
    if(n == 0):
        return 0
    return  sum(n-1) + n

print(sum(3))

#####################

def fact(n):
    if(n == 0 or n == 1):
        return 1
    return fact(n-1) * n

print(fact(5))


#############################

def pr(list, index = 0):
        if(index == len(list)):
               return 
        print(list[index])
        pr(list, index+1)

pr([1, 2, 3])

################################

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    print("END") #end will be printed 5 time, while returning to the end layer

show(5)
