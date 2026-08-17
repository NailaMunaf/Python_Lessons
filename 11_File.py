count = 0
with open("numbers.txt", "r") as f:
    data = f.read()
    nums = data.split(",")
          
    for el in nums:
        if(int(el) % 2 == 0):
            count += 1
print(count)

##################################
#########EXTRACTING NUMBERS#######
##################################

with open("numbers.txt", "r") as f:
    data = f.read()
    print(data)

    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]
print (num) #prints last num

############ READS 5 CHARC ##############

f = open("data.txt", "r")
data = f.read(5) #reading 5 characters
print(data)
print(type(data))
f.close()

############ READS LINES #################

f = open("data.txt", "r")

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)

line4 = f.readline()
print(line4) #prints empty line if file ends 

f.close()


########### REPLACE WORD ############
with open("data.txt", "r") as f:

    data = f.read()
    print(data)

    new_data = data.replace("python", "Java")
    print(new_data)

############ write file ############
f = open("data.txt", "a")
f.write("\nWriting in a file") #append in next line at end of file
f.close()
