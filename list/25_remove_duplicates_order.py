# 25. Remove duplicates while preserving original order
items = [5, 3, 5, 2, 3, 8, 2, 9, 1, 8]
result = []
for x in items:
    if x not in result:
        result.append(x)
print("Original list:", items)
print("Without duplicates:", result)
