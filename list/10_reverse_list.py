# 10. Reverse a list without using reverse()
nums = [1, 2, 3, 4, 5, 6]
reversed_list = []
for i in range(len(nums) - 1, -1, -1):
    reversed_list.append(nums[i])
print("Original list:", nums)
print("Reversed list:", reversed_list)
