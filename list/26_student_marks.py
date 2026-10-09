# 26. Marks of 20 students
marks = [78, 85, 62, 90, 45, 88, 73, 95, 56, 69,
         81, 77, 92, 58, 66, 84, 71, 99, 40, 63]
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)
above = 0
below = 0
for m in marks:
    if m > average:
        above += 1
    elif m < average:
        below += 1
print("Marks:", marks)
print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", round(average, 2))
print("Students above average:", above)
print("Students below average:", below)
