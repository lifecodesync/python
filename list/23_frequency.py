# 23. Count the frequency of each element in a list
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
freq = {}
for n in nums:
    freq[n] = freq.get(n, 0) + 1
print("List:", nums)
for key, count in freq.items():
    print(key, "->", count)
