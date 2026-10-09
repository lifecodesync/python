# 12. Display all elements present at even index positions
nums = [5, 10, 15, 20, 25, 30, 35, 40]
print("List:", nums)
print("Elements at even index positions:")
for i in range(0, len(nums), 2):
    print("Index", i, "->", nums[i])
