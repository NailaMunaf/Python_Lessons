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

##############################

def find_largest(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


numbers = [45, 12, 89, 34, 67]

result = find_largest(numbers)

print("Largest:", result)

#################################

def calculate_grade(marks):
    total = 0

    for mark in marks:
        total += mark

    average = total / len(marks)

    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


marks = [85, 90, 88, 92]

grade = calculate_grade(marks)

print("Grade:", grade)