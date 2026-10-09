# 27. Salaries of employees
salaries = [25000, 52000, 31000, 75000, 28000, 45000, 60000, 22000, 39000, 51000]
average = sum(salaries) / len(salaries)
above_50k = [s for s in salaries if s > 50000]
below_30k = [s for s in salaries if s < 30000]
print("Salaries:", salaries)
print("Highest salary:", max(salaries))
print("Lowest salary:", min(salaries))
print("Average salary:", round(average, 2))
print("Employees earning above Rs. 50,000:", len(above_50k), above_50k)
print("Employees earning below Rs. 30,000:", len(below_30k), below_30k)
