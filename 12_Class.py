class Student:
    college_name = "ABC college"  #stored once bcz all have same coll
    def __init__(self, name, marks): #init is called everytime object is created
        self.name = name
        self.marks = marks
        print("adding new students in Database..")

s1 = Student("Naila", 89)
print(s1.name, s1.marks) #Naila

s2 = Student("Fatima", 90)
print(s2.name, s2.marks)
print(s2.college_name) #or (Student.college_name)
