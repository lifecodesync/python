# 16. Nested list storing student name, roll number and marks
students = [
    ["Amit", 101, 85],
    ["Riya", 102, 92],
    ["Sneha", 103, 78],
    ["Rahul", 104, 88],
]
print("Name\tRoll No\tMarks")
for s in students:
    print(f"{s[0]}\t{s[1]}\t{s[2]}")
