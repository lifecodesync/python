# 14. Display only unique elements from a list containing duplicates
nums = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6]
unique = []
for n in nums:
    if n not in unique:
        unique.append(n)
print("Original list:", nums)
print("Unique elements:", unique)
