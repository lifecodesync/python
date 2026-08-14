s = input("Enter a string: ")

most = s[0]
max_count = 0

for ch in s:
    count = s.count(ch)

    if count > max_count:
        max_count = count
        most = ch

print("Most frequent character:", most)