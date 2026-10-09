# 13. Accept 10 numbers and sort them in ascending and descending order
nums = []
for i in range(10):
    nums.append(int(input(f"Enter number {i + 1}: ")))
print("Ascending order:", sorted(nums))
print("Descending order:", sorted(nums, reverse=True))
