# 22. Find common elements between two lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]
common = []
for x in list1:
    if x in list2 and x not in common:
        common.append(x)
print("List 1:", list1)
print("List 2:", list2)
print("Common elements:", common)
