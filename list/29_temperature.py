# 29. Temperature of 30 days
temps = [31, 33, 29, 35, 36, 30, 28, 32, 34, 37,
         33, 31, 29, 27, 30, 32, 35, 38, 36, 34,
         31, 30, 29, 28, 33, 35, 32, 31, 30, 29]
average = sum(temps) / len(temps)
hottest = temps.index(max(temps)) + 1
coldest = temps.index(min(temps)) + 1
above = sum(1 for t in temps if t > average)
below = sum(1 for t in temps if t < average)
print("Temperatures:", temps)
print("Hottest day: Day", hottest, "-", max(temps), "C")
print("Coldest day: Day", coldest, "-", min(temps), "C")
print("Average temperature:", round(average, 2), "C")
print("Days above average:", above)
print("Days below average:", below)
