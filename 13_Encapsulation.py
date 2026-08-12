class Student:
   
    def __init__(self, name, marks_list):
        self.name = name
        self.marks_list = marks_list 
   
    @staticmethod  #To make a function static we write decorator and it changes   
    def hello():
        print("hellow")  

    def ave_marks(self, marks_list):
        ave = (marks_list[0] + marks_list[1] + marks_list[2])/3
        return ave
            

s1 = Student("Naila", [100, 99, 98])
print(s1.ave_marks([100, 99, 98]))
s1.hello()

#encapsulation^^ attributes and methods are encapsuled.