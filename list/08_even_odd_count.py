# 8. Count even and odd numbers in a list of 15 integers
nums = [12, 7, 9, 20, 33, 44, 51, 68, 71, 80, 93, 102, 115, 126, 137]
even = 0
odd = 0
for n in nums:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
print("List:", nums)
print("Even count:", even)
print("Odd count:", odd)
