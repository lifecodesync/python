# 24. Rotate a list left and right by one position
nums = [1, 2, 3, 4, 5]
left = nums[1:] + nums[:1]
right = nums[-1:] + nums[:-1]
print("Original list:", nums)
print("Left rotated by 1:", left)
print("Right rotated by 1:", right)
