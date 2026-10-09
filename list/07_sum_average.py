# 7. Accept 10 numbers from the user, calculate sum and average
nums = []
for i in range(10):
    n = float(input(f"Enter number {i + 1}: "))
    nums.append(n)
total = 0
for n in nums:
    total += n
print("Numbers:", nums)
print("Sum:", total)
print("Average:", total / len(nums))
