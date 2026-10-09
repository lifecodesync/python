# 15. Find the second largest element in a list
nums = [45, 12, 78, 3, 89, 56, 89, 23]
largest = second = None
for n in nums:
    if largest is None or n > largest:
        second = largest
        largest = n
    elif n != largest and (second is None or n > second):
        second = n
print("List:", nums)
if second is None:
    print("No second largest element")
else:
    print("Second largest:", second)
