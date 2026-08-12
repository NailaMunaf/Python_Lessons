count = 0
with open("numbers.txt", "r") as f:
    data = f.read()
    nums = data.split(",")
          
    for el in nums:
        if(int(el) % 2 == 0):
            count += 1
print(count)
