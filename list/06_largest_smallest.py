# 6. Find the largest and smallest number without max() or min()
nums = [45, 12, 78, 3, 56, 89, 23]
largest = nums[0]
smallest = nums[0]
for n in nums:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n
print("List:", nums)
print("Largest:", largest)
print("Smallest:", smallest)
