# Student dictonary with name and grades
student={'Aarav':'A+',
         'Ishani':'C+',
         'Diya':'D',
         'Vihaan':'B',
         'Sai':'A'
}
print(student)

#added new student in dictonary 

new_name = input("Enter the student's name: ")
new_grade = input("Enter the student's grade: ")
student[new_name] = new_grade
print(student)

#Updating value of existing student 
name = input("Enter the name of the student you want to update: ")
if name in student:
    new_grade = input("Enter the new grade for: ")
    student[name] = new_grade
    print("New grades updated successfully!")
else:
    print("Invaild name")
print(student)
