class Student:
    college_name = "ABC college"  #stored once bcz all have same coll
    def __init__(self, name, marks): #init is called everytime object is created
        self.name = name
        self.marks = marks
        print("adding new students in Database..")

    def pr(self):
        print("Name:", self.name, ", Marks:", self.marks)

s1 = Student("Naila", 89)
s1.pr() #Naila

s2 = Student("Fatima", 90)
s2.pr()

# print(s2.college_name) #or (Student.college_name)

#write print function