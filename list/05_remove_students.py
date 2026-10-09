# 5. Remove first student, last student and a specific student by name
students = ["Amit", "Riya", "Sneha", "Rahul", "Priya", "Karan"]
print("Original list:", students)
students.pop(0)          # first student
students.pop()           # last student
students.remove("Rahul") # specific student
print("Remaining list:", students)
