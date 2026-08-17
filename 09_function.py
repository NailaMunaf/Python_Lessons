def eo():
    x = int(input("enter a number: "))
    if(x%2 == 0):
        print("EVEN")
    else:
        print("ODD")
        return
    
eo()

##############################

def factorial(n):
    elements = range(1,n+1)
    fact = 1
    i = 1
    for el in elements:
        fact *= i
        i += 1
    return fact

output = factorial(5)
print(output)

###############################

def ftn(a,b):
       return a + b

sum = ftn( 1, 3)
print(sum)


##############################

def conv(usd):
    pkr = usd*278.30
    print(pkr)
    return

conv(2)
