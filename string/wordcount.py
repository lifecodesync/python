s = input("Enter a sentence: ")

words = s.split()

count = 0
for word in words:
    count += 1

print("Number of words:", count)