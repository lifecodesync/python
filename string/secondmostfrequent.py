s = input("Enter a string: ")

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

values = sorted(freq.values(), reverse=True)

if len(values) >= 2:
    second = values[1]

    for ch in freq:
        if freq[ch] == second:
            print("Second most frequent:", ch)
            break
else:
    print("No second character")