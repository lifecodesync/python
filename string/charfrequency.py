s = input("Enter a string: ")

for ch in s:
    if s.index(ch) == s.find(ch):
        print(ch, ":", s.count(ch))