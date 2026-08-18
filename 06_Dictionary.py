s1 = input("enter chemistry's marks:")
s2 = input("enter math's marks:")
s3 = input("enter phy's marks:")

# dict = {
#     "chemistry" : s1,
#     "maths" : s2,
#     "phys" : s3,
# }

dict = {}
new_dict = {"chemistry" : s1}
dict.update(new_dict)

new_dict = {"maths" : s2}
dict.update(new_dict)

new_dict = {"phys" : s3}
dict.update(new_dict)

print(dict) #{'chemistry': '3', 'maths': '4', 'phys': '6'}

#########################
#######Assign Value######
#########################

dict = {
    "name" : "naila",
    "age" : "36",
    "course" :{
        "python" : 90,
        "maths" : 100,
        "chem" : 80,
    }
    
}
dict["age"] = 78
print(dict["age"]) #78

##############################
#### GET IN DICT #############
##############################

dict = {
    "name" : "naila",
    "age" : "36",
    "course" :{
        "python" : 90,
        "maths" : 100,
        "chem" : 80,
    }
    
}
print(dict.get("course")) #{'python': 90, 'maths': 100, 'chem': 80}
print(dict["course"]) #{'python': 90, 'maths': 100, 'chem': 80}

##################################33

def find_student(students, name):
    for student in students:

        if student["name"] == name:

            total = sum(student["marks"])
            average = total / len(student["marks"])

            if average >= 90:
                grade = "A"
            elif average >= 80:
                grade = "B"
            elif average >= 70:
                grade = "C"
            else:
                grade = "D"

            return {
                "name": student["name"],
                "total": total,
                "average": average,
                "grade": grade
            }

    return None


students = [
    {"name": "Ali", "marks": [80, 90, 85]},
    {"name": "Sara", "marks": [95, 92, 98]},
    {"name": "Ahmed", "marks": [70, 75, 68]}
]

result = find_student(students, "Sara")

print(result)